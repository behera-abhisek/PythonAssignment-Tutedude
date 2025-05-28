
file = open('sample.txt','r')
read = file.readline()
read1 =file.readline()
read2 =file.readline()
print(read+read1+read2)
file.close()


with open('sample.txt', 'r') as file:
    read = file.read()
    print("\n")
    print(read)

try:
    file = open("sample1.txt","r")
    read = file.readlines()
    print(read)
    file.close()
except FileNotFoundError:
    print("\n")
    print("Error: The file 'sample1.txt' was not found")
