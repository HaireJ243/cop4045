# function to find duplicated substring
def find_dup_str(s, n):

    #if n is longer than str length return empty str
    if n > len(s) / 2:
        return ""

    # find start of first possible substring
    for i in range(len(s) - n +1):

        first = s[i: i + n] #slice string to find first substr

        #start 2nd substring after first to prevent overlap
        for j in range(i + n, len(s) - n + 1):

            second = s[j: j + n] # slice for 2nd substr

            #check if substr are equal
            if first == second:

                return first # return found substr

    return "" # if no dupe is found



#ask user for a str
s = input("Enter a string: ")

# ask for substr length as integer
n = int(input("Enter substring length: "))

#call find dupe function
answer = find_dup_str(s,n)

#print answer
print(answer)


#function to find longest duped substr
def find_max_dup(s):

    longest = "" # longest substr start empty

    # try every length of substr
    for n in range(1, len(s) + 1):

        #call find_dup_dtr()
        result = find_dup_str(s,n)

        # if duped substr is found
        if result != "":

            longest = result #new longest duped substr

    return longest

#ask user for string
s = input("Enter a string: ")

#call function
answer = find_max_dup(s)

#print answer
print(answer)