class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hours = int(self.hours)
        minutes = int(self.minutes)
        seconds = int(self.seconds)
        if hours < 10 and minutes < 10 and seconds < 10:
            return f'0{hours}:0{minutes}:0{seconds}'
        elif hours < 10 and minutes < 10 and seconds >= 10:
            return f'0{hours}:0{minutes}:{seconds}'
        elif hours < 10 and minutes >= 10 and seconds >= 10:
            return f'0{hours}:{minutes}:{seconds}'
        elif hours >= 10 and minutes >= 10 and seconds >= 10:
            return f'{hours}:{minutes}:{seconds}'
        elif hours >= 10 and minutes < 10 and seconds < 10:
            return f'{hours}:0{minutes}:0{seconds}'
        elif hours >= 10 and minutes >= 10 and seconds < 10:
            return f'{hours}:{minutes}:0{seconds}'

    def next_second(self):
        hours = int(self.hours)
        minutes = int(self.minutes)
        seconds = int(self.seconds) + 1
        self.seconds = seconds
        if seconds > Time.max_seconds:
            self.seconds = 0
            minutes += 1
            self.minutes = minutes
        if minutes > Time.max_minutes:
            self.minutes = 0
            hours += 1
            self.hours = hours
        if hours > Time.max_hours:
            self.hours = 0
        return Time.get_time(self)

time = Time(10, 59, 59)
print(time.next_second())