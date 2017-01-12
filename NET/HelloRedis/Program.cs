using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using StackExchange.Redis;

namespace HelloRedis
{
    class Program
    {
        static void Main(string[] args)
        {
            // Connection setup
            var configurationOptions = new ConfigurationOptions
            {
                EndPoints = { "pub-redis-19354.eu-central-1-1.1.ec2.redislabs.com:19354" },
                KeepAlive = 10,
                AbortOnConnectFail = false,
                ConfigurationChannel = "",
                TieBreaker = "",
                ConfigCheckSeconds = 0,
                CommandMap = CommandMap.Create(new HashSet<string>
            { // EXCLUDE a few commands
                "SUBSCRIBE", "UNSUBSCRIBE", "CLUSTER"
            }, available: false),

                Password = "d749djfuHjk"

            };

            ConnectionMultiplexer redis = ConnectionMultiplexer.Connect(configurationOptions);

            // Standard connection
            IDatabase db = redis.GetDatabase();

            RedisValue reply = db.HashGet("myHash", "myElem");
            Console.WriteLine(reply);

        }
    }
}
