# age = int(input("Enter your age : "))

# if age > 16:
#     print("You can drive")
# else:
#     print("You can not drive")


age = int(input("Enter your age : "))

if age > 16 and age < 70:
    print("You can drive")
elif age == 0 or age <= 2:
    print("Infants cant drive")
elif age > 70:
    print("You need to get tested again")
else:
    print("You can not drive")