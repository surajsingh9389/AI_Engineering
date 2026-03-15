# class RepositoryAnalyzer:
#     def __init__(self, repo_name, stars, issues):
#         self.repo_name = repo_name
#         self.stars = stars
#         self.issues = issues

#     def summary(self):
#         return f"Repo: {self.repo_name} | Stars: {self.stars} | Issues: {self.issue}"
    

# repo = RepositoryAnalyzer("ai-roadmap", 1200, 45)

# print(repo.summary())


from github_api import get_repo_data
from formatter import format_repo

repo_name = "ai-repo"
data = get_repo_data(repo_name)

stars = data["stars"]
issues = data["issues"]

print(format_repo(repo_name, stars, issues))

