import requests
#python -m pip install plotly 
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
resp_json = r.json()

#解析item列表中的每个key-value并保存到两个列表names和stars
items = resp_json['items']
repo_names, repo_stars = [], []
for repo in items:
    repo_names.append(repo['name'])
    repo_stars.append(repo['stargazers_count'])

#显示数据的格式：条形图，x为name, y为stars   
data = [
    {
        'type': 'bar',
        'x': repo_names,
        'y': repo_stars,
    }
]

#横纵坐标的格式
layout = {
    'title': 'Github Top-stared Python repos',
    'xaxis': {'title': 'repository'},
    'yaxis': {'title': 'stars'},
}

#绘图：把data绘制到layout中，生成html
figure = {'data': data, 'layout': layout}
offline.plot(figure, filename='repo_visual.html')