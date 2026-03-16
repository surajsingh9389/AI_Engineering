# 1. list - ordered, mutable, indexed, allow duplicates
#    tuple - ordered, imutable, indexed, allow duplicates
#    set - unordered, mutable, unindexed, don't allow duplicates
   
# 2. we use dictionary for same purpose - 
#    dic = {'a': 1}

# 3.
# def top_repo(repos):
#     if not repos: return None 
    
#     return max(repos, key=lambda  r: r["stars"])
    
#     # max_star_repo = repos[0]
    
#     # for repo in repos:
#     #     curr_repo_stars = repo["stars"]
#     #     max_star_repo_stars = max_star_repo["stars"]
        
#     #     if curr_repo_stars > max_star_repo_stars:
#     #         max_star_repo = repo
            
#     # return max_star_repo
        
        
# repos = [
#  {"name":"repo1","stars":100},
#  {"name":"repo2","stars":500},
#  {"name":"repo3","stars":300}
# ]

# print(top_repo(repos))


# 4. for clean architecture, separate the files based on services. instead of writing the whole code in main.py we separate the logic into file and then import this module use there functions

# 5. after create the venv for our local python project then activate the venv. we need library and packages to perform some task so we use pip install command to intall specific libary now the main thing we use pip freeze > requirements.text to sotre the information of our packages and there version if we did not use this it project does not know what package and library we use and what the version was is also help to install other repo library and package with there version which they use.