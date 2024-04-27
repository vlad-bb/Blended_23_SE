import re

"""
Є словник з мільйоном елементів, ми знаємо значення, але хочемо знайти ключ
"""

users = {
    "Bob Sponge": "098700",
    "Bill Murey": "0766633",
    "Ann Dou": "0689922"
}

phone = users.get("Bob Born", "Unknown")
print(phone)  # O(1)

counter = 1
for key, value in users.items():
    print(counter)
    if value == '0766633':
        print(f"Contact found, name {key} phone {value}")  # O(n)
        break
    counter += 1


def read_email(email_address):
    print(f"Read important email from {email_address}")


emails = ["bill@gmail.com", "noreply@amazon.com", 'info@goit.com.ua', 'win@casino.com']
spam_words = ['casino', '1000000']
inform_list = ["noreply", 'dontreply']


# складний алгоритм
# for email in emails:  # O(n*m)
#     is_spam = False
#     for spam in spam_words:
#         if spam in email:
#             print("Skip spam email")
#             is_spam = True
#             break
#     # if not is_spam:
#     #     read_email(email)
#
#     is_info = False
#     for info in inform_list:
#         if info in email:
#             print("Skip info email")
#             is_info = True
#             break
#
#     if not is_info and not is_spam:
#         read_email(email)

# простий алгоритм

def read_email(email_address):
    print(f"Read important email from {email_address}")


emails = ["bill@gmail.com", "noreply@amazon.com", 'info@goit.com.ua', 'win@casino.com']
spam_words = ['casino', '1000000']
inform_list = ["noreply", 'dontreply']

spam_temp = f'^(?!.*({"|".join(spam_words)})).*$'  # todo fix regex
info_temp = f'^(?!.*({"|".join(inform_list)})).*$'  # todo fix regex

spam_pattern = re.compile(rf'^(?!.*({"|".join(spam_words)})\b).*$')
info_pattern = re.compile(rf'^(?!.*({"|".join(inform_list)})\b).*$')

for email in emails:  # O(n)
    if spam_pattern.match(email):
        print("Skip by spam")
        continue
    elif info_pattern.match(email):
        print("Skip by info")
        continue

    read_email(email)
