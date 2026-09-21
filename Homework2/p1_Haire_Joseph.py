def line_number(f1: str, f2: str) -> None:
    """Reads one file and writes its lines, with line numbers, to another file"""

    try:
        with open(f1, "r") as file: #open file to read from
            with open(f2, "w") as new_file: # open file to write to

                line_num = 1
                for line in file:
                    new_file.write(str(line_num) + ". " + line) #write numbered lines to new file
                    line_num += 1

    except:
        print("An error occurred attempting to access files.")
        raise

def parse_functions(f3: str) -> tuple:
    """Reads a python file, and gathers information on all functions"""

    try:
        with open(f3, "r") as file: #open file to read from

            lines     = file.readlines() #read all lines into a list
            functions = [] #list to hold function information
            
            for i in range(len(lines)):
                if lines[i].startswith("def "):
                    line          = lines[i]
                    function_code = lines[i]
                    

                    #find function name
                    start         = 4
                    end           = line.find("(")
                    function_name = line[start:end]

                    #find function arguments
                    close_parenthesis = line.find(")")
                    arguments         = line[end + 1: close_parenthesis] 

                    #find function body
                    j = i + 1
                    while j < len(lines):
                        if lines[j].strip() == "": #skip blank lines
                            j += 1
                            continue

                        if not lines[j].startswith(" "):
                            if not lines[j].startswith("\t"):
                                break

                        if lines[j].strip().startswith("#"): #skip comments
                            j += 1
                            continue

                        current_line = lines[j]

                        if "#" in current_line: #remove comments
                            comment_start = current_line.find("#")
                            current_line = current_line[:comment_start]
                            current_line = current_line.rstrip()
                            current_line = current_line + "\n"

                        function_code += current_line
                        j += 1

                    function_info = (function_name, i + 1, arguments, function_code) # place information into a tuple
                    functions.append(function_info)
                

            functions.sort() #sort functions by function name
            sorted_functions = []

            for item in functions: #rearrange for assignment specifications
                new_item = (item[1], item[0], item[2], item[3])
                sorted_functions.append(new_item)

            return tuple(sorted_functions)

    except:
        print("An error occurred while parsing the file.")
        raise

def main():

    line_number("p1_Haire_Joseph.py", "p1_Haire_Joseph.py.txt")
    print(parse_functions("p1_Haire_Joseph.py"))

main()
