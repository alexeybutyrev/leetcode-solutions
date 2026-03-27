#!/usr/bin/env node
import { LeetCode, Credential } from 'leetcode-query';
import fs from 'fs';
import path from 'path';

const LEETCODE_SESSION = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjEzMTcwNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjkwZDZhNWU1YWUxYjQyMmM1MmFjNmFmZWVhZmQwZGVmYmQ3NTQ2NGJiODJmZDYyZGEzMTgyNmFkMzI3ZDU3MTQiLCJzZXNzaW9uX3V1aWQiOiI2MjJjYzlmNCIsImlkIjoyMTMxNzA0LCJlbWFpbCI6ImJ1dGlyZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhbGV4ZXlfd2lzaCIsInVzZXJfc2x1ZyI6ImFsZXhleV93aXNoIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2FsZXhleV93aXNoL2F2YXRhcl8xNjMzMDkwMTE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3NDYzOTY1NCwiaXAiOiIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiLCJpZGVudGl0eSI6IjAyMzc5OTUzYjkzY2QyMjMyNDNkYjA5ZjFkZDRlNWI5IiwiZGV2aWNlX3dpdGhfaXAiOlsiOGY5YTVmMjg1MGEwNTNmYzZiMzkxZjcyYzcyNDJhMjgiLCIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.7RTqTK3erFDe-vhBxdrtOyyC3zFCD8nF1oxTbC5cGiA';

// Use absolute path for output directory
const OUTPUT_DIR = '/home/node/.openclaw/workspace/leetcode-solutions/solutions';

const langToExt = {
  python: 'py', python3: 'py', java: 'java', javascript: 'js', typescript: 'ts',
  cpp: 'cpp', c: 'c', csharp: 'cs', go: 'go', rust: 'rs', ruby: 'rb',
  swift: 'swift', kotlin: 'kt', scala: 'scala', php: 'php', mysql: 'sql',
  mssql: 'sql', oracle: 'sql', bash: 'sh', racket: 'rkt', elixir: 'ex', dart: 'dart'
};

