import os
import re
import requests
from collections import defaultdict

# -----------------------------
# Configuration
# -----------------------------
OWNER = "AcademySoftwareFoundation"
REPO = "MaterialX"
GITHUB_API = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set. Please export or set it first.")

HEADERS = {
    "Authorization": f"{TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Regex to match issue references: #123 or full GitHub URL
ISSUE_REF = re.compile(r"(?:#(\d+)|https?://github\.com/[^/]+/[^/]+/issues/(\d+))")

# -----------------------------
# Fetch issues
# -----------------------------
def fetch_issues():
    """Fetch all open issues from GitHub (exclude PRs)."""
    issues = []
    page = 1
    while True:
        url = f"{GITHUB_API}?state=open&per_page=100&page={page}"
        print(f"Fetching page {page}...")
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            raise Exception(f"Failed to fetch issues: {r.status_code} — {r.text}")
        data = r.json()
        if not data:
            break
        # Exclude pull requests
        issues.extend([i for i in data if "pull_request" not in i])
        page += 1
    return issues

# -----------------------------
# Build sub-issue mapping
# -----------------------------
def build_hierarchy(issues):
    """Build mapping of parent -> sub-issues based on body references."""
    refs = defaultdict(list)
    titles = {}
    open_numbers = {i["number"] for i in issues}

    for issue in issues:
        number = issue["number"]
        titles[number] = issue.get("title", "(no title)")
        body = issue.get("body") or ""
        mentioned = ISSUE_REF.findall(body)
        for m in mentioned:
            ref_num = int(m[0] or m[1])
            if ref_num in open_numbers and ref_num != number:
                refs[number].append(ref_num)
        refs[number] = sorted(set(refs.get(number, [])))
    return refs, titles

# -----------------------------
# Render Markdown table
# -----------------------------
def render_markdown_table(refs, issues, titles):
    """Create a Markdown table with clickable links, author, and assignee."""
    lines = ["| Issue # | Title | Sub-issues | Author | Assignee |",
             "| --- | --- | --- | --- | --- |"]

    # Map issue number -> author & assignee
    issue_meta = {}
    for i in issues:
        issue_num = i["number"]
        author = i["user"]["login"] if i.get("user") else ""
        assignee = i["assignee"]["login"] if i.get("assignee") else ""
        issue_meta[issue_num] = (author, assignee)

    for num in sorted(titles.keys()):
        title = titles[num]
        children = refs.get(num, [])
        if children:
            child_str = ", ".join(f"[#{c}](https://github.com/{OWNER}/{REPO}/issues/{c}) ({titles.get(c,'unknown')})" for c in children)
        else:
            child_str = ""
        author, assignee = issue_meta.get(num, ("",""))
        lines.append(f"| [#{num}](https://github.com/{OWNER}/{REPO}/issues/{num}) | {title} | {child_str} | {author} | {assignee} |")
    return "\n".join(lines)

# -----------------------------
# Main
# -----------------------------
def main():
    print("Fetching open issues...")
    issues = fetch_issues()
    print(f"Fetched {len(issues)} open issues.")

    refs, titles = build_hierarchy(issues)
    md_table = render_markdown_table(refs, issues, titles)

    out_file = "MaterialX_Open_Issue_Subissues.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(md_table)
    print(f"Markdown table written to {out_file}")

if __name__ == "__main__":
    main()
