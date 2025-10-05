#WAP to check if a list contains a palindrome of elements.

#palindrome
list1 = ["m","o","m"]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
    
#not palindrome
list2 = ["m","u","m","m","y"]
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")