#Palindrome using Recursion
def Palindrome(word,n,i):
    #if a single letter
    if i==n//2:
        return True
    #if word at first place in array equal to word at equivalent last pace in array
    elif word[i]==word[(-i-1)]:
        return Palindrome(word,n,i+1)
    else:
        return False


given_word='nniittiinn'
Check_word=Palindrome(given_word, len(given_word), 0)
if Check_word==True:
    print("word is palindrome")
else:
    print("False")