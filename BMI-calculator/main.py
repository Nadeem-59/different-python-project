# Python calculator 

# agar meine print kay sath round bhi likha tou answer round mei aiye ga warna round mei nhi decimal mei aiye ga answer

operator = input("Enter an operator (+ - * /):")
num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    result = num1 + num2
    print(round(result))

elif operator == "-":
    result = num1 - num2
    print(result)
       
elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(result)

else:
    print(f"{operator} is not valid")
