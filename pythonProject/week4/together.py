print("Week 4 -- Lab practice")
print("-" * 50)


inputNumber = int(input("Enter a number: "))


if inputNumber % 2 == 0:
    even_number = True
else:
    even_number = False


if even_number:
    print(f"{inputNumber} is an even number")
else:
    print(f"{inputNumber} is an odd number")
