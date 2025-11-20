import sys 
    #check if correct number of argumnets 
if len(sys.argv) == 3:
    script_name=sys.argv[0]
    name=sys.argv[1]
    rollno=sys.argv[2]
else:
   script_name=sys.argv[0]
   name = "snehalata"
   rollno = "179"
   print("No input given -using default values:")
  #printing statements
print("script Name:",script_name)
print("student Name:",name)
print("Roll Number:",rollno)
