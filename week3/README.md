# 0. Config Server seed (Linux & Macosx)
To make the local sbt executable
* `cd server`
* chmod 700 sbt
* chmod -R 700 ./sbt-dist/bin

# 1. How to use this seed? (Linux & Macosx)
## 1.1 Deploy your web-client
* Change the path in your console to folder myClient with `cd myClient`
* Install npm packages for building the client with `npm install`
* Deploy the production client codes to the server `npm run build`

## 1.2 Start server
* Change the path in your console to folder server with `cd ../server`
* Open the play interactive console with `./sbt`
* Type `~run` to start play server in watch mode
* Stop play server with `Ctl + D`
* Then `enter` 