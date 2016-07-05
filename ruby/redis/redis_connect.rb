require 'redis'

redis = Redis.new(:host => "pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com", :port => 13628, :db => 0, :password => "rs87362c")

redis.set('foo', 'bar');
value = redis.get('foo');
puts value

