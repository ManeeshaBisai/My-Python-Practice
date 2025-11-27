def is_palindrome(n):
    original = n
    reverse = 0
    
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    
    if original == reverse:
        return True
    else:
        return False

# Input
num = int(input("Enter a number: "))

# Output
if is_palindrome(num):
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")
