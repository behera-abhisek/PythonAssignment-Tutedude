start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
total = 0
for number in range(start_num,end_num+1):
    #total = total + number
    total += number
print("The sum of the numbers from", start_num, "to", end_num, "is", total)