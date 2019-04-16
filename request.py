from requests import get

ret = get("http://10.0.10.1:12345/student")
print(ret.json())

