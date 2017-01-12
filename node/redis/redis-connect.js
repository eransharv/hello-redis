'use strict';

var redis = require('redis');

// The client stashes the password and will reauthenticate on every connect.
var client = redis.createClient(13628, 'pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com', {no_ready_check: true}, {password: 'rs87362c'});

client.on('connect', function() {
    	console.log('Connected to Redis');
	client.set("foo_rand000000000000", "some fantastic value", redis.print);
	client.get("foo_rand000000000000", redis.print);
});

client.quit(function (err, res) {
    console.log('Exiting from quit command.');
});
