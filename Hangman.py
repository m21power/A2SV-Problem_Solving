word='MESAY' #u can use random word  generator instead
import string
def hangman():
    word_letters=set(word) 
    
    alphabet=set(string.ascii_uppercase)
    used_letters=set() 
    
    lives=6
    while len(word_letters)>0 and lives >0:
        
        print("you have ",lives," lives left and you have used these letters: ",''.join(used_letters))
        
        word_list=[]
        for letters in word:
            if letters in used_letters:
                word_list.append(letters)
            else:
                word_list.append('-')
        print('current word: ',' '.join(word_list))
        user_letter=input('guess letter: ').upper()
        
        if user_letter in (alphabet - used_letters):
        #if user letter is in (the difference between the two sets)-->
        #alphabet minus used letters == the letter only found in alphabet
            
            used_letters.add(user_letter)
            #check for if user letter is in word lettersm

            #else your lives will drop by one 
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1 #takes away a life
                print('the letter is not in a word.')
        elif user_letter in used_letters:
            print('you have already used that! ')
        else:
            print("wrong character! ")
    if lives==0:
        print('you lost! ')
    else:
        print('you win! ')
        
         

hangman()

 
