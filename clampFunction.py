print("Input value -> result of clamp function")
for num in range(0,10):
    if num <= 3:
        print(num, " -> 3")
    elif 3 < num < 6:
        print(num, " ->", num)
    else:
        print(num, " -> 6")
