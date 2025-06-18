import requests
import os
import argparse

def get_reviews(pr, token, repo, username):
    pr_number = pr['number']
    pr_title = pr['title']
    pr_url = pr['html_url']

    headers = {
        'Authorization': f'{token}'
    }

    reviews_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/reviews"
    reviews_resp = requests.get(reviews_url, headers=headers)
    if reviews_resp.status_code != 200:
        print(f"-  Could not fetch reviews for PR #{pr_number}")

    reviews = reviews_resp.json()
    reviewed = any(review['user']['login'].lower() == username.lower() for review in reviews)

    if reviewed:
        print(f"- Reviewing: PR #{pr_number}: {pr_title}")
        print(f"   {pr_url}")    

def perform_search(token, args):

    user = args.user
    repo = args.repo    
    request_type = args.type
    search_type = args.search_type.lower()
    maximum = args.max

    headers = {
        'Authorization': f'{token}',
        "Accept": "application/vnd.github+json"
    }
    params = {
    }
    if request_type == 'author':
        # Search for PRs that are assigned to the user
        params['q'] = f'author:{user}'
    elif request_type == 'mentioned':
        # Search for PRs that mentions the user
        params['q'] = f'mentions:{user}'
    elif request_type == 'review':
        # Search for PRs that are assigned to the user for review
        params['q'] = f'review-requested:{user}'
    elif request_type == 'all':
        # Search for all PRs that are assigned to the user
        params['q'] = ''        

    # Add search ype and repo to the query.
    params['q'] += f' is:{search_type} repo:{repo} is:open'

    # Set number of results to {maximum}
    params['per_page'] = maximum
    # Set page to 1
    params['page'] = 1

    response = requests.get('https://api.github.com/search/issues', headers=headers, params=params)

    prs = response.json().get('items', [])
    return prs

def main():
    # Get arguments for user and repo. Set defaults to kwokcb and AcademySoftwareFoundation/MaterialX
    parser = argparse.ArgumentParser(description='Search for open PRs assigned to a user in a specific GitHub repository.')
    parser.add_argument('--user', type=str, default='kwokcb', help='GitHub username to search for review requests.')
    parser.add_argument('--repo', type=str, default='AcademySoftwareFoundation/MaterialX', help='GitHub repository to search in.')
    # Add arguments for type of query, default to review. Options include review, author, all, and mentioned
    parser.add_argument('--type', type=str, default='review', choices=['review', 'author', 'all', 'mentioned'],
                        help='Type of query to perform. Default is review.')
    # Add argument for Markdown output. 
    parser.add_argument('--markdown', action='store_true', help='Output in Markdown format.')
    # Add search type argument. Default is pr
    parser.add_argument('--search_type', type=str, default='pr', choices=['PR', 'issue'],
                        help='Type of search to perform. Default is pr.')
    # Add results count. Default max to 50
    parser.add_argument('--max', type=int, default=50, help='Maximum number of results to return. Default is 50.')
    # Add option to get the user branch for each PR
    parser.add_argument('--get_user_branch', action='store_true', help='Get the user branch for each PR.')

    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN environment variable is not set. Please set it to your GitHub token.")

    args = parser.parse_args()
    prs = perform_search(GITHUB_TOKEN, args)

    user = args.user
    repo = args.repo    
    request_type = args.type
    search_type = args.search_type.lower()    

    # Save prs to file    
    with open('open_prs.json', 'w') as f:
        import json
        json.dump(prs, f, indent=4)

    if args.markdown:
        # Print in Markdown format
        title = f"## Github Query"
        print(title)
        print(f"- User: {user}")
        print(f"- Repository: {repo}")
        detail = f"- {len(prs)} {search_type} items found. Query type: {request_type}"
        print(detail + "\n")

        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

        if len(prs) > 0:
            branch_title = ''
            branch_title_separator = ''
            if args.get_user_branch:
                branch_title = 'Branch |'
                branch_title_separator = '--- |'
            table_header = f"| Title | Link | {branch_title} Created By | Created At |\n| --- | --- | {branch_title_separator} --- | --- |"
            print(table_header)
            for pr in prs:
                formatted_date = pr['created_at'].split('T')
                formatted_date = f"{formatted_date[0]} {formatted_date[1][:5]}"

                branch = ""
                if args.get_user_branch:
                    # This can be very slow...
                    pr_number = pr['number']
                    pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"                
                    pr_detail_resp = requests.get(pr_url, headers=headers)
                    pr_full = pr_detail_resp.json()
                    if 'head' in pr_full and 'ref' in pr_full['head']:
                        branch = pr_full['head']['ref'] + " |"
                print(f"| {pr['title']} | [{pr['number']}]({pr['html_url']}) | {branch} {pr['user']['login']} | {formatted_date} |")
    
                #get_reviews(pr, GITHUB_TOKEN, repo, user)

    else:
        title = f"Open PRs for {user} in {repo}" + f" ({len(prs)} found. Query type: {request_type}"
        print(title)
        if len(prs) > 0:
            for pr in prs:
                formatted_date = pr['created_at'].split('T')
                formatted_date = f"{formatted_date[0]} {formatted_date[1][:5]}"
                print(f"- \"{pr['title']}\" : {pr['html_url']}. Created by {pr['user']['login']} on {formatted_date}.")

                #get_reviews(pr, GITHUB_TOKEN, repo, user)


if __name__ == '__main__':
    main()