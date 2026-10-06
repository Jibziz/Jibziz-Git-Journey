# try:
#     num1 = int(input("Please enter your numerator: "))

#     num2 = int(input("Please enter your denoinator: "))

#     print(num1/num2)
    
# except ZeroDivisionError:
#     print("Its not divible by Zero")
    
# except ValueError:
#     if type(num1) != int:
#         print("Please enter a valid numerator")
#     else:
#         print("Please enter a valid denominator")
        
user_input = input("Enter a number: ")
   
try:        
    value = int(user_input)
    result = 100 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Bad input: {e}")
    
print("Will this run?")