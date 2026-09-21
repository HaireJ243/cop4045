#part a 
tuples = [
    (a, b, c, d)
    for a in range(1, 11)
    for b in range(1, 11)
    for c in range(1, 11)
    for d in range(1, 11)
    if len({a, b, c, d}) == 4 and a**2 + b**2 == c**2 + d**2
]

print("Part A\n", tuples, "\n")


#part b
str_lst = ['One', 'SEVEN', 'three', 'two', 'Ten']

lst = [(str.lower(), len(str)) for str in str_lst if len(str) < 5]
print("Part B\n", lst, "\n")


#part c
names = ['Christopher Ashton Kitcher', 'Elizabeth Stamatina Fey']

full_name_format = [ # first M. Last
    name.split()[0] + " " + name.split()[1][0] + ". " + # [1] = middle name [0] = first letter of middle name
    name.split()[2] for name in names]

print("Part C\n", full_name_format, "\n")


#part d
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

tup_lst = [(str1, str2) for str1 in lst1 for str2 in lst2
           if sorted(str1.lower()) == sorted(str2.lower())]
print("Part D\n", tup_lst, "\n")


#part e
s = ['one', 'two', 'three']

d = {str: len(str) for str in s}
print("Part E\n", d, "\n")


#part f
text = "Hello world"

d2 = {i:c for i, c in enumerate(text)
     if c.lower() in "aeiou"}
print("Part F\n", d2)