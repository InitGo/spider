import json

jsonstring ='{"user_man":[{"name":"Peter"},{"name":"xiaoming"}],'\
            '"user_woman":[{"name":"Anni"},{"name":"zqw"}]}'

json_data = json.loads(jsonstring)

print(json_data.get("user_man"))

print(json_data.get("user_woman"))

print(json_data.get("user_man")[0].get("name"))