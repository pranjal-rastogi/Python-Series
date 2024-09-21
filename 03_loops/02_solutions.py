n = int(input("Enter the number: "))

sum_even_number = 0;

for num in range(1,n+1):
    if num % 2 == 0:
        sum_even_number += num

print(sum_even_number)
