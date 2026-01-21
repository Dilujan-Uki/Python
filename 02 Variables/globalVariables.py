x = "Hello Python";

def sayHello():
    x="Hello World";
    print(x);

sayHello();

#Global Keyword
def firstFunction():
    global x;
    x = "all good";

firstFunction();
print("How are these?" + x);