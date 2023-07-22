def age_to_day(age):
    days = age * 365
    return days

var1 = int(input("How old are you : "))
var2 = age_to_day(var1)

print(f"You are {var1} old, that's mean you lived {var2} days")
