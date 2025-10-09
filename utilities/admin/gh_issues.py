import os
import re
import requests
from collections import defaultdict
from datetime import datetime

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

# Regex patterns for subissues
INLINE_REF = re.compile(r"#(\d+)")
URL_REF = re.compile(r"https?://github\.com/[^/]+/[^/]+/issues/(\d+)")
TASK_LIST_REF = re.compile(r"^\s*[-*+]\s*\[[ xX]\]\s*#(\d+)", re.MULTILINE)

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
    """Build mapping of parent -> sub-issues based on body references (inline, URL, task list)."""
    refs = defaultdict(list)
    titles = {}
    open_numbers = {i["number"] for i in issues}

    for issue in issues:
        number = issue["number"]
        titles[number] = issue.get("title", "(no title)")
        body = issue.get("body") or ""
        mentioned = set()
        mentioned.update(int(m) for m in INLINE_REF.findall(body))
        mentioned.update(int(m) for m in URL_REF.findall(body))
        mentioned.update(int(m) for m in TASK_LIST_REF.findall(body))
        refs[number] = sorted([m for m in mentioned if m in open_numbers and m != number])
    return refs, titles

# -----------------------------
# Render Markdown table
# -----------------------------
def render_markdown_table(refs, issues, titles):
    lines = ["| Issue | Title | Related I ssues | Author | Assignee | Date Updated |",
             "| --- | --- | --- | --- | --- | --- |"]

    sorted_issues = sorted(issues, key=lambda x: x.get("updated_at", x.get("created_at")), reverse=True)

    for i in sorted_issues:
        num = i["number"]
        title = titles[num]
        children = refs.get(num, [])
        child_str = ", ".join(f"[#{c}](https://github.com/{OWNER}/{REPO}/issues/{c}) ({titles.get(c,'unknown')})" for c in children) if children else ""
        author = i["user"]["login"] if i.get("user") else ""
        assignee = i["assignee"]["login"] if i.get("assignee") else ""
        updated = i.get("updated_at") or i.get("created_at")
        updated_fmt = updated.replace("T"," ").split("Z")[0] if updated else ""
        lines.append(f"| [#{num}](https://github.com/{OWNER}/{REPO}/issues/{num}) | {title} | {child_str} | {author} | {assignee} | {updated_fmt} |")
    return "\n".join(lines)

