class time:
  def __init__(self,h=0,m=0,s=0):
    self.h=hour
    self.m=minute
    self.s=second
  def __add__(self, other):
	total_seconds = self.h * 3600 + self.m * 60 + self.s + \
	other.h * 3600 + other.m * 60 + other.s

	new_hour, remainder = divmod(total_seconds, 3600)
	new_minute, new_second = divmod(remainder, 60)

	return Time(new_hour, new_minute, new_second)

    def __str__(self):
	return "{self.h:02d}:{self.m:02d}:{self.s:02d}"

# Example usage:
time1 = Time(3, 45, 30)
time2 = Time(1, 30, 15)

sum_time = time1 + time2
print("Time 1:", time1)
print("Time 2:", time2)
print("Sum of Time 1 and Time 2:", sum_time)

