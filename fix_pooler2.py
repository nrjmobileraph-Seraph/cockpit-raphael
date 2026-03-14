p='C:/Users/BoulePiou/cockpit-raphael/db_wrapper.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
t=t.replace('aws-0-eu-west-1.pooler.supabase.com','aws-1-eu-west-1.pooler.supabase.com')
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Pooler corrige aws-1')
