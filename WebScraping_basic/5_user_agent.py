import requests
res = requests.get("http://andocoding.tistory.com")
# res.raise_for_status()

with open("coding.html", "w", encoding="utf8") ddas f:
    f.write(res.text)