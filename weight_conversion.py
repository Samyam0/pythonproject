weight = float(input("enter the weight:"))
unit = input("enter K for kilogram and LB for pound(K or LB):")

if unit == "k":
    weight =weight* 2.205
    unit = "lbs"
elif unit =="LB":
    weight/=2.205
    unit = "kg"
else:
    print("invalid input")
print(f"your weight is{weight} {unit}")