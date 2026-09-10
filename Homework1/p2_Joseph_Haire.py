# function to find Pythagorean triples
def find_Pythagorean(n):

    #list to store triples
    triples = []

    # possible triples for a
    for a in range(1, n + 1):

        #possible triples for b
        for b in range(1, n + 1):

            # possible triples for c
            for c in range(1, n + 1):

                # check if a b and c are in the right order
                if 0 < a < b < c: 

                    #pythag formula
                    if a**2 + b**2 == c**2:

                        #add triple to list
                        triples.append((a,b,c))

    #return list
    return triples

# ask user for input of positive integers
n = int(input("Enter a possitive integer: "))

#call function and pass n as argument
answer = find_Pythagorean(n)

# show all possible triples
for triple in answer:
    print(triple)