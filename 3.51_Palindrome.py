""" Write a Python function that checks whether a passed string is
palindrome or not. """

def isPalindrome(string): 
    if (string == string[::-1]) : 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 
 
#Enter input string 
string = input ("Enter string: ") 
 
print(isPalindrome(string))
