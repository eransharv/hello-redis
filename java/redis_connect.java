import redis.clients.jedis.JedisPool; 
import redis.clients.jedis.JedisPoolConfig; 
import redis.clients.jedis.Jedis;
import redis.clients.jedis.Protocol;

public class redis_connect {

    public static void main(String[] args) {
         
	//localhostJedis j = new Jedis("pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com",13628);
       //j.auth("rs87362c");

       JedisPoolConfig poolConfig = new JedisPoolConfig();
       poolConfig.setMaxTotal(128);
	poolConfig.setMaxIdle(10);
	poolConfig.setMinIdle(1);
	poolConfig.setMaxWaitMillis(30000);

       JedisPool pool = new JedisPool(
       		poolConfig,
               "pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com",
               13628,
               Protocol.DEFAULT_TIMEOUT,
               "rs87362c"
       );

	Jedis j = pool.getResource();
	j.set("foo", "bar");
       System.out.println(j.get("foo"));
	pool.returnResource(j);
    }

}
