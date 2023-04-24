import requests
api = 'https://api.gap.im/sendMessage'
headers = {'token' : '912842e69c5cfa42f5231f88b76c4b3982a33d3cd79d9ad49d64a38e18ad9e6d'}
pyload = {
    'chat_id' : '+989143607299',
    'type' : 'text',
    'data' : 'سلام من رباتم',

}
x = requests.post(api,data=pyload,headers=headers)
print(x.text)
# donnnnnne gg