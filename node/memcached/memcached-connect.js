var memjs = require('memjs');

var mc = memjs.Client.create('pub-memcache-11977.us-east-1-1.2.ec2.garantiadata.com:11977', {
  username: 'eran',
  password: 'rs87362c'
});    

mc.set('foo', 'bar');
mc.get('foo', function (err, value, key) {
    if (value != null) {
        console.log(value.toString());
    }
});
