file_name = "binaryTodecimal.py"
 
python_file = open(file_name,'r')
count = 0
 
for line in python_file:
    count += len(line.split())
print(count)