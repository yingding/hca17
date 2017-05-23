import pandas as pd
from pymongo.database import Database as Database
from typing import Any

class AccessHelper:

    @classmethod
    def get_collection_entries_as_list(cls, db: Database, collection_name: str, **kwargs):
        # db.collection.find() returns a cursor, which you can iterate through
        # the cursor can also be passed to creat a list
        condition = {}
        # default mapper identity function
        mapper = lambda x : x;
        if 'start' in kwargs and 'end' in kwargs and 'col_name' in kwargs:
            start, end, col_name = kwargs['start'], kwargs['end'], kwargs['col_name']
            condition = {col_name : {'$gte':int(start),'$gte':int(end)}}
        if 'mapper' in kwargs:
            mapper = kwargs['mapper']
        cursor = db[''+collection_name].find(condition)
        collection_entries = list(map(mapper,cursor))
        return collection_entries

    @classmethod
    def get_collection_entries_as_dataframe(cls, db: Database, collection_name: str, **kwargs):
        """
        :param db:
        :param collection_name:
        :param kwargs: named args
        :return:
        """
        list = cls.get_collection_entries_as_list(db, collection_name, **kwargs)
        return pd.DataFrame(data=list)


    @classmethod
    def set_index_inplace(cls, df: pd.DataFrame, idx_column):
        """
        :param df:
        :param idx_column:
        :return:
        """
        df.set_index(idx_column, inplace=True)

