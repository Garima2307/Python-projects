#Experimenting codes here ......NO PROJECTS INSIDE THIS FOLDER


# name = input("Enter your name: ")

# age = int(input("Enter your age: "))

# future_age = age + 10

# print(future_age)

def is_prime(num):
    for i in range(2 , num):
        if num % i ==0 :
            print("False")
            return
        
    print("True")
    return

            
is_prime(45)