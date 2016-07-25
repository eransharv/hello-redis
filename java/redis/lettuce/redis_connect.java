import com.lambdaworks.redis.*;

/**
 * @author Eran Sharvit
 */
public class redis_connect {

    public static void main(String[] args) {
	  
        // Syntax: redis://[password@]host[:port][/databaseNumber]
        RedisClient redisClient = RedisClient.create(RedisURI.create("redis://rs87362c@pub-redis-13628.us-east-1-2.1.ec2.garantiadata.com:13628/0"));

        StatefulRedisConnection<String, String> connection = redisClient.connect();
	RedisCommands<String, String> syncCommands = connection.sync();
	syncCommands.set("foo", "bar!");
        System.out.println("Connected to Redis");
  	connection.close();
        redisClient.shutdown();
    }
}
