# Learning goal of this tutorial
* Get familiar with different charts

# (Optional) Installing the libs
* `npm install highcharts --save`
* `npm install highcharts-more --save`
* `npm install highcharts-3d --save`
* `npm install angular2-highcharts --save`

# HighCharts Demo
* https://www.highcharts.com/demo
* https://www.highcharts.com/demo/pie-basic

Note: While examining the highcharts demo, open the view options, than copy the options for the chart you are interested.

# HighCharts Examples
* [angular2-highcharts examples](https://github.com/gevgeny/angular2-highcharts/blob/master/README.md)

# HighChart Offline Export
* https://www.highcharts.com/docs/export-module/client-side-export

# Todo:
load your data to the plots

<!-- 
# 0. Config Server seed (Linux & Macosx & Windows)
To make the local sbt executable
* `cd server`
* chmod 700 sbt
* chmod -R 700 ./sbt-dist/bin

# 1. How to use this seed? (Linux & Macosx)
## 1.1 Deploy your web-client
* Change the path in your console to folder myClient with `cd myClient`
* Install npm packages for building the client with `npm install`
* Deploy the production client codes to the server `npm run build`

## 1.2 config your server
* open the config file `server/conf/application.conf` in IDE
* edit the myApp.home variable with the absolute path of your conf folder
```
myApp.home="/Users/yingding/VCS/github/hca17/week3/server/conf"
```
Note: Windows OS shall use the exactly the same path string as linux and macosx, for local.properties in Android, windows need to `\\` and `\:` in the path.
* edit the mongodb connection URL
```
playjongo.uri="mongodb://username:password@127.0.0.1:27017/mydb"
```
Note: 
* replace the username with your mongodb username
* replace the password with your mongodb password for the username
* replace the 127.0.0.1 with your host ip
* replace mydb with your mongodb database name, in demo case it is the same "mydb"

## 1.3 Start server
* Change the path in your console to folder server with `cd ../server`
* Open the play interactive console with `./sbt`
* Type `~run` to start play server in watch mode
* Stop play server with `Ctl + D`
* Then `enter` 

## 1.4 See daemon in action
* The play module follows lazy loading, with out the tcp request server module will not be loaded.
* Call your web-client `localhost:9000` in browser and examine the output in the sbt console
* A example daemon printing out a date string for every minutes can be seen.

# 2. Issue while import the sbt project in IntelliJ IDEA
* right click on week3 (root of the project)
* Click on "File" (in Menu) -> Project Structure... -> remove the root and root-build module in Module section with "-"
* open the build.sbt in server folder in IntelliJ IDEA utimate
* Click on the "import project" on the yellow popup message
* After indexing the play java project shall be imported properly
-->

# Change Log:
* added sass loader in webpack.common.js
* updated nav bar to the side bar
* added examples of charts with highcharts

