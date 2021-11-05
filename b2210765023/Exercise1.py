N = int(input("Please enter a number: "))

odds = 0
evens = 0
counter = 0
for i in range (1,N+1):
    if i%2!=0 :
        odds += i
    else :
        evens += i
        counter += 1

print("The sum of odd numbers is",odds)
print("The average of even numbers is",evens//counter)
