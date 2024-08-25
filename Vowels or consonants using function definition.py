def is_vowel(char):
    vowels  = 'aeiouAEIOU'
    if char in vowels :
        return True 
    else  :
        return False 
def is_consonant(char):
    consonants  = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    if char in consonants :
        return True 
    else  :
        return False 

char = input("Enter the alphabet : ")

if is_vowel(char):
    print(char ," is a vowel") 
elif is_consonant(char) :
    print(char," is a consonant") 
else :
    print(char," is neither a vowel nor a consonent")  
    

