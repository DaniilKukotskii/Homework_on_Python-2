# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def user_enter():
    while True:
        try:
            user_num = int(input("Enter the finite number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return user_num



def int_power_of_two(finite_number: int):
    i = 0
    while i < finite_number:
        result = 2**i
        if result > 10: break
        i += 1
        print(result)
    if finite_number == 0: print("Result: 0")


user_ent = user_enter()
power_two = int_power_of_two(user_ent)
