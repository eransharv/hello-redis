require 'dalli' #Ruby client for accessing memcached servers
require 'connection_pool' #Generic connection pooling for Ruby


options = { :username => 'eran', :password => 'rs87362c' }
dc = Dalli::Client.new('pub-memcache-11977.us-east-1-1.2.ec2.garantiadata.com:11977', options)

MEMCACHED = ConnectionPool.new(size: 10, timeout: 3) { dc }

MEMCACHED.with do |conn|
  conn.set('foo', 'bar')
end
