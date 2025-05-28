
file = open('output.txt','w')
write_file=str(input("Enter text to write to the file: "))
write= file.write(write_file+"\n")
print("Data successfully written to output.txt")
file.close()
file = open('output.txt','a')
append_file=str(input("Enter additional text to append: "))
append= file.write(append_file)
print("Data successfully appended.")
file.close()

with open('output.txt', 'r') as file:
    read = file.read()
    print("\n")
    print("Final content of the output.txt:")
    print(read)

