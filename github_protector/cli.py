import os
import subprocess
import requests
import argparse
from pathlib import Path
from dotenv import load_dotenv

def get_git_remote_info():
    """Extract owner and repo name from git remote origin URL."""
    try:
        url = subprocess.check_output(["git", "remote", "get-url", "origin"], stderr=subprocess.STDOUT).decode("utf-8").strip()
        if url.endswith(".git"):
            url = url[:-4]
        
        if url.startswith("git@"):
            path = url.split(":")[-1]
        else:
            # Handle https://github.com/owner/repo
            path = "/".join(url.split("/")[-2:])
            
        parts = path.split("/")
        if len(parts) >= 2:
            return parts[-2], parts[-1]
    except Exception:
        pass
    return None, None

def get_git_username():
    """Get the current git user name."""
    try:
        return subprocess.check_output(["git", "config", "user.name"], stderr=subprocess.STDOUT).decode("utf-8").strip()
    except Exception:
        return None

def main():
    # Load .env from current working directory
    load_dotenv(dotenv_path=Path(".") / ".env")

    parser = argparse.ArgumentParser(description="Protect a GitHub branch via the API.")
    parser.add_argument("--token", help="GitHub Admin Token (defaults to ADMIN_TOKEN in .env)")
    parser.add_argument("--username", help="GitHub username/owner (defaults to git remote owner or git config user.name)")
    parser.add_argument("--repo", help="GitHub repository name (defaults to git remote repo name)")
    parser.add_argument("--branch", default="main", help="Branch to protect (default: main)")

    args = parser.parse_args()

    # Priority logic for inputs
    remote_owner, remote_repo = get_git_remote_info()
    
    token = args.token or os.getenv("ADMIN_TOKEN")
    owner = args.username or remote_owner or get_git_username()
    repo = args.repo or remote_repo

    if not token:
        print("Error: GitHub Admin Token is required. Use --token or set ADMIN_TOKEN in .env")
        return
    if not owner:
        print("Error: GitHub username/owner is required. Use --username or ensure git is configured.")
        return
    if not repo:
        print("Error: GitHub repository name is required. Use --repo or run inside a git repository.")
        return

    print(f"🚀 Protecting branch '{args.branch}' for {owner}/{repo}...")

    url = f"https://api.github.com/repos/{owner}/{repo}/branches/{args.branch}/protection"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 1
        },
        "restrictions": None
    }
    
    try:
        response = requests.put(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print(f"✅ Success: Branch '{args.branch}' is now protected.")
            print("Settings applied: PR required, 1 approval required, Enforce for admins.")
        else:
            print(f"❌ Failed with status code {response.status_code}:")
            try:
                print(response.json())
            except:
                print(response.text)
            
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
