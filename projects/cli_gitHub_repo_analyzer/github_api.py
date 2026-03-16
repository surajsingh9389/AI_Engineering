import requests

def get_repo_data(repo_name):
    URL = f"https://api.github.com/repos/{repo_name}"
    
    response = requests.get(URL)
    
    if response.status_code != 200:
       return {"stars": 0, "issues": 0}
    
    data = response.json()
    
    stars = data["stargazers_count"]
    open_issues = data["open_issues"]
    
    return {"stars": stars, "issues": open_issues}
        
