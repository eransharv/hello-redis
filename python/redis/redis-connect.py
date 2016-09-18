import redis

print("\nconnecting to redis labs cloud...")	

pool = redis.ConnectionPool(host='pub-redis-11458.us-east-mz.1.ec2.garantiadata.com', 
	port=11458, password='rs87362c',
	max_connections=1)
r = redis.Redis(connection_pool=pool)

''' without connection pooling:
r = redis.StrictRedis(host='pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', port=13628,password='rs87362c')
'''

'''with SSL:
r = redis.Redis( url='rediss://:password@hostname:port/0',
    password='password',
    ssl_keyfile='path_to_keyfile/garantia_user_private.key',
    ssl_certfile='path_to_certfile/garantia_user.crt',
    ssl_cert_reqs='required',
    ssl_ca_certs='path_to_ca_certfile/garantia_ca.pem')
'''

print("\nset test key...")
print("\n>r.set(`foo`, `bar`)")
r.set('eran', 'bar')

print("\nget test key...")
print("\n>r.get(`foo`)")
print(">foo=" + r.get('foo'))

print("\ndone.")
