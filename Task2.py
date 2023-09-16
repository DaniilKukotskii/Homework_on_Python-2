# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# x    y
# 5 + 10 = 15
# 5 * 10 = 50


def find_xy(summa, multiplication):
    for x in range(1, 1001):
        y = summa - x
        if x * y == multiplication: return x, y
        else: return "Integer values for x and y were not found."
        
        # Я пытался сделать так, что если не нашлось подходящих значений, программа сообщала об этом и предлагала попробовать 
        # ввести значения еще раз, чтобы не возвращать None, но не вышло - кусок кода ниже работал даже если целые значения есть.
        # Поэтому вывожу строку о том, что целые значения не были найдены.
        
        
        # else:
        #     print("There are no x and y values for the specified conditions. Do you want to re-enter them?")
        #     user_choice = int(input("Enter 0 if no; Enter 1 if yes: "))
        #     if user_choice == 1: 
        #         user_enter()
        #     else: 
        #         print("Ok, the programm will be closed.")
        #         break



def user_enter():

    while True:
        try:
            user_sum = int(input("Enter the sum: "))
            if user_sum >=1001 or user_sum <= 0: 
                print("You entered an incorrect value. The possible range of numbers is from 1 to 1000 inclusive. Enter again.")
                continue
            else: break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue


    while True:
        try:
            user_multiplication = int(input("Enter the multiplication: "))
            if user_multiplication >=1001 or user_multiplication <= 0: 
                print("You entered an incorrect value. The possible range of numbers is from 1 to 1000 inclusive. Enter again.")
                continue
            else: break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

    if user_multiplication <= user_sum: 
                print("You entered invalid values. Check your entry is correct")
                user_sum, user_multiplication = user_enter()
    
    return user_sum, user_multiplication

# скорее всего, эту функцию(user_enter) можно сократить, но я не знаю как это все объединить, я пытался 


user_sum, user_multiplication = user_enter()

print(f"Result(x, y): {find_xy(user_sum, user_multiplication)}")