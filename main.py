
def is_palindrome (text):
    return text[::-1] == text
while True:
    text = input("Enter your text: ")
    print(f"{is_palindrome(text)} is palindrome" if is_palindrome(text) else "Not palindrome")
#assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
#assert is_palindrome('0P') == False, 'Test2'
#assert is_palindrome('a.') == True, 'Test3'
#assert is_palindrome('aurora') == False, 'Test4'
#print("ОК")


