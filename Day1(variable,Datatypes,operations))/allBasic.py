#create a variable to give meomary or store something any data type name of variable is known as variable name

#a is storing string type of data(text inclued in "" is called string) so data type of a is string
a = 'hello'
#a is storing number so data type of a is INT
a =10


# now to print anything int terminal we use print 
    # print("hello")
# print whats inside variable a 
    # print(a)
    
b=10
c=b

b=12

print(c)
print(b)

# a is storint bollean type data which is true
a=True

#concatinade to string variable
firstName  = "Rohit"
lastName = "7" #in js you can also concatenate str and int cause it convert int to string if its str+int

print(firstName+" "+lastName)


#arr or list arr can contain any type str int bool even one more arr and arr is ot datatype its datastructure cause it stores multiple value
a =[1,"my name is","Rohit"]
print(a[1]+" "+a[2])

#object or dict it stores key value pair value of key can be of anytype  and it can store datastructure also

obj = {
    "hello":"yellow",
    "bat":"ball",
    "arr":[1,2,3]
}
print(obj.get("hello"))
print(obj["arr"])