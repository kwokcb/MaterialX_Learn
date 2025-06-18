#!/bin/bash

REPO="AcademySoftwareFoundation/MaterialX"

format_date() {
  # Input ISO8601 UTC date (e.g. 2025-05-30T15:52:07Z)
  # Output: YYYY-MM-DD HH:MM
  date -d "$1" +"%Y-%m-%d %H:%M"
}

print_prs() {
  local filter_desc="$1"
  local search_filter="$2"

  echo ""
  echo "## $filter_desc"
  echo ""
  echo "| Title | Branch | Created At | Updated At | URL |"
  echo "|-------|--------|------------|-----|-----|"

  # Get raw JSON output with createdAt, then process line by line
 gh pr list -R "$REPO" --search "$search_filter" --state open \
    --json title,headRefName,createdAt,updatedAt,url \
    --template '{{range .}}{{.title}}|{{.headRefName}}|{{.createdAt}}|{{.updatedAt}}|{{.url}}{{"\n"}}{{end}}' |
    while IFS='|' read -r title branch createdAt updatedAt url; do
      createdFormatted=$(format_date "$createdAt")
      updatedFormatted=$(format_date "$updatedAt")
      echo "| $title | $branch | $createdFormatted | $updatedFormatted | [Link]($url) |"
    done
}

print_prs "PRs requesting your review" "review-requested:@me"

print_prs "PRs authored by you" "author:@me"

#print_prs "PRs assigned to you" "assignee:@me"

print_prs "PRs mention you" "mention:@me"

echo ""
echo "## All Open PRs"
echo ""
echo "| Title | Branch | Created At | Updated At | URL |"
echo "|-------|--------|------------|------------|-----|"

gh pr list -R "$REPO" --state open \
  --json title,headRefName,createdAt,updatedAt,url \
  --template '{{range .}}{{.title}}|{{.headRefName}}|{{.createdAt}}|{{.updatedAt}}|{{.url}}{{"\n"}}{{end}}' |
  while IFS='|' read -r title branch createdAt updatedAt url; do
    createdFormatted=$(format_date "$createdAt")
    updatedFormatted=$(format_date "$updatedAt")
    echo "| $title | $branch | $createdFormatted | $updatedFormatted | [Link]($url) |"
  done