# -----------------------------
# Render HTML table
# -----------------------------
def render_html_table(refs, issues, titles):
    """Generate HTML with Bootstrap 5.3.2 and sortable columns."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MaterialX Open Issues</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<!-- Bootstrap Icons -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<style>
/* Header and row styling to emulate a table using Bootstrap grid */
.issues-container { border: 1px solid #dee2e6; border-radius: 4px; overflow: hidden; }
.issue-header { background: #f8f9fa; font-weight: 600; }
.issue-row { border-top: 1px solid #dee2e6; }
.issue-row:nth-child(odd) { background: #ffffff; }
.issue-row:nth-child(even) { background: #fefefe; }
.sort-icon { cursor: pointer; margin-left: 6px; font-size: 1.05em; vertical-align: middle; }
.sort-icon.active { color: #0d6efd; }
.hdr-label { display: inline-block; }
.col-truncate { max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
</style>
</head>
<body>
<div class="container mt-4">
<h2>MaterialX Open Issues</h2>
<div class="issues-container">
  <div id="issues-header" class="row gx-2 py-2 align-items-center issue-header">
    <div class="col"><span class="hdr-label">Issue #</span>
        <i class="bi bi-arrow-up-short sort-icon" title="Sort ascending" onclick="sortTable(0,'asc', this)"></i>
        <i class="bi bi-arrow-down-short sort-icon" title="Sort descending" onclick="sortTable(0,'desc', this)"></i>
    </div>
    <div class="col"><span class="hdr-label">Title</span>
        <i class="bi bi-arrow-up-short sort-icon" title="Sort ascending" onclick="sortTable(1,'asc', this)"></i>
        <i class="bi bi-arrow-down-short sort-icon" title="Sort descending" onclick="sortTable(1,'desc', this)"></i>
    </div>
    <div class="col"><span class="hdr-label">Sub-issues</span></div>
    <div class="col"><span class="hdr-label">Author</span>
        <i class="bi bi-arrow-up-short sort-icon" title="Sort ascending" onclick="sortTable(3,'asc', this)"></i>
        <i class="bi bi-arrow-down-short sort-icon" title="Sort descending" onclick="sortTable(3,'desc', this)"></i>
    </div>
    <div class="col"><span class="hdr-label">Assignee</span>
        <i class="bi bi-arrow-up-short sort-icon" title="Sort ascending" onclick="sortTable(4,'asc', this)"></i>
        <i class="bi bi-arrow-down-short sort-icon" title="Sort descending" onclick="sortTable(4,'desc', this)"></i>
    </div>
    <div class="col"><span class="hdr-label">Date Updated</span>
        <i class="bi bi-arrow-up-short sort-icon" title="Sort ascending" onclick="sortTable(5,'asc', this)"></i>
        <i class="bi bi-arrow-down-short sort-icon" title="Sort descending" onclick="sortTable(5,'desc', this)"></i>
    </div>
  </div>
  <div id="issues-body">
"""

    sorted_issues = sorted(issues, key=lambda x: x.get("updated_at", x.get("created_at")), reverse=True)

    for i in sorted_issues:
        num = i["number"]
        title = titles[num]
        children = refs.get(num, [])
        child_str = ", ".join(f"<a href='https://github.com/{OWNER}/{REPO}/issues/{c}'>#{c}</a> ({titles.get(c,'unknown')})" for c in children) if children else ""
        author = i["user"]["login"] if i.get("user") else ""
        assignee = i["assignee"]["login"] if i.get("assignee") else ""
        updated = i.get("updated_at") or i.get("created_at")
        updated_fmt = updated.replace("T"," ").split("Z")[0] if updated else ""
        # Build a responsive row using Bootstrap columns
        html += f"<div class='row issue-row align-items-center py-2'>"
        html += f"<div class='col'><a href='https://github.com/{OWNER}/{REPO}/issues/{num}'>#{num}</a></div>"
        html += f"<div class='col'>{title}</div>"
        html += f"<div class='col'>{child_str}</div>"
        html += f"<div class='col'>{author}</div>"
        html += f"<div class='col'>{assignee}</div>"
        html += f"<div class='col'>{updated_fmt}</div>"
        html += "</div>\n"

    html += """
  </div>
</div>
</div>
<script>
function sortTable(n, dir, el) {
    // n: column index, dir: 'asc' or 'desc', el: clicked icon element
    const container = document.getElementById('issues-body');
    const rows = Array.from(container.querySelectorAll('.issue-row'));
    const asc = (dir === 'asc');

    const collator = new Intl.Collator(undefined, {numeric: true, sensitivity: 'base'});

    rows.sort((a, b) => {
        let x = (a.children[n] && a.children[n].innerText) ? a.children[n].innerText.trim() : '';
        let y = (b.children[n] && b.children[n].innerText) ? b.children[n].innerText.trim() : '';

        if (n === 0) {
            const xi = parseInt(x.replace(/\D/g,'')) || 0;
            const yi = parseInt(y.replace(/\D/g,'')) || 0;
            return (xi - yi) * (asc ? 1 : -1);
        }
        if (n === 5) {
            const xd = Date.parse(x) || 0;
            const yd = Date.parse(y) || 0;
            return (xd - yd) * (asc ? 1 : -1);
        }

        return (collator.compare(x, y)) * (asc ? 1 : -1);
    });

    // Re-attach in sorted order
    rows.forEach(r => container.appendChild(r));

    // Update sort state attributes on header container
    const header = document.getElementById('issues-header');
    header.setAttribute('data-sort-col', n);
    header.setAttribute('data-sort-dir', asc ? 'asc' : 'desc');

    // Highlight active icon for the column
    try {
        const th = header.children[n];
        // remove active from this header only
        Array.from(header.querySelectorAll('.sort-icon')).forEach(ic => ic.classList.remove('active'));
        if (el) {
            el.classList.add('active');
        } else {
            const icon = th.querySelector(dir === 'asc' ? '.bi-arrow-up-short' : '.bi-arrow-down-short');
            if (icon) icon.classList.add('active');
        }
    } catch (e) {
        // ignore
    }
}
</script>
</body>
</html>
"""
    return html

# -----------------------------
# Main
# -----------------------------
def main():
    print("Fetching open issues...")
    issues = fetch_issues()
    print(f"Fetched {len(issues)} open issues.")

    refs, titles = build_hierarchy(issues)

    # Markdown output
    md_table = render_markdown_table(refs, issues, titles)
    md_file = "MaterialX_Open_Issue_Subissues.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_table)
    print(f"Markdown table written to {md_file}")

    # HTML output
    html_table = render_html_table(refs, issues, titles)
    html_file = "MaterialX_Open_Issue_Subissues.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_table)
    print(f"HTML table written to {html_file}")

if __name__ == "__main__":
    main()