function sanitizeFilename(name) {
  return name.replace(/[^a-zA-Z0-9 \-_]/g, '_');
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Retry with exponential backoff
async function withRetry(fn, maxRetries = 5, baseDelay = 2000) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (err.message?.includes('504') || err.message?.includes('Gateway') || err.message?.includes('timeout')) {
        const delay = baseDelay * Math.pow(2, i);
        console.log(`Retry ${i + 1}/${maxRetries} after error (waiting ${delay}ms)...`);
        await sleep(delay);
      } else {
        throw err;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

async function main() {
  console.log('=== LeetCode Solutions Scraper ===\n');
  
  // Create output directory
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  console.log(`Output directory: ${OUTPUT_DIR}\n`);
  
  const credential = new Credential();
  await credential.init(LEETCODE_SESSION);
  const leetcode = new LeetCode(credential);
  
  // Get user info
  const whoami = await withRetry(() => leetcode.whoami());
  console.log(`Authenticated as: ${whoami.username}\n`);
  
  // Get all submissions with pagination
  console.log('Fetching all submissions...');
  const allSubmissions = [];
  let offset = 0;
  const limit = 50;
  let lastCount = limit;
  
  while (lastCount === limit) {
    const subs = await withRetry(() => leetcode.submissions({ limit, offset }));
    lastCount = subs.length;
    
    // Filter accepted
    const accepted = subs.filter(s => s.statusDisplay === 'Accepted');
    allSubmissions.push(...accepted);
    
    console.log(`Fetched ${subs.length} (offset ${offset}) - ${accepted.length} accepted (total: ${allSubmissions.length})`);
    
    offset += limit;
    await sleep(800);  // Slower to avoid rate limiting
  }
  
  console.log(`\nTotal accepted submissions: ${allSubmissions.length}`);
  
  // Group by problem+language, keep best runtime
  const problems = new Map();
  for (const sub of allSubmissions) {
    const key = `${sub.titleSlug}|${sub.lang}`;
    if (!problems.has(key)) {
      problems.set(key, sub);
    } else {
      const existing = problems.get(key);
      if (sub.runtime && existing.runtime && sub.runtime < existing.runtime) {
        problems.set(key, sub);
      }
    }
  }
  
  console.log(`Unique problem+language: ${problems.size}\n`);
  
  // Fetch code and save each solution
  let savedCount = 0;
  let noCodeCount = 0;
  let errorCount = 0;
  const langStats = new Map();
  
  // Load already saved (to resume if interrupted)
  const savedFile = '/home/node/.openclaw/workspace/leetcode-solutions/.saved.json';
  let saved = new Set();
  if (fs.existsSync(savedFile)) {
    saved = new Set(JSON.parse(fs.readFileSync(savedFile, 'utf-8')));
    console.log(`Resuming: ${saved.size} already saved`);
  }
  
  for (const [key, sub] of problems) {
    if (saved.has(key)) {
      savedCount++;
      continue;
    }
    
    try {
      // Get submission details with code
      const details = await withRetry(() => leetcode.submission(sub.id));
      const code = details?.code;
      
      if (!code) {
        noCodeCount++;
        console.log(`No code for: ${sub.title}`);
        saved.add(key); // Mark as processed even without code
        continue;
      }
      
      // Create problem directory
      const titleSanitized = sanitizeFilename(sub.title);
      const problemDir = path.join(OUTPUT_DIR, titleSanitized);
      fs.mkdirSync(problemDir, { recursive: true });
      
      const ext = langToExt[sub.lang?.toLowerCase()] || sub.lang?.toLowerCase() || 'txt';
      const filepath = path.join(problemDir, `solution.${ext}`);
      
      // Create header
      let header = `// Problem: ${sub.title}\n// Language: ${sub.lang}\n// Runtime: ${sub.runtime} ms\n// Memory: ${sub.memory} MB\n\n`;
      if (['py', 'rb', 'sh', 'ex'].includes(ext)) {
        header = header.replace(/\/\//g, '#');
      } else if (ext === 'sql') {
        header = header.replace(/\/\//g, '--');
      }
      
      fs.writeFileSync(filepath, header + code, 'utf-8');
      savedCount++;
      saved.add(key);
      
      // Track language stats
      langStats.set(sub.lang, (langStats.get(sub.lang) || 0) + 1);
      
      // Save progress every 50 solutions
      if (savedCount % 50 === 0) {
        fs.writeFileSync(savedFile, JSON.stringify([...saved]), 'utf-8');
      }
      
      console.log(`Saved: ${sub.title} (${sub.lang}) - ${savedCount}/${problems.size}`);
      
      await sleep(300);
    } catch (err) {
      errorCount++;
      console.log(`Error: ${sub.title} - ${err.message}`);
      await sleep(2000);  // Wait longer after error
    }
  }
  
  // Save final state
  fs.writeFileSync(savedFile, JSON.stringify([...saved]), 'utf-8');
  
  // Create README
  const uniqueProblems = new Set([...problems.values()].map(s => s.titleSlug)).size;
  
  let readme = `# LeetCode Solutions

My LeetCode solutions scraped automatically.

## Stats

- Total solutions: **${savedCount}**
- Problems solved: **${uniqueProblems}**
- No code available: ${noCodeCount}
- Errors: ${errorCount}

## Languages

| Language | Count |
|----------|-------|
`;
  
  for (const [lang, count] of [...langStats.entries()].sort((a, b) => b[1] - a[1])) {
    readme += `| ${lang} | ${count} |\n`;
  }
  
  readme += `
## Structure

\`\`\`
solutions/
├── problem-name/
│   └── solution.<ext>
\`\`\`
`;
  
  fs.writeFileSync('/home/node/.openclaw/workspace/leetcode-solutions/README.md', readme, 'utf-8');
  console.log('\nCreated README.md');
  
  console.log(`\n=== Complete! Saved ${savedCount} solutions ===`);
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
