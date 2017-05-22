from utilities.dbutil import MongoDbUtil as mu

# Global variable
# Todo: modify user and password
user = ""
password = ""
# Todo: you may also want to change host to your db host ip string
host = "127.0.0.1"
port = "27017"
dbname = "mydb"

# Get Global db object
db = mu.getDB(user, password, host, port, dbname)

# Application Run Section
mu.test(db)



