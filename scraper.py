#!/usr/bin/env python3
"""LeetCode Solutions Scraper - Fetches all accepted submissions from LeetCode."""

import urllib.request
import urllib.error
import json
import os
import time
from pathlib import Path

LEETCODE_SESSION = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjEzMTcwNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjkwZDZhNWU1YWUxYjQyMmM1MmFjNmFmZWVhZmQwZGVmYmQ3NTQ2NGJiODJmZDYyZGEzMTgyNmFkMzI3ZDU3MTQiLCJzZXNzaW9uX3V1aWQiOiI2MjJjYzlmNCIsImlkIjoyMTMxNzA0LCJlbWFpbCI6ImJ1dGlyZXZAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhbGV4ZXlfd2lzaCIsInVzZXJfc2x1ZyI6ImFsZXhleV93aXNoIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2FsZXhleV93aXNoL2F2YXRhcl8xNjMzMDkwMTE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3NDYzOTY1NCwiaXAiOiIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiLCJpZGVudGl0eSI6IjAyMzc5OTUzYjkzY2QyMjMyNDNkYjA5ZjFkZDRlNWI5IiwiZGV2aWNlX3dpdGhfaXAiOlsiOGY5YTVmMjg1MGEwNTNmYzZiMzkxZjcyYzcyNDJhMjgiLCIyNjAwOjQwNDA6YTY0Zjo2YTAwOjMxMjg6ZDU3MTpkMzA2OjJhN2UiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.7RTqTK3erFDe-vhBxdrtOyyC3zFCD8nF1oxTbC5cGiA'

BASE_URL = "https://leetcode.com"
GRAPHQL_URL = f"{BASE_URL}/graphql"

