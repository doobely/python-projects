lower = int(input("give lower:  "))
upper = int(input("give upper:  "))
list=[]

for number in range(lower,upper + 1):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            list.append(number)

print(list)
