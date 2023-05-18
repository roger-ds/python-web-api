import httpx

result = httpx.get("http://exemple.com/index.html")

print(result.status_code)
print(result.headers)
print(result.content)
