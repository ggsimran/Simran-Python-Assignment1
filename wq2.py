full_name = input("Enter your full name: ")

name = full_name.split()

first_initial = name[0][0] 
last_initial = name[-1][0]

initials = f"{first_initial.upper()}.{last_initial.upper()}"
print(f"Your initials are: {initials} ")