var redisPool = require('redis-connection-pool')('myRedisPool', {
    host: 'pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', // default 
    port: 13628 , //default 
    max_clients: 30, // defalut 
    perform_checks: false, // checks for needed push/pop functionality 
    database: 0, // database number to use 
    options: {
      auth_pass: 'rs87362c'
    } //options for createClient of node-redis, optional 
  });
 
redisPool.set('test-key', 'foobar', function (err) {
  redisPool.get('test-key', function (err, reply) {
    console.log(reply); // 'foobar' 
  });
});
