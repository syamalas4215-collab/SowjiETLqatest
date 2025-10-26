'''import pandas as pd

df= pd.read_csv("emp.csv")
print(df)'''

'''s= "abc@gmail.com"
l=s.split("@")
print("first split",l)
#print(l)
#p= l.split(".")
#print("last split",p)
p=l[1].split(".")
print("last split",p)
print(type(l))'''

'''email="abc@gmail.com"
username=email.split("@")
u = username[0]
print("Username is",u)
domain=username[1]
print("Domain is",domain)'''

'''sentense="Python is fun and powerful"
count_words = sentense.split(" ")
print("number of words:",len(count_words))
#for word in len(count_words):
    #print(word)'''

'''filename = "report.pdf"
s= filename.split(".")
print("extension:", s[1])'''

'''line = "John,25,Engineer,50000"
s= line.split(",")
print("Name:",s[0])
print("Age:",s[1])
print("Profession:",s[2])
print("salary:",s[3])'''

sentence="I love Python"
s= sentence.split(" ")
reversed_sentence = sentence[1::-1]
#print("reversed:",s[2],s[1],s[0])
print("Reversed sentence:",reversed_sentence)

'''emails = ["ajay@gmail.com", "neha@yahoo.com", "ritu@outlook.com"]
for e in emails:
    print(e.split("@")[1])'''


'''path = "C:/Users/Ajay/Documents/file.txt"
p=path.split("/")
print(p)'''


'''full_name = "Rahul Sharma"
names= full_name.split(" ")
print(names[0])
print(names[1])'''


'''sentence = "Python    is  easy"
sentence1 = sentence.replace("   ", " ")
print(sentence1)'''


email = "ajay@gmail.com"
s= email.split(".")
print("top level domain :",s[1])








