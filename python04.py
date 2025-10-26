
'''''# Factorial using for loop
def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Factorial using while loop
def factorial_while(n):
        result = 1
        i = 1
        while i <= n:
            result *= i
            i += 1
        return result

# Taking user input
n = int(input("Enter a number: "))

# Handling negative inputs
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} using for loop: {factorial_for(n)}")
    print(f"Factorial of {n} using while loop: {factorial_while(n)}")'''


'''def is_prime_basic(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False

    is_a_prime = True
    # Check for factors from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            is_a_prime = False
            break  # Exit the loop once a factor is found
    return is_a_prime


# Example usage
print(f"Is 29 a prime number? {is_prime_basic(29)}")
print(f"Is 30 a prime number? {is_prime_basic(30)}")'''


'''def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        print(n)
    if n % 2 == 0:
        print("not a prime number")
        n = n + 1
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                print("not a prime number")
                return False
            else:
                print("prime number")
m=int(input("Enter a number: "))
print(m)
is_prime(m)'''

'''def is_prime(n):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Taking input range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")'''

'''num = int(input("Enter a number: "))
n = abs(num)  # handle negatives
count = 0

if n == 0:
    count = 1  # Special case for 0
else:
    while n > 0:
        n //= 10
        count += 1

print("Number of digits:", count)

num = input("Enter a number: ")'''

'''count = 0
for digit in num:
    if digit.isdigit():  # To ignore '-' sign for negative numbers
        count += 1

print("Number of digits:", count)'''


'''n = int(input("Enter a number: "))
i=1
for i in range(1, n):
    print(i)
    i=i+1
    print(i+1)'''

'''n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of first", n, "natural numbers is:", sum)

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "natural numbers is:", sum)


n= int(input("Enter a number: "))
a=0
b=1
c=0
while c < n:
    print(a, end=" ")
    a=b
    b=a+b
    c += 1'''

'''def grade(p):
    if p>90:
        return 'Grade Distinction'
    elif p>80 and p<90:
        return 'Grade first Class'
    elif p>70 and p<80:
        return 'Grade second Class'
    elif p>60 and p<70:
        return 'Grade third Class'
    else:
        return 'Failed'

print(grade(88))
print(grade(50))
print(grade(91))

def common_elements(l1,l2):
    if len(l1) != len(l2):
        return False
    common = []
    for x in l1:
        if x in l2 and x not in common:
            common.append(x)
    return common

l1=[1,3,5,7,8]
l2=[1,2,3,4,5]
print(common_elements(l1,l2))

def list_of_chars(l):
    chars = []
    for char in l:
        chars.append(char)
    return chars

print(list_of_chars('apple'))

def any_duplicates_list(l):
    elements= []
    for element in l:
        if l.count(element) == 1:
            elements.append(element)
            return 'false'
        else:
            return 'true'

print(any_duplicates_list(['apple', 'banana', 'apple', 'kiwi','orange']))

def occurence_of_elements(l):
    elements = {}
    for i in l:
       elements[i] = l.count(i)
    return elements

print(occurence_of_elements([1,2,3,4,5,1,3]))

s = "abracadabra"
print(s[3:9:1]) 

city = "ETLQALabs"
city_reverse= ''
for i in city:
    city_reverse=i+ city_reverse


print(city_reverse)


city = "ETLQALabs"
sliced_city =city[3:8:1]
print(sliced_city)

def duplicate_chars(l):
    for char in l:
        if l.count(char) > 1:
            return  'duplicates'
    return ' no duplicates'
print(duplicate_chars([1,2,3,4,3]))
print(duplicate_chars([1,2,3,4])) 

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[0:10:2]) 

def getMax(list1):
    max = list1[0]
    for num in list1:
        if num > max:
            max = num
    print(max)

getMax([1,4,3,19,5])

def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime

    i = 2
    while i * i <= n:  # Only check up to square root of n
        if n % i == 0:
            return False  # Not prime if divisible
        i += 1
    return True  # Prime if no divisor found

# Taking input from user
num = int(input("Enter a number: "))

# Printing result
if is_prime(num):
        print("Prime number")
else:
        print("Not a prime number")


#list = [1,6,9,3,1,9,2]

def list_element(n):
    final_list = []
    for element in n:
        if element not in final_list:
            final_list.append(element)

        else:
            continue
    print(final_list)

list_element([1,6,9,3,1,9,2])

def add(n):
    sum = 0
    for num in n:
        sum += num
    print ("addition of list of elements:", sum)


add([1,2,3,4,5,6])

def largest_number(n):
    largest = 0
    for num in n:
        if num > largest:
            largest = num
        else:
            continue

    print("largest number in the list is :",largest)
largest_number([1,6,19,3,22])

def remove_duplicates(l):
    unique = []
    for num in l:
        if num not in unique:
            unique.append(num)
        else:
            continue
    print(unique)
remove_duplicates([1,2,3,4,5,4,3,2,1,9])


def largest_number(n):
    bigger_number = []
    largest = 0
    for num in n:
        if num > largest:
            largest = num
            bigger_number.append(num)
            print(bigger_number)

        else:
            continue

largest_number=[1,4,0,3,22]
second_largest = sorted(list(set(largest_number)))[-2]
print(second_largest)'''

city = 'Bangalore'
print(city[3::-1])








































