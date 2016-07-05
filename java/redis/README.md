How to Use:
-----------

download jedis.jar.

if you want connection pooling download: http://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.2/commons-pool2-2.2.jar


compile the file and add the jar to the classpath:
--------------------------------------------------
- javac -cp jedis-2.8.1.jar redis_connect.java
- with connection pooling: javac -cp commons-pool2-2.2.jar:jedis-2.8.1.jar redis_connect.java 

execute the program:
--------------------------------------------------
- java -cp jedis-2.8.1.jar:. redis_connect
- with connection pooling: java -cp commons-pool2-2.2.jar:jedis-2.8.1.jar:. redis_connect