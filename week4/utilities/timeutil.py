import datetime

class TimeUtil:
    # class / static variable epoch, which is associated to class, different from object variable
    # https://stackoverflow.com/questions/68645/static-class-variables-in-python
    epoch = datetime.datetime.utcfromtimestamp(0)

    @classmethod
    def unix_time_millis(cls, dt):
        """
        this method transforms datetime object to utc timestamp in milliseconds
        :param dt: a utc datetime object
        :return: utc timestamp in milliseconds
        """
        # int() round up the decimals
        return (dt - cls.epoch).total_seconds() * 1000

    @classmethod
    def unix_time_secs(cls, dt):
        """
        this method transforms datetime object to utc timestamp in seconds
        :param dt: a utc datetime object
        :return: utc timestamp in seconds
        """
        return cls.unix_time_millis(dt) / 1000

    @classmethod
    def timestamp_in_secs_2_datetime(cls, timestamp):
        """
        this method transforms the long representation of a utc timestamp to a datetime object
        :param timestamp: long
        :return: datetime object of the timestamp (long) given
        """
        return cls.epoch + datetime.timedelta(seconds=timestamp)

    @classmethod
    def timestamp_in_millisecs_2_datetime(cls, timestamp):
        """
        this method transforms the long representation of a utc timestamp to a datetime object
        :param timestamp: long
        :return: datetime object of the timestamp (long) given
        """
        return cls.epoch + datetime.timedelta(milliseconds=timestamp)

    @classmethod
    def test(cls):
        """
        1494406804593 timestamp in millisecs
        1495574845    23.may.2017 in secs
        :return:
        """
        datetime_now = datetime.datetime.now()
        timestamp_now_in_secs = cls.unix_time_secs(datetime_now)
        timestamp_now_in_millisecs = cls.unix_time_millis(datetime_now)
        print("\n## Testing the timeutil functions")
        print("Datetime Now: {}".format(str(datetime_now)))
        print("Now in utc timestamp in secs:{}".format(timestamp_now_in_secs))
        print("Now in utc timestamp in millisecs:{}".format(timestamp_now_in_millisecs))
