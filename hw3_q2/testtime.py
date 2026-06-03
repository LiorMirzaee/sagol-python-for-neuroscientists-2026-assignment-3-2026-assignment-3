
class Time:
    def __init__(self, hour= 0, minute = 0, second = 0):
        if isinstance(hour, int) and 0 <= hour < 24:
            self.hour = hour
        else:
            self.hour = 0
        if isinstance(minute, int) and 0 <= minute < 60:
            self.minute = minute
        else:
            self.minute = 0
        if isinstance(second, int) and 0 <= second <60:
            self.second = second
        else:
            self.second = 0

    def __str__(self):
        h= str(self.hour).zfill(2)
        m= str(self.minute).zfill(2)
        s= str(self.second).zfill(2)
        return f"{h}:{m}:{s}"
    
    def is_after(self, other_time):
        self_seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        other_time_seconds = (other_time.hour * 3600) + (other_time.minute * 60) + other_time.second 
        return self_seconds > other_time_seconds
    
    def __add__(self, other_time):
        self_seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        other_time_seconds = (other_time.hour * 3600) + (other_time.minute * 60) + other_time.second 
        
        total_seconds = self_seconds + other_time_seconds
        total_seconds = total_seconds % 86400

        new_hour = total_seconds // 3600
        rimain_seconds = total_seconds % 3600
        new_minute = rimain_seconds // 60
        new_second = rimain_seconds % 60

        return Time(new_hour, new_minute, new_second)
