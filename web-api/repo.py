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