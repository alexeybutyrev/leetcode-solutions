#!/usr/bin/env node
// Direct GraphQL approach with manual fetch
import fs from 'fs';
import path from 'path';

const LEETCODE_SESSION = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjEzMTcwNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjkwZDZhNWU1YWUxYjQyMmM1MmFjNmFmZWVhZmQwZGVmYmQ3NTQ2NGJiODJmZDYyZGEzMTgyNmFkMzI3ZDU3MTQiLCJzZXNzaW9uX3V1aWQiOiI2MjJjYzlmNCIsImlkIjoyMTMxNzA0LCJlbWFpbCI6ImJ1dGlyZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhbGV4ZXlfd2lzaCIsInVzZXJfc2x1ZyI6ImFsZXhleV93aXNoIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2FsZXhleV93aXNoL2F2YXRhcl8xNjMzMDkwMTE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3NDYzOTY1NCwiaXAiOiIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiLCJpZGVudGl0eSI6IjAyMzc5OTUzYjkzY2QyMjMyNDNkYjA5ZjFkZDRlNWI5IiwiZGV2aWNlX3dpdGhfaXAiOlsiOGY5YTVmMjg1MGEwNTNmYzZiMzkxZjcyYzcyNDJhMjgiLCIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.7RTqTK3erFDe-vhBxdrtOyyC3zFCD8nF1oxTbC5cGiA';

const GRAPHQL_URL = 'https://leetcode.com/graphql';

const langToExt = {
  python: 'py', python3: 'py', java: 'java', javascript: 'js', typescript: 'ts',
  cpp: 'cpp', c: 'c', csharp: 'cs', go: 'go', rust: 'rs', ruby: 'rb',
  swift: 'swift', kotlin: 'kt', scala: 'scala', php: 'php', mysql: 'sql',
  mssql: 'sql', oracle: 'sql', bash: 'sh', racket: 'rkt', elixir: 'ex', dart: 'dart'
};

function sanitizeFilename(name) {
  return name.replace(/[^a-zA-Z0-9 \-_]/g, '_');
}

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function graphql(query, variables = {}) {
  const res = await fetch(GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Cookie': `LEETCODE_SESSION=${LEETCODE_SESSION}`,
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    },
    body: JSON.stringify({ query, variables })
  });
  
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  }
  
  const data = await res.json();
  if (data.errors) {
    throw new Error(`GraphQL Error: ${JSON.stringify(data.errors)}`);
  }
  return data.data;
}

