import art_Day10

def add(n1, n2):
    return n1 + n2

def subtract(n1 , n2):
 return n1-n2

def multiply(n1 , n2):
 return n1 * n2

def divide(n1 , n2):
 return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide ,
}

def calculator():
    print(art_Day10.logo)
    first_num = float(input("What is the first number?: "))
    calc = True

    while calc:
        for symbol in operations:
            print(symbol)
        operation_to_choose = input("Pick an operation : ")
        second_num = float(input("What is the second number?: "))
        answer = operations[operation_to_choose](first_num , second_num)
        print(f"{first_num} {operation_to_choose} {second_num} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or  type 'n' to start a new calculation: ").lower()
        if choice == "y":
            first_num = answer
        else :
            calc = False
            print("\n" * 25)
            calculator()

calculator()




"""code written by me """
# def continue_calculation(n1 , n2):
#     ans = 0
#     k = ""
#     for key in operations:
#         if key == operation_to_choose:
#             k = key
#             ans = operations[key](n1, n2)
#             break
#     return  f"{n1} {k} {n2} = {ans}" , ans
#
#
# print(art.logo)
# first_num = float(input("What is the first number?: "))
#
# for symbol in operations:
#     print(symbol)
# operation_to_choose = input("Pick an operation : ")
# second_num = float(input("What is the second number?: "))
#
# #LOGIC BEGINS HERE
# calc = True
# while calc:
#     answer , key_actual_val = continue_calculation(first_num ,second_num)
#     print(answer)
#
#     is_new_calc = input(f"Type 'y' to continue calculating with {key_actual_val}, or  type 'n' to start a new calculation: ").lower()
#     if is_new_calc == "n":
#         continue_calc = False
#
#         print("\n" * 25)
#         print(art.logo)
#         first_num = float(input("What is the first number?: "))
#     else:
#         first_num = key_actual_val
#
#         print(art.logo)
#
#     for symbol in operations:
#         print(symbol)
#
#     operation_to_choose = input("Pick an operation : ")
#     second_num = float(input("What is the second number?: "))
#
#
#


