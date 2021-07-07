

num = int(input("Enter the No: "))
count = 0

if (num == 6174):
    count += 1
    print("Constant Found at iteration: " + str(count))
else:
    difference = 0
    num = [str(x) for x in str(num)]
    while(difference != 6174):
        count += 1

        num.sort()
        start = int("".join([str(i) for i in num]))
        num.sort(reverse=True)
        rev = int("".join([str(i) for i in num]))
        difference = abs(rev-start)
        num = [str(x) for x in str(difference)]
        print(num)

print("No of times executed: " + str(count))
