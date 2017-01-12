require 'dalli' #Ruby client for accessing memcached servers


options = { :username => 'eran', :password => 'rs87362c' }
dc = Dalli::Client.new('pub-memcache-11977.us-east-1-1.2.ec2.garantiadata.com:11977', options)

dc.set('abc', 123)
value = dc.get('abc')
puts value
