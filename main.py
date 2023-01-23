#city = input("What is name of your city?\n")
#pet_name = input("What is the name of your pet?\n")
#brand_name = print("Your Brand name could be " + city + " " + pet_name)


age = input("What is your age?\n")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"you have {days_remaining}days, {weeks_remaining}weeks,{months_remaining}months, {years_remaining}years"
print(message)