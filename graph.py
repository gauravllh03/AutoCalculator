import numpy as np
import math
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
graph('np.tanh(x)', range(-10, 11))
