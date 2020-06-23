input_seconds = input("Enter the elapsed time in seconds: ")
input_seconds = int(input_seconds)
seconds = input_seconds % 60
minutes_1 = input_seconds // 60
hours = minutes_1 // 60
minutes_2 = minutes_1 % 60

print()
print("The elapsed time in seconds = {}".format(input_seconds))
print()
print("The equivalent time in hours:minutes:seconds = {}:{}:{}".format(hours,minutes_2,seconds))
