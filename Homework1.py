
largest_str = ""
for phrase in range(5):
    input_str = input("Write a string")
    if len(input_str) > len(largest_str):
        largest_str = input_str
print(largest_str)