p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
t=t.replace(
    'data = json.dumps({"client_id":cid,"client_secret":cs,"grant_type":"authorization_code","code":auth_code}).encode()',
    'data = urllib.parse.urlencode({"client_id":cid,"client_secret":cs,"grant_type":"authorization_code","code":auth_code}).encode()'
)
t=t.replace(
    'headers={"Content-Type":"application/json"}',
    'headers={"Content-Type":"application/x-www-form-urlencoded"}'
)
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Fix OK')
