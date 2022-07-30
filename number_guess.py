import random
import math

#Taking Inputs
lower = int(input("Enter Lower Bound: "))

upper = int(input("Enter Upper Bound: "))

print(f"You choose {lower} as lower bound")
print(f"You choose {upper} as upper bound")

result = random.randint(lower, upper)
print("Guess the number in 7 tries")


count = 0
while count < 7:
    count += 1
    Number = int(input("Gues the number: "))
    if result == Number:
        print(f"You got it, the number is {result} in {count}")
        break
    elif result > Number:
        print("Wrong guess, too low, try again")
    else:
        print("Wrong guess, too high, try agian")
if count > 7:
    print("sorry number of tries exceeded")
