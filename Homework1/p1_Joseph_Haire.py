import math # use advanced mathematic functions
import matplotlib.pyplot as plt # to plot the graph

while True:

    a = input("Enter a: ")

    # user presses "ENTER" for "a" to exit program without inputting anything
    if a == "": 
        break

    # if user enters number for "a"  continue to input for "b" and "c"
    a = float(a)
    b = float(input("Enter b: ")) 
    c = float(input("Enter c: "))

    # b^2-4ac
    d = b**2 - 4*a*c

    # if d is <, =, or > 0
    # no real solutions
    if d < 0:

        print("no real solutions")

        # find x coordinate
        xopt = -b / (2*a) 

        x_min = xopt - 5 # range of graph
        x_max = xopt + 5

    # one real solution
    elif d == 0:

        # find x of solution
        x1 = -b / (2*a) 

        print("one real solution: %.5f" % x1) # print solution to 5 decimal places as shown in sample

        x_min = x1 - 5 # range of graph
        x_max = x1 + 5

    # two real solutions
    else: 

        #first solution
        x1 = (-b - math.sqrt(d)) / (2*a) # minus sqrt

        #second solution
        x2 = (-b + math.sqrt(d)) / (2*a) # plus sqrt

        print("two real solutions: x1=%.5f, x2=%.5f" % (x1, x2))

        #compare solutions

        if x1 < x2:

            # range of graph to include both solutions
            x_min = x1 - 2 
            x_max = x2 + 2

        else: 

            x_min = x2 - 2
            x_max = x1 + 2

    # list for x values
    x_values = []

    # list for y values
    y_values = []

    #150 points for graph
    graph_point = (x_max - x_min) / 149

    #start at beginning of range
    x = x_min

    #loop to place points on graph
    for i in range(150):

        #y= ax^2+bx+c
        y = (a*(x**2)) + (b*x) + c

        # add x values to list
        x_values.append(x)

        # add y values to list
        y_values.append(y)

        # move x by one graph point
        x = x + graph_point

    # plot x and y values
    plt.plot(x_values, y_values)

    # graph labels
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Quadratic Function")

    #show plot
    plt.show()
