from constants import COUNTER

local_counter = "Global scope"

payment = 3


def check_order(payment: int):
    global COUNTER
    COUNTER += 1

    def check_payment():
        # nonlocal payment
        # global payment
        if payment < 10:
            # payment += 5
            pass
        return payment

    edited_payment = check_payment()
    return edited_payment


# print(local_counter)

if __name__ == '__main__':
    print(check_order(2))
