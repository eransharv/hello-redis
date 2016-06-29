import redis

print("connecting to redis labs cloud...")	

pool = redis.ConnectionPool(host='pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', port=13628,password='rs87362c')
r = redis.Redis(connection_pool=pool)

##r = redis.StrictRedis(host='pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', port=13628,password='rs87362c')

print("set test key...")
r.set('eran', 'bar')
r.get('foo')
print("done.")
