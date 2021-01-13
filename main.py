# Sort user inputed list
print("Enter words separated by spaces")
user_list = input()

# Takes user input and splits it to get access to individual list items
list_to_sort = user_list.split()
print(list_to_sort)
print("\n")

# Get length of input
list_len = len(list_to_sort)

for i in range(list_len-1): 
  
  for j in range(0, list_len-i-1): 
    # Traverse array from 0 to n-i-1 
    # Swap if greater than next 
    if list_to_sort[j] > list_to_sort[j+1] : 
      list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j] 

print(list_to_sort)