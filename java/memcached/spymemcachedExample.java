import java.io.IOException;
//import net.spy.memcached.*;
import net.spy.memcached.AddrUtil;
import net.spy.memcached.ConnectionFactoryBuilder;
import net.spy.memcached.ConnectionFactoryBuilder.Protocol;
import net.spy.memcached.MemcachedClient;
import net.spy.memcached.auth.AuthDescriptor;

public class spymemcachedExample {
    public static void main(String[] args) {
//        AuthDescriptor ad = new AuthDescriptor("PLAIN", new PlainCallbackHandler("eran", "rs87362c"));

        try {
  		MemcachedClient client = new MemcachedClient(new ConnectionFactoryBuilder()
        		.setProtocol(Protocol.BINARY)
		        .setAuthDescriptor(AuthDescriptor.typical("eran", "rs87362c"))
		        .build(), AddrUtil.getAddresses("pub-memcache-11977.us-east-1-1.2.ec2.garantiadata.com:11977"));

		client.set("foo", 0, "bar");
		String value = (String)client.get("foo");
		System.out.println(value);

        } catch (IOException e) {
            // handle exception
        }
    }
}
