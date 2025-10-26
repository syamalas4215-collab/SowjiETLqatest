print("hello world")
print("division of 2 numbers",  50/3.5)
print("multiply a string", "sowji" * 10)

a = 10
b = 3

#print(a + b)  # Addition → 13
# print(a - b)  # Subtraction → 7
# print(a * b)  # Multiplication → 30
# print(a // b) # Floor division → 3
# bprint(a % b)  # Modulus (remainder) → 1
# print(a ** b) # Power → 1000
# non_captalised_string = "hi i am SowJanya"
# print(non_captalised_string.title())

x = 15
x -= 6

print("x value is ", x)
x *= 3
print("x value is ", x)
x /= 3
print("x value is ", x)
x %= 3
print("x value is ", x)
y = 4
y **= 3
print("y value is ", y)

students = ["Anurag","kavya","Akshar","arif","raghu"]

print(students)

student = [3,1.5,7,4,9.5]
x = student.sort()
print(student)

nums = [3, 1.5, 7, 2.2, 10]
nums.sort()
print(nums)


mixed = [3, "apple", 1.5, "banana"]

# Sort as strings
print(sorted(mixed, key=str))
# ['1.5', '3', 'apple', 'banana']

students = ("sowji","ravi","lasya","kavya")
for student in students:
    print("students names are :",student)

fruits = ["apple","banana","orange"]
#for fruit in fruits:
for i in range(len(fruits)):
        print(i,fruits[i])
colors = {"red","orange","yellow","green","pink"}
for color in colors:
    print(color)


