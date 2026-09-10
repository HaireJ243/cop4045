import math # use advance mathematical functions
import matplotlib.pyplot as plt

# function to plot mathematical function
def plot_function(fun_str, domain, ns):

    # min and max from tuple
    x_min = domain[0]
    x_max = domain[1]

    #list for x values
    x_values = []

    #list for y values
    y_values = []

    # distance between points on graph
    point = (x_max - x_min) / (ns - 1)

    # start x at min
    x = x_min

    # add values to x_values
    for i in range(ns):

        x_values.append(x)

        #move to next point on graph
        x = x + point

    # calculate y values
    for x in x_values:

        # evaluate using current x
        y = eval(fun_str)

        #add y values to y_values
        y_values.append(y)

    # table heading
    print()
    print("     x       y")

    # print x and y valuess
    for i in range(ns):

        print("%10.4f %10.4f" % (x_values[i], y_values[i]))

    # plot function
    plt.plot(x_values, y_values)

    # axis labels
    plt.xlabel("x")
    plt.ylabel("y")

    #plot title
    plt.title(fun_str)

    #show plot
    plt.show()

#ask user for function
fun_str = input("Enter function with variable x: ")

#ask for # of samples
ns = int(input("Enter number of samples: "))

#ask for x min and max
x_min = float(input("Enter x min: "))
x_max = float(input("Enter x max: ")) 

#create domain tuple
domain = (x_min, x_max)

#call function
plot_function(fun_str, domain, ns)
