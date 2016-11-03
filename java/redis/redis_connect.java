import redis.clients.jedis.JedisPool; 
import redis.clients.jedis.JedisPoolConfig; 
import redis.clients.jedis.Jedis;
import redis.clients.jedis.Protocol;

public class redis_connect {

//Example of a JedisPoolConfig that has good configuration with our 

    public static void main(String[] args) {
         
	//localhostJedis j = new Jedis("pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com",13628);
       //j.auth("rs87362c");

       
	// // Create and set a JedisPoolConfig
	JedisPoolConfig poolConfig = new JedisPoolConfig();


 	//While it is nice to know your connections are still alive, those onBorrow PING requests are wasting an RTT before your request, and the other two tests are wasting valuable Redis resources. In theory, a connection can go bad even after the PING test so you should catch a connection exception in your code and deal with it even if you send a PING. If your network is mostly stable, and you do not have too many drops, you should remove those tests and handle this scenario in your exception catches only.

	//// Tests (PING) whether connection is dead when connection retrieval method is called.  Sends a PING request when you ask for the resource.
 	poolConfig.setTestOnBorrow(false);

	// Tests (PING) whether connection is dead when returning connection to the pool. Sends a PING whe you return a resource to the pool.
	poolConfig.setTestOnReturn(false);

	//Tests (PING) whether connections are dead during idle periods.  Sends periodic PINGS from idle resources in the pool.
        poolConfig.setTestWhileIdle(false);



   	//Number of connections to Redis that can be in the pool
      	poolConfig.setMaxTotal(50);

 	//Minimum number of idle connections to Redis. These can be seen as always open and ready to serve
	poolConfig.setMinIdle(3);
 	
	// Maximum number of idle connections to Redis
	poolConfig.setMaxIdle(20);

  	//Idle connection checking period
	 poolConfig.setTimeBetweenEvictionRunsMillis(0);   // setting it to any onther value will trigger an eviction every period, and the number of max conns that will be evicted in every cycle is defined in the next param.


        //Maximum number of connections to test in each idle check
        poolConfig.setNumTestsPerEvictionRun(5);


	poolConfig.setMaxWaitMillis(30000);

       JedisPool pool = new JedisPool(
       		poolConfig,
               "redis-17773.c10.us-east-1-3.ec2.cloud.redislabs.com",
               17773,              
               Protocol.DEFAULT_TIMEOUT,
               "pXgI5OocM8JvxMjG"
       );

	Jedis j = pool.getResource();
	j.set("foo", "bar");
        System.out.println(j.get("foo"));
        j.close();
    }

}
