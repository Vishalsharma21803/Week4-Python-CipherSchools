# File Access Mode
# Read Only => r
# Read and Write => r+
# Write Only => w 
# Write and Read  => w+
# Append Only => a
# Append and Read => a+

"""TEXT FILES"""
file=open("random.txt","w")
file.write("blah blah blah")
file.write("\n new line")
file.close() 
'''Writing a file'''
file=open("random.txt","w")
file.write("Jatin katyal")
a=["Jatin","Katyal","nmarth","aaranah"]
file.writelines(a)
file.close()

'''Reading a file'''
# read
# readline
# readlines

file=open("sample.txt","r")
a=file.read()
print(a)
print(file.read()) 
"""Streams"""
'''
Iterables which can be iterated in single direction.
They don't have starting and ending point.
file is an example of a stream.
'''

"""Smarter Way Of Opening Files"""

#Context Programming

with open("random.txt","r") as file:
    print(file.read())

#print(file.read())



class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self,*args):
        print("Exitted")
        print(args)
        return True

with A() as x:
    print(x)
    print("inside context")
    raise Exception

print("outside context")

#Whatever happens in a context remains in a context


"""JSON FILES"""



'''
<html>
    <body>
        Hi
    </body>
</html>
{
    "html":{
        "body":"Hi"
    }
}
'''

a={
    "name":"Jatin Katyal",
    "marks":100,
    "languages":[
        "c++",
        "python",
        "go",
        "rust"
        ]
}

import json
s=json.dumps(a)
type(a)
print(s)
