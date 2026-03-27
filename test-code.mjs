#!/usr/bin/env node
// Test getting submission code
import { LeetCode, Credential } from 'leetcode-query';

const LEETCODE_SESSION = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjEzMTcwNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjkwZDZhNWU1YWUxYjQyMmM1MmFjNmFmZWVhZmQwZGVmYmQ3NTQ2NGJiODJmZDYyZGEzMTgyNmFkMzI3ZDU3MTQiLCJzZXNzaW9uX3V1aWQiOiI2MjJjYzlmNCIsImlkIjoyMTMxNzA0LCJlbWFpbCI6ImJ1dGlyZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhbGV4ZXlfd2lzaCIsInVzZXJfc2x1ZyI6ImFsZXhleV93aXNoIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2FsZXhleV93aXNoL2F2YXRhcl8xNjMzMDkwMTE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3NDYzOTY1NCwiaXAiOiIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiLCJpZGVudGl0eSI6IjAyMzc5OTUzYjkzY2QyMjMyNDNkYjA5ZjFkZDRlNWI5IiwiZGV2aWNlX3dpdGhfaXAiOlsiOGY5YTVmMjg1MGEwNTNmYzZiMzkxZjcyYzcyNDJhMjgiLCIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.7RTqTK3erFDe-vhBxdrtOyyC3zFCD8nF1oxTbC5cGiA';

async function main() {
  console.log('Testing submission details...\n');
  
  const credential = new Credential();
  await credential.init(LEETCODE_SESSION);
  const leetcode = new LeetCode(credential);
  
  // Get a submission ID
  const submissions = await leetcode.submissions({ limit: 1, offset: 0 });
  const subId = submissions[0]?.id;
  console.log('Submission ID:', subId);
  
  // Get submission details
  console.log('\nGetting submission details...');
  const details = await leetcode.submission(subId);
  console.log('Details:', JSON.stringify(details, null, 2));
}

main().catch(console.error);
