#!/usr/bin/python3

# formula is 1 kg = 2.2 lb

def convert(kg):
    pounds = kg * 2.2
    return pounds  


var1 = int(input("Enter a weight in Kg : "))
var2 = convert(var1)
print(f"{var1}kg is equal to {var2} lbs")

