from utilities.dbutil import MongoDbUtil as mu
from dbhelper.accesshelper import AccessHelper as ah
import pprint # pretty print
from utilities.timeutil import TimeUtil as tu
import pandas as pd

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
# show all collections in mongodb
mu.test(db)

# get all entries as a list
print("\n#### get all entries as a list")
list = ah.get_collection_entries_as_list(db, "moods")
pprint.pprint(list)
# get all entries as dataframe
df = ah.get_collection_entries_as_dataframe(db, "moods")
pprint.pprint(df)

# get all entries as seleted dataframe
print("\n#### get all entries as seleted dataframe")
df = ah.get_collection_entries_as_dataframe(db, "moods", start='1494406821407', end='1494407125644', col_name='_id.timestamp')
pprint.pprint(df)

# get all entries with mapper function
print("\n#### get all entries as seleted dataframe with mapper")
mapper = lambda x: {'timestamp': x['_id']['timestamp'], 'mood': x['mood']}
df = ah.get_collection_entries_as_dataframe(db, "moods",mapper=mapper)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)
pprint.pprint(df)

# get all entries with mapper function and timestamp as index
print("\n#### get all entries as seleted dataframe with mapper")
#format = '%Y-%m-%d %H:%M:%S.%f'
#format = '%Y-%m-%d %H:%M:%S'
mapper = lambda x: {'timestamp': tu.timestamp_in_millisecs_2_datetime(int(x['_id']['timestamp'])), 'mood': x['mood']}
df = ah.get_collection_entries_as_dataframe(db, "moods",mapper=mapper)
pprint.pprint(df)

# get all entries with mapper function and timestamp as index
print("\n#### get all entries as seleted dataframe with mapper and converted index to timestamp")
df = ah.get_collection_entries_as_dataframe(db, "moods",mapper=mapper)
## set index of a dataframe
## https://stackoverflow.com/questions/10457584/redefining-the-index-in-a-pandas-dataframe-object
# format = '%Y-%m-%d %H:%M:%S.%f'

# df['timestamp'] = pd.to_datetime(df['timestamp'])
ah.set_index_inplace(df, 'timestamp')
df.sort_index(inplace=True, ascending=False)
print(df)

# def mood2idx(x):
#     if x == 'NOTHING':
#         return 0;
#     elif x == 'SAD':
#         return -1;
#     elif x == 'HAPPY':
#         return 1;
#     else:
#         return -10



# mood_binary = [mood2idx(x) for x in df['mood'].tolist()]
# pprint.pprint(mood_binary)

## Ploting
# from utilities.plotutil import PlotUtil as pu
# pu.ploting(df.index, mood_binary, "time line", 'mood histogram', 'categorical moods', 'mood', True)





# tu.test()








