number = int(input('Please give me a number : '))
print("Number is",number)

def A_Func(number) :
    number = str(number)
    string = ""
    for x in number :
        if int(x)%2 == 0 : string +="Even"+x  
        else : string+="Odd"+x
    print("Func A : "+string)
    return string

def B_Func(string):
    string = string.replace("Even", "NEVE" )
    string = string.replace("Odd", "DDO") 
    print ("Func B : "+string)
    return string


def C_Func(string):  
    string = string.replace("DDO", "686879" )
    string = string.replace("NEVE", "78698669") 
    print ("Func C : "+string)
    return string

def D_func(string):
    string = string.replace("78698669", "NEVE" )
    string = string.replace("686879", "DDO")
    print("Func D : "+string)
    return string

def E_Func(string):
    string = string.replace("NEVE", "Even")
    string = string.replace("DDO", "Odd") 
    print ("Func E : "+string)
    return string

def F_Func(string):
    string = string.replace("Even", "")
    string = string.replace("Odd", "") 
    print ("Func F : "+string)
    return int(string)

A_Func_resault = A_Func(number)
print("Type Number input is :", type(number), "Type Resault A is :", type(A_Func_resault))
B_Func_resault = B_Func(A_Func_resault)
print("Type Resault B is :", type(B_Func_resault))
C_Func_resault = C_Func(B_Func_resault)
print("Type Resault C is :", type(C_Func_resault))
D_func_resault = D_func(C_Func_resault)
print("Type Resault D is :", type(D_func_resault))
E_func_resault = E_Func(D_func_resault)
print("Type Resault E is :", type(E_func_resault))
F_func_resault = F_Func(E_func_resault)
print("Type Resault F is :", type(F_func_resault))









