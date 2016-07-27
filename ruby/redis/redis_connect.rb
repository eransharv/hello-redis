require 'redis' #using the redis-rb, A Ruby client library for Redis
require 'connection_pool' //Generic connection pooling for Ruby


#If no object is available in the pool within :timeout seconds, it  will raise an error
Redis.current = ConnectionPool.new(size: 10, timeout: 5) do
 	#All timeout values are specified in seconds
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

