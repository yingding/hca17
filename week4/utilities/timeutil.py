import datetime

class TimeUtil():
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
        return cls.unix_time_secs(dt) * 1000

    @classmethod
    def unix_time_secs(cls, dt):
        """
        this method transforms datetime object to utc timestamp in seconds
        :param dt: a utc datetime object
        :return: utc timestamp in seconds
        """
        return (dt - cls.epoch).total_seconds() * 1.0

    @classmethod
    def timestamp_in_secs_2_datetime(cls, timestamp):
        """
        this method transforms the long representation of a utc timestamp to a datetime object
        :param timestamp: long
        :return: datetime object of the timestamp (long) given
        """
        return cls.epoch + datetime.timedelta(seconds=timestamp)