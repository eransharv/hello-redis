require 'redis'
require 'connection_pool'

Redis.current = ConnectionPool.new(size: 10, timeout: 5) do
	redis = Redis.new(
		:host => "pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com", 
		:port => 13628, 
		:db => 0, 
		:password => "rs87362c",
		:connect_timeout => 1.0,
		:read_timeout => 1.0,
		:write_timeout   => 1.0
	)
	redis.set('foo', 'bar');
	value = redis.get('foo');
	puts  value
end

