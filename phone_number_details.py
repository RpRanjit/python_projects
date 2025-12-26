import phonenumbers
from phonenumbers import timezone, geocoder, carrier

#Make sure the phone number is string
number = input("Enter your phone number +___: ")
# parse give the detail of phone number
#be sure to write country code before number like +977
phone = phonenumbers.parse(number)
#In which time zone the number is located
time = timezone.time_zones_for_number(phone)
#name of the SIM
car = carrier.name_for_number(phone, "en")

reg = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(car)
print(reg)