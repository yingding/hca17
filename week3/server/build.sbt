name := """server"""

version := "0.0.1"

lazy val root = (project in file(".")).enablePlugins(PlayJava)

scalaVersion := "2.11.11"

libraryDependencies += javaJdbc
libraryDependencies += cache
libraryDependencies += javaWs
libraryDependencies += "org.mongodb" % "mongo-java-driver" % "3.2.2"
libraryDependencies += "org.jongo" % "jongo" % "1.3.0"
libraryDependencies += "uk.co.panaxiom" %% "play-jongo" % "2.0.0-jongo1.3"
libraryDependencies += "commons-collections" % "commons-collections" % "3.2.1"
