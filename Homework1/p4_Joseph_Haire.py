import math # use advance mathematical functions
import matplotlib.pyplot as plt

# function to plot mathematical function
def plot_function(fun_str, domain, ns):
    
    x_min = domain[0]# min and max from tuple
    x_max = domain[1]
    x_values = []#list for x values
    y_values = []#list for y values

    point = (x_max - x_min) / (ns - 1)# distance between points on graph
    x = x_min# start x at min

    for i in range(ns):# add values to x_values
        x_values.append(x)
        x = x + point#move to next point on graph
    
    for x in x_values:# calculate y values
        y = eval(fun_str)# evaluate using current x
        y_values.append(y)#add y values to y_values

    print() # table heading
    print("     x       y")

    for i in range(ns):# print x and y valuess
        print("%10.4f %10.4f" % (x_values[i], y_values[i]))

    plt.plot(x_values, y_values)# plot function
    plt.xlabel("x")# axis labels
    plt.ylabel("y")
    plt.title(fun_str)#plot title   
    plt.show()#show plot

fun_str = input("Enter function with variable x: ")#ask user for function
ns = int(input("Enter number of samples: "))#ask for # of samples
x_min = float(input("Enter x min: "))#ask for x min and max
x_max = float(input("Enter x max: ")) 

#create domain tuple
domain = (x_min, x_max)

#call function
plot_function(fun_str, domain, ns)
