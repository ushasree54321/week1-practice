hours=int(input())
if hours <= 2:
    parking_charge = hours*30
elif hours <= 5:
    parking_charge = hours*25
else:
    parking_charge = hours*20

if parking_charge > 150:
    service_charge = 20
else:
    service_charge = 0

final_amount = parking_charge+service_charge

print("Parking Charge: ",parking_charge)
print("Service Charge: ",service_charge)
print("Final Amount: ",final_amount)
