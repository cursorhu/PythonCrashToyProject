import requests

#API的url
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
#header指定使用github-V3版本的API
headers = {'Accept':'application/vnd.github.v3+json'}
#发送get请求，返回response
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
#json方法将返回的json格式数据转化为字典变量(key-value)以便解析
resp_json = r.json()
print(resp_json.keys())
print(f"total_count: {resp_json['total_count']}")
#列出top-10 repos
for i in range(1, 11):
    #key-value嵌套访问的方式和访问多维数组形式类似
    repo = resp_json['items'][i]
    print(f"### top{i} stared python repo:")
    print(f"name: {repo['name']}")
    print(f"owner: {repo['owner']['login']}") #owner必定不为空
    print(f"description: {repo['description']}")
    print(f"repository: {repo['html_url']}")
    print(f"stars: {repo['stargazers_count']}")
    print(f"forks: {repo['forks']}")
    #print(f"license: {repo['license']['name']}") #license可能为空，此时访问name字段报错
