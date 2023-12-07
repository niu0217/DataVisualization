import requests
import plotly.express as px

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
repo_links, stars, hover_texts = [], [], []
print(f"Repositories returned: {len(repo_dicts)}")
for repo_dict in repo_dicts:
    # 将仓库名字转换为链接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(
    x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
