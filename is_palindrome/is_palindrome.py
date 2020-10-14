def is_palindrome(s):
    s = s.lower()
    s=s.replace(" ", "")
    res = True
    pos=0
    while pos<len(s)/2:
        print(s[pos], s[len(s)-pos-1])
        if s[pos]!=s[len(s)-pos-1]:
            
            res = False
        pos+=1
    return res



# take the input
to_check = input("Enter a string without numbers: ")

# get the result
print(is_palindrome(to_check))