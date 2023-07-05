#"w" overwrites entire file
#"a" adds to the end of the file
#\n start the code on a new line
employee_file = open("index.html", "w")

employee_file.write("<p> This is HTML</p>")

employee_file.close()