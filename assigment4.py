vehicle_type = str(input("vehicle type :"))
fastag_active = True
is_national_holiday = false

if fastag_active == False:
    print("Double toll penalty applied: cash mode")

elif is_national_holiday == True:
    print("Festive waiver applied: half toll")

elif vehicle_type == "car":
    print("Toll amount: 100 rupees")

elif vehicle_type == "SUV":
    print("Toll amount: 150 rupees")

elif vehicle_type == "truck":
    print("Toll amount: 300 rupees")

else:
    print("Invalid vehicle category")
