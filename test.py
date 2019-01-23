import requests
res = requests.post('http://127.0.0.1:5000/documents/Test+1', json={"content":"lalala"})
if res.ok:
    print res.json()
