#!/usr/bin/env node
import { LeetCode, Credential } from 'leetcode-query';
import fs from 'fs';
import path from 'path';

const LEETCODE_SESSION = process.env.LEETCODE_SESSION || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjEzMTcwNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjkwZDZhNWU1YWUxYjQyMmM1MmFjNmFmZWVhZmQwZGVmYmQ3NTQ2NGJiODJmZDYyZGEzMTgyNmFkMzI3ZDU3MTQiLCJzZXNzaW9uX3V1aWQiOiI2MjJjYzlmNCIsImlkIjoyMTMxNzA0LCJlbWFpbCI6ImJ1dGlyZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhbGV4ZXlfd2lzaCIsInVzZXJfc2x1ZyI6ImFsZXhleV93aXNoIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2FsZXhleV93aXNoL2F2YXRhcl8xNjMzMDkwMTE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3NDYzOTY1NCwiaXAiOiIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiLCJpZGVudGl0eSI6IjAyMzc5OTUzYjkzY2QyMjMyNDNkYjA5ZjFkZDRlNWI5IiwiZGV2aWNlX3dpdGhfaXAiOlsiOGY5YTVmMjg1MGEwNTNmYzZiMzkxZjcyYzcyNDJhMjgiLCIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.7RTqTK3erFDe-vhBxdrtOyyC3zFCD8nF1oxTbC5cGiA';

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

async function withRetry(fn, maxRetries = 3, delayMs = 5000) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (err.message?.includes('504') || err.message?.includes('Gateway')) {
        console.log(`Retry ${i + 1}/${maxRetries} after 504 error...`);
        await sleep(delayMs * (i + 1));
      } else {
        throw err;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

async function main() {
  console.log('=== LeetCode Solutions Scraper ===\n');
  
  // Initialize with session cookie
  console.log('Authenticating...');
  const credential = new Credential();
  await credential.init(LEETCODE_SESSION);
  
  const leetcode = new LeetCode(credential);
  
  // Get user info
  const whoami = await leetcode.whoami();
  console.log(`Authenticated as: ${whoami.username || whoami.login}\n`);
  
  // Get all submissions (need to paginate through all)
  console.log('Fetching all submissions...');
  const allSubmissions = [];
  let offset = 0;
  const limit = 50;  // Smaller batches
  let total = 0;
  
  while (true) {
    const result = await withRetry(() => leetcode.submissions({ limit, offset }));
    
    if (!result || !result.submissions || result.submissions.length === 0) {
      break;
    }
    
    // Filter accepted submissions
    const accepted = result.submissions.filter(s => s.statusDisplay === 'Accepted');
    allSubmissions.push(...accepted);
    
    total = result.total || total;
    console.log(`Fetched ${result.submissions.length} (offset ${offset}/${total || '?'}) - ${accepted.length} accepted`);
    
    if (result.submissions.length < limit) {
      break;
    }
    
    offset += limit;
    await sleep(3000);  // Slower to avoid rate limiting
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
      // Keep faster runtime
      if (sub.runtime && existing.runtime) {
        try {
          const curr = parseFloat(sub.runtime);
          const prev = parseFloat(existing.runtime);
          if (curr < prev) problems.set(key, sub);
        } catch {}
      }
    }
  }
  
  console.log(`Unique problem+language: ${problems.size}\n`);
  
  // Create solutions directory
  const solutionsDir = path.join(process.cwd(), 'solutions');
  fs.mkdirSync(solutionsDir, { recursive: true });
  
  // Fetch code and save each solution
  let savedCount = 0;
  const problemCache = new Map();
  
  for (const [key, sub] of problems) {
    try {
      // Get problem info
      if (!problemCache.has(sub.titleSlug)) {
        const problem = await withRetry(() => leetcode.problem(sub.titleSlug));
        problemCache.set(sub.titleSlug, problem);
        await sleep(500);
      }
      
      const problem = problemCache.get(sub.titleSlug);
      const difficulty = problem?.difficulty || 'Unknown';
      
      // Get submission details (code)
      const details = await withRetry(() => leetcode.submission(sub.id));
      const code = details?.code || '';
      
      if (!code) {
        console.log(`Skipping ${sub.title} - no code`);
        continue;
      }
      
      // Create problem directory
      const titleSanitized = sanitizeFilename(sub.title);
      const problemDir = path.join(solutionsDir, titleSanitized);
      fs.mkdirSync(problemDir, { recursive: true });
      
      // Determine file extension
      const ext = langToExt[sub.lang?.toLowerCase()] || sub.lang?.toLowerCase() || 'txt';
      const filepath = path.join(problemDir, `solution.${ext}`);
      
      // Create header
      let header = `// Problem: ${sub.title}\n// Difficulty: ${difficulty}\n// Language: ${sub.lang}\n// Runtime: ${sub.runtime || 'N/A'}\n// Memory: ${sub.memory || 'N/A'}\n\n`;
      
      // Adjust comment style
      if (['py', 'rb', 'sh', 'ex'].includes(ext)) {
        header = header.replace(/\/\//g, '#');
      } else if (ext === 'sql') {
        header = header.replace(/\/\//g, '--');
      }
      
      fs.writeFileSync(filepath, header + code, 'utf-8');
      savedCount++;
      console.log(`Saved: ${sub.title} (${sub.lang})`);
      
      await sleep(500);
    } catch (err) {
      console.log(`Error saving ${sub.title}: ${err.message}`);
    }
  }
  
  // Create README
  const langs = [...new Set([...problems.values()].map(s => s.lang))].sort();
  const problemSlugs = [...new Set([...problems.values()].map(s => s.titleSlug))];
  
  let readme = `# LeetCode Solutions

My LeetCode solutions scraped automatically.

## Stats

- Total solutions: ${savedCount}
- Problems solved: ${problemSlugs.length}

## Structure

\`\`\`
solutions/
├── problem-name/
│   └── solution.<ext>
\`\`\`

## Languages Used

`;
  for (const lang of langs) {
    readme += `- ${lang}\n`;
  }
  
  fs.writeFileSync('README.md', readme, 'utf-8');
  console.log('\nCreated README.md');
  
  console.log(`\n=== Complete! Saved ${savedCount} solutions ===`);
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
