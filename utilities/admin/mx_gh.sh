#!/bin/bash

REPO="AcademySoftwareFoundation/MaterialX"

echo ""
echo "=== PRs where you're @mentioned ==="
gh pr list -R "$REPO" --search "mention:@me" --state open

echo ""
echo "=== PRs assigned to you ==="
gh pr list -R "$REPO" --search "assignee:@me" --state open --json url --template '{{range .}}{{.url}}{{"\n"}}{{end}}'

echo ""
echo "=== PRs requesting your review ==="
#gh pr list -R "$REPO" --search "review-requested:@me" --state open
gh pr list -R AcademySoftwareFoundation/MaterialX --search "review-requested:@me" --state open --json url --template '{{range .}}{{.url}}{{"\n"}}{{end}}'

echo ""
echo "=== PRs where I'm the author ==="
gh pr list -R "$REPO" --search "author:@me" --state open --json url --template '{{range .}}{{.url}}{{"\n"}}{{end}}'
