from memclient import MemClient

print("\nconnecting to redis labs memcached cloud...")	

# create a new client
client = MemClient()
client.connect('pub-memcache-17991.us-east-1-1.2.ec2.garantiadata.com', 17991)

print("\nset test key...")
print("\n>r.set(`foo`, `bar`)")
client.set('foo', 'bar', noreply=False)

print("\nget test key...")
print("\n>r.get(`foo`)")
print client.get('foo')

client.quit()
print("\ndone.")




