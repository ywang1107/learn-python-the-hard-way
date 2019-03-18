

def print_num(top,step):
    i = 0
    numbers = []
    while i < top:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers


print("The numbers: ")
numbers = print_num(100,5)
for num in numbers:
    print(num)