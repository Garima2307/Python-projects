import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for easy level: use strings instead of lists
#hard level:
list_of_pss = []
for n in range(0,nr_letters):      #0<=X<nr_letters
    l = random.choice(letters)
    list_of_pss.append(l)

for n in range(0,nr_symbols):
    l = random.choice(symbols)
    list_of_pss.append(l)

for n in range(0,nr_numbers):
    l = random.choice(numbers)
    list_of_pss.append(l)

print(list_of_pss)
random.shuffle(list_of_pss)
print(list_of_pss)


password = ""
for char in list_of_pss:
    password += char
print(f"Your Password is: {password}")