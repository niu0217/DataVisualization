import requests

# 执行API调用的网址
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# 要求Github API的版本为v3，并且返回JSON格式的结果
headers = {"Accept": "application/vnd.github.v3+json"}
# 使用requests调用API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转换为字典
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nSelected information about first repository: ")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
