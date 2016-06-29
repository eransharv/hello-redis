import redis

print("\nconnecting to redis labs cloud...")	

pool = redis.ConnectionPool(host='pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', port=13628,password='rs87362c')
r = redis.Redis(connection_pool=pool)

''' without connection pooling:
r = redis.StrictRedis(host='pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', port=13628,password='rs87362c')
'''

print("\nset test key...")
print("\n>r.set(`foo`, `bar`)")
r.set('eran', 'bar')

print("\nget test key...")
print("\n>r.get(`foo`)")
print(">foo=" + r.get('foo'))

print("\ndone.")
