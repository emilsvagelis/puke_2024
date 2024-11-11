n=int(input("Ievadiet skaitli n: "))
index=1

while index<=n:
    if index%3==0 and index%5==0:
        print("FizzBuzz")
        break
    elif index%3==0:
        print("Fizz")
    elif index%5==0:
        print("Buzz")
    else:
        print(index)


    index+=1