async function main() {
  console.log('=== LeetCode Solutions Scraper ===\n');
  
  // Get the username from whoami
  const whoamiQuery = `
    query {
      userStatus {
        username
        isSignedIn
      }
    }
  `;
  
  const whoami = await graphql(whoamiQuery);
  const username = whoami.userStatus?.username;
  console.log(`Authenticated as: ${username}\n`);
  
  if (!username) {
    throw new Error('Not authenticated');
  }
  
  // Get solved problems count
  const profileQuery = `
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        submitStats: submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
  `;
  
  const profile = await graphql(profileQuery, { username });
  const stats = profile.matchedUser?.submitStats?.acSubmissionNum || [];
  const totalSolved = stats.find(s => s.difficulty === 'All')?.count || 0;
  console.log(`Total solved: ${totalSolved}\n`);
  
  // Get the problems the user has solved
  // Use the correct GraphQL query structure
  const problemsQuery = `
    query problemsetQuestionsList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        totalNum
        questions: data {
          acRate
          difficulty
          freqBar
          frontendQuestionId: questionFrontendId
          isFavor
          paidOnly: isPaidOnly
          status
          title
          titleSlug
          topicTags {
            name
            id
            slug
          }
        }
      }
    }
  `;
  
  // Get all problems and filter by status = "ac"
  let allProblems = [];
  let skip = 0;
  const limit = 100;
  
  while (true) {
    const result = await graphql(problemsQuery, {
      categorySlug: 'all-code-essentials',
      limit,
      skip,
      filters: { status: 'AC' }  // Only solved problems
    });
    
    const questions = result.problemsetQuestionList?.questions || [];
    if (questions.length === 0) break;
    
    allProblems.push(...questions);
    console.log(`Fetched ${questions.length} solved problems (total: ${allProblems.length})`);
    
    const totalNum = result.problemsetQuestionList?.totalNum || 0;
    if (questions.length < limit || allProblems.length >= totalNum) break;
    skip += limit;
    await sleep(1000);
  }
  
  console.log(`\nTotal solved problems found: ${allProblems.length}\n`);
  
  // Now get submissions for each problem
  const solutionsDir = path.join(process.cwd(), 'solutions');
  fs.mkdirSync(solutionsDir, { recursive: true });
  
  let savedCount = 0;
  let errorCount = 0;
  
  for (const problem of allProblems) {
    try {
      // Get the user's accepted submission for this problem
      const submissionQuery = `
        query submissions($questionSlug: String!, $limit: Int, $offset: Int) {
          questionSubmissionList(questionSlug: $questionSlug, limit: $limit, offset: $offset) {
            submissions {
              id
              code
              lang
              statusDisplay
              runtime
              memory
            }
          }
        }
      `;
      
      await sleep(300);
      const subResult = await graphql(submissionQuery, {
        questionSlug: problem.titleSlug,
        limit: 10,
        offset: 0
      });
      
      const submissions = subResult.questionSubmissionList?.submissions || [];
      const accepted = submissions.filter(s => s.statusDisplay === 'Accepted');
      
      if (accepted.length === 0) {
        console.log(`No accepted submission for: ${problem.title}`);
        continue;
      }
      
      // Take the best runtime
      accepted.sort((a, b) => {
        const runtimeA = parseFloat(a.runtime?.replace('ms', '') || '999999');
        const runtimeB = parseFloat(b.runtime?.replace('ms', '') || '999999');
        return runtimeA - runtimeB;
      });
      
      const best = accepted[0];
      const code = best.code;
      
      if (!code) {
        console.log(`No code for: ${problem.title}`);
        continue;
      }
      
      // Create problem directory
      const titleSanitized = sanitizeFilename(problem.title);
      const problemDir = path.join(solutionsDir, titleSanitized);
      fs.mkdirSync(problemDir, { recursive: true });
      
      const ext = langToExt[best.lang?.toLowerCase()] || best.lang?.toLowerCase() || 'txt';
      const filepath = path.join(problemDir, `solution.${ext}`);
      
      let header = `// Problem: ${problem.title}\n// Difficulty: ${problem.difficulty}\n// Language: ${best.lang}\n// Runtime: ${best.runtime || 'N/A'}\n// Memory: ${best.memory || 'N/A'}\n\n`;
      
      if (['py', 'rb', 'sh', 'ex'].includes(ext)) {
        header = header.replace(/\/\//g, '#');
      } else if (ext === 'sql') {
        header = header.replace(/\/\//g, '--');
      }
      
      fs.writeFileSync(filepath, header + code, 'utf-8');
      savedCount++;
      console.log(`Saved: ${problem.title} (${best.lang})`);
      
    } catch (err) {
      errorCount++;
      console.log(`Error: ${problem.title} - ${err.message}`);
    }
  }
  
  // Create README
  let readme = `# LeetCode Solutions

My LeetCode solutions scraped automatically.

## Stats

- Total solutions: ${savedCount}
- Problems solved: ${allProblems.length}

## Structure

\`\`\`
solutions/
├── problem-name/
│   └── solution.<ext>
\`\`\`
`;
  
  fs.writeFileSync('README.md', readme, 'utf-8');
  console.log('\nCreated README.md');
  
  console.log(`\n=== Complete! Saved ${savedCount} solutions (${errorCount} errors) ===`);
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