def graphql_request(query, variables=None):
    """Make a GraphQL request to LeetCode."""
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(GRAPHQL_URL, data=data, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
        raise

def get_user_info():
    """Get current user info."""
    query = """
    query getUserStatus {
        userStatus {
            username
            isSignedIn
        }
    }
    """
    return graphql_request(query)

def get_all_submissions(username, limit=100):
    """Get all submissions with pagination."""
    all_submissions = []
    offset = 0
    
    while True:
        query = """
        query getSubmissions($username: String!, $limit: Int!, $offset: Int!) {
            submissionList(username: $username, limit: $limit, offset: $offset) {
                total
                hasNext
                submissions {
                    id
                    title
                    titleSlug
                    statusDisplay
                    lang
                    timestamp
                    url
                    runtime
                    memory
                }
            }
        }
        """
        variables = {"username": username, "limit": limit, "offset": offset}
        result = graphql_request(query, variables)
        
        data = result.get("data", {}).get("submissionList", {})
        submissions = data.get("submissions", [])
        total = data.get("total", 0)
        has_next = data.get("hasNext", False)
        
        # Filter only accepted submissions
        accepted = [s for s in submissions if s["statusDisplay"] == "Accepted"]
        all_submissions.extend(accepted)
        
        print(f"Fetched {len(submissions)} submissions (offset {offset}/{total}), {len(accepted)} accepted")
        
        if not has_next:
            break
        
        offset += limit
        time.sleep(0.5)  # Rate limiting
    
    return all_submissions

def get_submission_code(submission_id):
    """Get the actual code for a submission."""
    query = """
    query getSubmissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            runtime
            memory
            lang
        }
    }
    """
    variables = {"submissionId": int(submission_id)}
    result = graphql_request(query, variables)
    return result.get("data", {}).get("submissionDetails", {})

def get_problem_info(title_slug):
    """Get problem difficulty and tags."""
    query = """
    query getProblem($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            difficulty
            topicTags {
                name
            }
        }
    }
    """
    variables = {"titleSlug": title_slug}
    result = graphql_request(query, variables)
    return result.get("data", {}).get("question", {})

def lang_to_extension(lang):
    """Map LeetCode language to file extension."""
    mapping = {
        "python": "py",
        "python3": "py",
        "java": "java",
        "javascript": "js",
        "typescript": "ts",
        "cpp": "cpp",
        "c": "c",
        "csharp": "cs",
        "go": "go",
        "rust": "rs",
        "ruby": "rb",
        "swift": "swift",
        "kotlin": "kt",
        "scala": "scala",
        "php": "php",
        "mysql": "sql",
        "mssql": "sql",
        "oracle": "sql",
        "bash": "sh",
        "racket": "rkt",
        "elixir": "ex",
        "dart": "dart",
    }
    return mapping.get(lang.lower(), lang.lower())

def sanitize_filename(name):
    """Sanitize a string for use in filename."""
    return "".join(c if c.isalnum() or c in " -_" else "_" for c in name)

def main():
    print("=== LeetCode Solutions Scraper ===\n")
    
    # Get user info
    print("Checking authentication...")
    user_info = get_user_info()
    username = user_info.get("data", {}).get("userStatus", {}).get("username")
    if not username:
        print("ERROR: Not authenticated. Check your LEETCODE_SESSION.")
        return
    
    print(f"Authenticated as: {username}\n")
    
    # Get all submissions
    print("Fetching all submissions...")
    submissions = get_all_submissions(username)
    print(f"\nTotal accepted submissions: {len(submissions)}")
    
    # Group by problem (keep best submission per language per problem)
    problems = {}
    for sub in submissions:
        key = (sub["titleSlug"], sub["lang"])
        if key not in problems:
            problems[key] = sub
        else:
            # Keep the one with better runtime
            existing = problems[key]
            if sub.get("runtime") and existing.get("runtime"):
                try:
                    curr_runtime = float(sub["runtime"].replace("ms", ""))
                    existing_runtime = float(existing["runtime"].replace("ms", ""))
                    if curr_runtime < existing_runtime:
                        problems[key] = sub
                except:
                    pass
    
    print(f"Unique problem+language combinations: {len(problems)}\n")
    
    # Create output directory
    output_dir = Path("solutions")
    output_dir.mkdir(exist_ok=True)
    
    # Fetch code and save
    problem_cache = {}
    saved_count = 0
    
    for (title_slug, lang), sub in problems.items():
        try:
            # Get problem info if not cached
            if title_slug not in problem_cache:
                problem_cache[title_slug] = get_problem_info(title_slug)
            
            problem_info = problem_cache[title_slug]
            difficulty = problem_info.get("difficulty", "Unknown")
            
            # Get submission code
            details = get_submission_code(sub["id"])
            code = details.get("code", "")
            
            if not code:
                print(f"Skipping {sub['title']} - no code found")
                continue
            
            # Create problem directory
            title_sanitized = sanitize_filename(sub["title"])
            problem_dir = output_dir / title_sanitized
            problem_dir.mkdir(exist_ok=True)
            
            # Save solution file
            ext = lang_to_extension(lang)
            filename = f"solution.{ext}"
            filepath = problem_dir / filename
            
            # Add header comment
            header = f"// Problem: {sub['title']}\n// Difficulty: {difficulty}\n// Language: {lang}\n// Runtime: {sub.get('runtime', 'N/A')}\n// Memory: {sub.get('memory', 'N/A')}\n\n"
            
            # Adjust comment style for language
            if ext in ["py", "rb", "sh", "ex"]:
                header = header.replace("//", "#")
            elif ext in ["sql"]:
                header = header.replace("//", "--")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(header + code)
            
            saved_count += 1
            print(f"Saved: {sub['title']} ({lang})")
            
            time.sleep(0.3)  # Rate limiting
            
        except Exception as e:
            print(f"Error saving {sub['title']}: {e}")
    
    print(f"\n=== Complete! Saved {saved_count} solutions ===")
    
    # Create README
    readme = f"""# LeetCode Solutions

My LeetCode solutions scraped automatically.

## Stats

- Total solutions: {saved_count}
- Problems solved: {len(set(p[0] for p in problems.keys()))}

## Structure

```
solutions/
├── problem-name/
│   └── solution.{ext}
```

## Languages Used

"""
    
    langs = sorted(set(lang for _, lang in problems.keys()))
    for lang in langs:
        readme += f"- {lang}\n"
    
    with open("README.md", "w") as f:
        f.write(readme)
    
    print("Created README.md")

if __name__ == "__main__":
    main()
