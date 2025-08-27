num = 29

flag = False

if num > 1:
    # check for factors 
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            flag = True
            break


if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")