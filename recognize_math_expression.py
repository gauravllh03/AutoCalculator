
"""
Requires:
- Python 3
- pip install opencv-python
- pip install pytesseract
- download Tesseract-OCR data
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image
import pyautogui
import math
from sympy import *
import matplotlib.pyplot as plt

def graph(formula, x_range):
    if formula.find("tan")!=-1 or formula.find("sin")!=-1 or formula.find("cos")!=-1:
        x = np.arange(0,3*np.pi,0.1)
    else:
        x=np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.title("Graph for the expression detected is :")
    plt.xlabel("x-values ------->")
    formula=formula+" ------>"
    plt.ylabel(formula)
    plt.show()


    
def integration(s):
    x, y = symbols('x y') 
    print("Before Integration : {}".format(s)) 
    # Use sympy.integrate() method 
    intr = integrate(s, x) 
    print("After Integration : {}".format(intr))

    
def differentiation(s):
    x, y = symbols('x y') 
    print("Before Differentiation : {}".format(s)) 
    # Use sympy.integrate() method 
    intr = diff(s, x) 
    print("After Differentiation : {}".format(intr))


def findRoots( a, b, c): 
    if a == 0: 
        print("Invalid") 
        return -1
    d = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(d)) 
    if d > 0:
        print("Real roots")
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
    elif d == 0:
        print("Equal roots")
        print(-b / (2*a)) 
        print(-b / (2*a)) 
    else: #d<0
        print("Imaginary roots")
        print(- b / (2*a) , " + i", sqrt_val/(2*a)) 
        print(- b / (2*a) , " - i", sqrt_val/(2*a)) 
  

def is_valid_expression(number1, number2, operator, result):
    number1 = int(number1)
    number2 = int(number2)
    result = int(result)
    if operator == '-':
        return number1 - number2 == result
    if operator == '+':
        return number1 + number2 == result
    if operator == 'x' or operator == '*':
        return number1 * number2 == result
    if operator == ":" or operator == "/":
        return number1 / number2 == result


    
def precedence(op): 
      
    if op == '+' or op == '-': 
        return 1
    if op == '*' or op == '/' or op == '%': 
        return 2
    return 0




def applyOp(a, b, op): 
      
    if op == '+': return a + b 
    if op == '-': return a - b 
    if op == '*': return a * b 
    if op == '/': return a // b
    if op == '%': return a % b

def trigoevaluate(tokens): 
      
    values = []  
    ops = [] 
    i = 0
      
    while i < len(tokens): 
           
        if tokens[i] == ' ': 
            i += 1
            continue

        elif tokens[i] == '(': 
            ops.append(tokens[i]) 
            i=i+1
        
        elif tokens[i].isalpha(): 
            val = 0
            trig_op=""
            for j in range(3):
                trig_op+=tokens[i]
                i+=1
               
            while (i < len(tokens) and
                tokens[i].isdigit()): 
              
                val = (val * 10) + int(tokens[i]) 
                i += 1
            if(i < len(tokens) and tokens[i] == ' '):
                i+=1
            if(i < len(tokens) and tokens[i] == '.'):
                i+=1
                k=1
                
                if(tokens[i] == ' '):
                    i+=1
                while(i < len(tokens) and tokens[i].isdigit()):
                    val += (int(tokens[i])/math.pow(10,k))
                    k+=1
                    i+=1
              
            if trig_op == "sin":
                val=math.sin(val)

            elif trig_op == "cos":
                val=math.cos(val)

            elif trig_op == "tan":
                val=math.tan(val)

            elif trig_op == "log":
                val=math.log(val)

            values.append(val) 
        
        elif tokens[i] == ')': 
          
            while len(ops) != 0 and ops[-1] != '(': 
              
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.pop() 
            i=i+1
          
        else: 
           
            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                          
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.append(tokens[i]) 
            i=i+1
          
        #i += 1
    while len(ops) != 0: 
          
        val2 = values.pop() 
        val1 = values.pop() 
        op = ops.pop() 
                  
        values.append(applyOp(val1, val2, op)) 
      
    return values[-1] 
  

    
def evaluate(tokens): 
      
    values = []  
    ops = [] 
    i = 0
      
    while i < len(tokens): 
           
        if tokens[i] == ' ': 
            i += 1
            continue

        elif tokens[i] == '(': 
            ops.append(tokens[i]) 
            i=i+1
        
        elif tokens[i].isdigit(): 
            val = 0
               
            while (i < len(tokens) and
                tokens[i].isdigit()): 
              
                val = (val * 10) + int(tokens[i]) 
                i += 1
              
            values.append(val) 
        
        elif tokens[i] == ')': 
          
            while len(ops) != 0 and ops[-1] != '(': 
              
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.pop() 
            i=i+1
          
        else: 
           
            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                          
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.append(tokens[i]) 
            i=i+1
          
        #i += 1
    while len(ops) != 0: 
          
        val2 = values.pop() 
        val1 = values.pop() 
        op = ops.pop() 
                  
        values.append(applyOp(val1, val2, op))
      
    return values[-1] 






while 1:
    input()
    #image=pyautogui.screenshot(region=(1400,210,520,300))
    image=pyautogui.screenshot(region=(1500,80,300,100))
    new_size=tuple(3*x for x in image.size)
    image=image.resize(new_size,Image.ANTIALIAS)
    image=cv2.cvtColor(np.array(image),cv2.COLOR_RGB2GRAY)
    ret,image= cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    cv2.imshow("//test.png",image)
    text=pytesseract.image_to_string(image)
    print("You entered :",text)
    if(text.find("plot")!=-1):
        print("Welcome to graph plotter")
        graph(text[5:],range(-10,11))        
    elif(text.find("int")!=-1):
        print("Welcome to integration calculator !\n")
        integration(text[4:])
    elif(text.find("diff")!=-1):
        print("Welcome to differentiation calculator !\n")
        differentiation(text[5:])
    elif text.find("x2")!=-1:
        print("You entered a Quadratic equation. Nice , let me give you the roots ")
        si=list(text)
        sa=0
        sb=0
        sc=0
        if(si[0]=='-'):
                sa=1
        f=1 
        for i in range(1,len(si)):
            #print(si[i])
            if si[i]=='+':
                si[i]='#'
                if f==1:
                    f=2
                elif f==2:
                    break
            elif si[i]=='-':
                si[i]='#'
                if f==1:
                    f=2
                    sb=1 
                elif f==2:
                    sc=1 
                    break
        #print(si)
        s=""
        for i in si:
            s+=i
        #print(s)
        data=s.split("#")
        #print(data)
        #print(sc)
        b=0
        a=0
        c=0
        l=""
        if len(data)==1:
            a=1
        elif len(data)==2:
            if s[-1]!='x':
                c=int(data[1])
                if sb==1:
                    c=-1*c
                for i in data[0]:
                    if(i=='x'):
                        break
                    elif i=='-':
                        continue
                    else:
                        l+=i
                if l=='':
                    l=1
                a=int(l)
                if sa==1 :
                    a=a*-1
            else :
                for i in data[1]:
                    if(i=='x'):
                        break
                    else:
                        l+=i
                if l=='':
                    l=1
                b=int(l)
                if sb==1 :
                    b=-1*b
                l=""
                for i in data[0]:
                    if(i=='x'):
                        break
                    elif i=='-':
                        continue
                    else:
                        l+=i
                if l=='':
                    l=1
                a=int(l)
                if sa==1 :
                    a=a*-1
        else:       
            c=int(data[2])
            if sc==1:
                c=-1*c
            
            l=""
            for i in data[1]:
                if(i=='x'):
                    break
                else:
                    l+=i
            if l=='':
                l=1
            b=int(l)
            if sb==1 :
                b=-1*b
            l=""
            for i in data[0]:
                if(i=='x'):
                    break
                else:
                    l+=i
            if l=='':
                l=1
            a=int(l)
            if sa==1 :
                a=a*-1
        findRoots(a, b, c)

    elif text.find("tan")!=-1 or text.find("sin")!=-1 or text.find("cos")!=-1:
        print("You entered a Trigonometric equation. Good choice bro!")
        print(trigoevaluate(text))
    else:
        print("You entered an Arithmetic expression")
        print(evaluate(text))
    
    print("------ Done -------")
