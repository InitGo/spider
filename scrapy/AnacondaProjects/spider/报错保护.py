

try:
    print(html.text)
except ConnectionError:
    print('拒绝连接')