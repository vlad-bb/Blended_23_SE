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
spam_words_string = "|".join(spam_words)
inform_list_string = "|".join(inform_list)

spam_temp = f'^(?!.*(?:{spam_words_string})).*$'  # todo fix regex
info_temp = f'^(?!.*(?:{inform_list_string})).*$'  # todo fix regex

spam_pattern = re.compile(spam_temp)
info_pattern = re.compile(info_temp)

for email in emails:  # O(n)
    if spam_pattern.match(email):
        print("Skip by spam")
        continue
    elif info_pattern.match(email):
        print("Skip by info")
        continue

    read_email(email)
