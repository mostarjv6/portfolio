
# full working calculete


frist_number = float(input("inter your frist num "))
sec_number = float(input("inter your frist num2 "))
opretor = input("inter your opertor + - * / ")

while opretor not in ["+", "-", "*", "/"]:
    print("Invalid operator. Please enter one of +, -, *, /.")
    opretor = input("inter your opertor + - * / ")

if opretor == "+":
    print(frist_number + sec_number)
elif opretor == "-":
    print(frist_number - sec_number)
elif opretor == "*":
    print(frist_number * sec_number)
elif opretor == "/":
    print(frist_number / sec_number)
 
else:
    print("something went wrong")
    
 