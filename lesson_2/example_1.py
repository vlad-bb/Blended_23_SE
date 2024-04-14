""" Код без функцій """
# users = []
#
# user_1_name = input("Enter name: ")
# user_1_age = input("Enter age: ")
# user_1_city = input("Enter city: ")
# user_1_phone = input("Enter phone: ")
# users.append([user_1_name, user_1_age, user_1_city, user_1_phone])
#
# user_2_name = input("Enter name: ")
# user_2_age = input("Enter age: ")
# user_2_city = input("Enter city: ")
# user_2_phone = input("Enter phone: ")
# users.append([user_2_name, user_2_age, user_2_city, user_2_phone])
#
# print(users)

''' код з використанням функцій '''


def get_user_info():
    user_name = input("Enter name: ")
    user_age = input("Enter age: ")
    user_city = input("Enter city: ")
    user_phone = input("Enter phone: ")
    return [user_name, user_age, user_city, user_phone]


users = []

for i in range(1, 101):
    print(i)
    user = get_user_info()
    users.append(user)

print(users)
