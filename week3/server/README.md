# 1. Import Project in IntelliJ Idea utimate
* open the file `server/build.sbt` in your IntelliJ IDE
* click on the `import project` in the popup menu while build.sbt is opening 

# 2. Setting up connections to mongodb
The following packages are used to establish a connection to mongodb in play framework. The libraryDependencies are declared in build.sbt file
```
libraryDependencies += "org.mongodb" % "mongo-java-driver" % "3.2.2"
libraryDependencies += "org.jongo" % "jongo" % "1.3.0"
libraryDependencies += "uk.co.panaxiom" %% "play-jongo" % "2.0.0-jongo1.3"
libraryDependencies += "commons-collections" % "commons-collections" % "3.2.1"
``` 

# 3. Install mongodb
* Install the mongodb according to https://docs.mongodb.com/manual/administration/install-community/
* on the ubuntu server, change the bindIp in /etc/mongd.conf file to your server ip, allow remote access to mongdb server
* restart mongodb with `sudo service mongod restart`
* use `netstat -tulpn` to display the services running in the system


# 4. Adding an admin user to your mongodb server
* `mongo -host <ip of the server>`
* `use mydb` (to create a db names mydb)
* Run the following command in your mongo shell in your server to create a user and password for the database
```
db.createUser({user:"xxxxxxx", pwd:"xxxxxxx", roles:["readWrite", "dbAdmin"]})
```
Note: you shall change the user name and pwd according to your need.

# 5. Open firewall settings on the server to allow remote access to mongodb
* List all the open ports with `iptables -L`
* Use iptable to setup firewall and open the incomming mongdb connections `sudo iptables -A INPUT -p tcp --destination-port 27017 -m state --state NEW,ESTABLISHED -j ACCEPT`
* save the iptable settings with `sudo iptables-save > /etc/iptables.conf`
* (optional) load the iptable settings with `sudo iptables-restore < /etc/iptables.conf`

For more details please refer to:
* https://docs.mongodb.com/manual/tutorial/configure-linux-iptables-firewall/
* https://www.rosehosting.com/blog/how-to-open-ports-in-ubuntu-and-centos-using-iptables/

# 6. Testing the connection with Robomongo
* Download Robomongo from https://robomongo.org/ for your os system
* Test the connection to your db server

# 7. Debugging the Server
* (Linux, MacOSX)start debugger with `./sbt -jvm-debug 9999` , debugging port 9999
* (Windows) start debugger with
```console
set SBT_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=9999" && sbt
```
* In IntelliJ IDEA utimate : menu -> Run -> Edit Configurations... -> + -> remote 
* Add the name: play-java-debugger
* In settings section : host "127.0.0.1", Port "9999"
* Apply and O.k.
* Set the break point and run the play-java-debugger

<!-- windows reference from https://stackoverflow.com/questions/23332378/how-can-i-enable-remote-debugging-for-sbt-in-windows -->

# Additional Readings about Play Java Seed (Starter)

This is a starter application that shows how Play works.  Please see the documentation at https://www.playframework.com/documentation/latest/Home for more details.

## Running

Run this using [sbt](http://www.scala-sbt.org/).  If you downloaded this project from http://www.playframework.com/download then you'll find a prepackaged version of sbt in the project directory:

```
./sbt run
```

And then go to http://localhost:9000 to see the running web application.

## Controllers

There are several demonstration files available in this template.

- HomeController.java:

  Shows how to handle simple HTTP requests.

- AsyncController.java:

  Shows how to do asynchronous programming when handling a request.

- CountController.java:

  Shows how to inject a component into a controller and use the component when
  handling requests.

## Components

- Module.java:

  Shows how to use Guice to bind all the components needed by your application.

- Counter.java:

  An example of a component that contains state, in this case a simple counter.

- ApplicationTimer.java:

  An example of a component that starts when the application starts and stops
  when the application stops.

## Filters

- Filters.java:

  Creates the list of HTTP filters used by your application.

- ExampleFilter.java

  A simple filter that adds a header to every response.
