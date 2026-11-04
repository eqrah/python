#if not type caste then it will show like
a="4"
b="3"
print(a+b) #output=43
print(int(a)+int(b)) #output= 7



#TYPECASTIG=Datatype to another datatype
#EXPlicit conversion = done by programmeer or developer as per req.

string1="11"
no=6
string_no = int(string1)
sum1= no+ string_no
print("RESULT IS:",sum1)
print(type(sum1))

x="4"
y="2"
print(int(x)+int(y))



#Implicit conversion = done by python itself from lower DATATYPE to higher data type
a=5
b=6.4
c=a+b
print(c)
print(type(c))
