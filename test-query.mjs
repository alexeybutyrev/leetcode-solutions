#!/usr/bin/env node
// Test using leetcode-query library
import { LeetCode, Credential } from 'leetcode-query';
import fs from 'fs';

const LEETCODE_SESSION = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjEzMTcwNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjkwZDZhNWU1YWUxYjQyMmM1MmFjNmFmZWVhZmQwZGVmYmQ3NTQ2NGJiODJmZDYyZGEzMTgyNmFkMzI3ZDU3MTQiLCJzZXNzaW9uX3V1aWQiOiI2MjJjYzlmNCIsImlkIjoyMTMxNzA0LCJlbWFpbCI6ImJ1dGlyZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhbGV4ZXlfd2lzaCIsInVzZXJfc2x1ZyI6ImFsZXhleV93aXNoIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2FsZXhleV93aXNoL2F2YXRhcl8xNjMzMDkwMTE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3NDYzOTY1NCwiaXAiOiIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiLCJpZGVudGl0eSI6IjAyMzc5OTUzYjkzY2QyMjMyNDNkYjA5ZjFkZDRlNWI5IiwiZGV2aWNlX3dpdGhfaXAiOlsiOGY5YTVmMjg1MGEwNTNmYzZiMzkxZjcyYzcyNDJhMjgiLCIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.7RTqTK3erFDe-vhBxdrtOyyC3zFCD8nF1oxTbC5cGiA';

async function main() {
  console.log('Testing leetcode-query library...\n');
  
  const credential = new Credential();
  await credential.init(LEETCODE_SESSION);
  const leetcode = new LeetCode(credential);
  
  // Get user info
  const whoami = await leetcode.whoami();
  console.log('User:', whoami);
  
  // Get recent submissions
  console.log('\nTrying to get submissions...');
  const submissions = await leetcode.submissions({ limit: 5, offset: 0 });
  console.log('Submissions response:', JSON.stringify(submissions, null, 2));
  
  // Try to get submission details
  if (submissions?.submissions?.[0]?.id) {
    const subId = submissions.submissions[0].id;
    console.log(`\nTrying to get submission ${subId} details...`);
    try {
      const details = await leetcode.submission(subId);
      console.log('Submission details:', JSON.stringify(details, null, 2).slice(0, 2000));
    } catch (e) {
      console.log('Error getting submission details:', e.message);
    }
  }
}

main().catch(console.error);
