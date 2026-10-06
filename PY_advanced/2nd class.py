
# try:
#     number = int(raw)
# except ValueError:
#     print("Not a number.")
# else:
#     #only runs if int(row) suceeded
#     print("Something")
    
# # Finally
# try:
#     f =open("data.txt")
#     process(f)
# except OSError:
#     print("Could not open file.")
# finally:
#     print("Cleaning up...")
    
# # Raise

# class InsufficientFundError(Exception):
#     pass



# def withdraw(balance, amount):
#     if amount <= 0:
#         raise InsufficientFundError("Amount must be positive.")
#     if amount > balance:
#         raise InsufficientFundError("Insufficient funds.")
#     return balance - amount

# withdraw(100_000, 80_000)

# def second_item(x):
#     try:
#         return(x[1])
#     except (IndexError, TypeError) as e:
#         return f"Error: {e}"

# print(second_item([10]))

f =open("EXERCISE 2.txt","r", encoding ="utf-8")
content = f.readlines()
print(content)
# print(f.readline())
# print(f.readlinze())
# print(f.readline())
# for i in range(1,11):
#     print(f.readline())