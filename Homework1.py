#Question 1
fruits_list=["pear","orange","apple","mandarin","banana"]

# Question2
for index in range(len(fruits_list)):
    if fruits_list[index]=="apple":
        print("I found it")

#Question 3
fruits_list.append("kiwi")
fruits_list.append("pinapple")
print(fruits_list)

#Question 4
letter_list=[len(fruits_list[0]),len(fruits_list[1]),len(fruits_list[2]),len(fruits_list[3]),len(fruits_list[4]),len(fruits_list[5]),len(fruits_list[6])]
for index in range(len(fruits_list)):
    print(fruits_list[index]+"has ",letter_list[index]," letters")

#Question 5
answer=[]
def half_squared(numbers):
    for number in numbers:
         y=(float)(number*number/2)
         answer.append(y)
    return answer

if half_squared([3,3])==[4.5,4.5]:
    print("True")

#Question 6
def tell_grades(grade):
    if (grade>=90 and grade<=100):
        return "Your grade is A."
    elif(grade>=60 and grade<=89):
        return "Your grade is B."
    elif(grade<60 and grade>=0):
        return "Your grade is C."
    elif(grade<0 and grade>100):
        return "Error!"

a=int(input("Please entry your scores:"))
str=tell_grades(a)
print(str)

#Question 7
def reSort(a,b,c):
    if(a<b):
        temp = b
        b=a
        a=temp
    elif (a > b):
        if(a< c):
           temp=c
           c=b
           b=a
           a=temp
        elif(a>c):
            if(b<c):
                temp=c
                c=b
                b=temp
                return a,b,c
            elif(b>c):
                return a,b,c
        return  a,b,c
    return  a,b,c

result=reSort(12,4,32)
print(result)

#Question 8
def traverse(array):
    for row in array:
     for item in row:
      print(item)
s=[[1,2,3],[4,5,6]]
traverse(s)


#Question 9
def f(x):
    arr=[]
    y=str(x**3)
    map(list,y)
    for i in map(str,y):
     arr.append(i)
    print(arr)
    arr=[int(j) for j in arr]
    return arr

number=int(input("Please entry an number:"))
new_arr=f(number)
sum=0
for index in range(len(new_arr)):
    sum=sum+new_arr[index]
print(sum)
result=[]
if(sum==number):
    result.append(number)
    print(result)


#Question 10
import random
def exchange(a,b):
    temp=b
    b=a
    a=temp
    return a,b

x=random.randint(1,10)
y=random.randint(1,10)
print("Produce two random integers:")
print(x,y)
ex_answer=exchange(x,y)
print("Then exchanging them")
print(ex_answer)

#Quetion 11
for i in range(1,8,2):
    print(int((7-i)/2)*" ",end="")
    for j in range(i):
        print("*",end="")
    print()

for i in range(5,0,-2):
    print(int((7-i)/2)*" ",end="")
    for j in range(i):
        print("*",end="")
    print()

#Question 12
for i in range(1,7):
    for j in range(i,7):
        print(j, end="")
    for index in range(0,i-1):
        index=index+1
        print(index,end="")
    print()


#Question 13
players = ['charles','martina','michael','florence','eli']
s=players[:len(players)]
print(s)

for i in range(len(s)):
    print(players[i].title(),end=" ")











