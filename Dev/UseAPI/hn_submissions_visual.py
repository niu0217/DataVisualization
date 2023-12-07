from operator import itemgetter
import plotly.express as px

import requests

# 执行API调用并存储响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
title_dicts, comment_dicts, comment_links = [], [], []
for submission_id in submission_ids[:5]:
    # 对于每篇文章，都执行一个API调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus code: {r.status_code}")
    response_dict = r.json()

    # 对于每篇文章，都创建一个字典
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    comment_dicts.append(submission_dict['comments'])

    comment_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    comment_links.append(comment_link)

# 可视化
title = "Most-Stars in hacker-news"
labels = {'x': 'caption', 'y': 'Comment'}
fig = px.bar(
    x=comment_links, y=comment_dicts, title=title, labels=labels)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
