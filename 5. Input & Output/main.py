# (5) Input & Output

# Q1. Ask the user for their name and age, then print:
name = str(input("What's your name? "))
age = int(input("What's your age? "))
print(f"Hello {name}! You're {age} years old.") # formatted string

# Q2. Take two numbers as input from the user and print their: Sum, Difference, Product
val1 = int(input("Enter First Number: "))
val2 = int(input("Enter Second Number: "))
print(f"The sum of {val1} and {val2} is {val1 + val2}")
print(f"The difference of {val1} and {val2} is {val1 - val2}")
print(f"The product of {val1} and {val2} is {val1 * val2}")

# Q3. Take these inputs: Name, City, Favorite color. Then print them in one sentence.
person_name = str(input("Enter your name: "))
city = str(input("Enter your city: "))
favorite_color = str(input("Enter your favorite color: "))
print(f"My name is {person_name} I live in {city} and my favorite color is {favorite_color}.") 

# Q4. Take input for: Product name, Product price, Quantity. Then calculate and print the total bill.
product_name = str(input("Enter product name: "))
product_price = int(input("Product price: "))
quantity = int(input("Product quantity: "))
print(f"Your toatal bill is {product_price * quantity}")