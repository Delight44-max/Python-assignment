import random 

numbers = []  


for count in range(10):
    num = random.randint(1, 50)  
    numbers.append(num)          

print("Random numbers:", numbers)

count = 0
for _ in numbers:  
    count += 1
print("Length of list:", count)

sum_even_pos = 0
for i in range(0, count, 2):  
    sum_even_pos += numbers[i]
print("Sum of elements at even positions:", sum_even_pos)

sum_odd_pos = 0
for i in range(1, count, 2):
    sum_odd_pos += numbers[i]
print("Sum of elements at odd positions:", sum_odd_pos)



product_third_pos = 1
for i in range(2, count, 3):  
    product_third_pos *= numbers[i]
print("Product of elements at every third position:", product_third_pos)


total_sum = 0
for num in numbers:
    total_sum += num
average = total_sum / count
print("Average of elements:", average)


largest = numbers[0] 
for num in numbers:
    if num > largest:
        largest = num
print("Largest element:", largest)



smallest = numbers[0] 
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest element:", smallest)


string_list = ["aba", "xyz", "aa", "abc", "1221"]

result_strings = []
for word in string_list:
    if len(word) >= 2 and word[0] == word[-1]:
        result_strings.append(word)

print("Matching strings:", result_strings)
print("Count:", len(result_strings))



seq_list = []
for i in range(1, 16):
    seq_list.append(i)
print("Sequential list:", seq_list)


dup_list = []
for num in seq_list:
    dup_list.append(num)
    dup_list.append(num) 
print("Duplicated list:", dup_list)


no_dup_list = []
for num in dup_list:
    if num not in no_dup_list:
        no_dup_list.append(num)
print("Without duplicates:", no_dup_list)



































