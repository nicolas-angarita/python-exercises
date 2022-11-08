#!/usr/bin/env python
# coding: utf-8

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise

# In[169]:



def is_two(x):
    return x == 2 or x == "2"



# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[172]:


def is_vowel(x):
   
    return  x in ['a', 'e', 'i', 'o', 'u']





# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.


def is_consonant(c):
    is_vowel = ['a', 'e', 'i', 'o', 'u']
    return c not in is_vowel



# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.


def my_word(x):
    is_vowel = 'aeiou'
    if x[0].lower() in is_vowel:
    
        print(x)
    
    else:   
        
        print(x.capitalize())
    


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.




def calculate_tip():
        bill_total = float(input('What is your bill total?: $'))
        tip_percent = float(input('What percent do you want to tip?: '))


        tip_amount = round(bill_total * (tip_percent/100), 2)

        print(f'Your total tip is ${tip_amount}')
    


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[192]:



def apply_discount(op, discount):
    
    discount = discount / 100
    
    total = op - (op * discount)
    
    print(total)




# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[201]:



def handle_commas(string):
        string = string.replace(",", "")
        return string




# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[21]:



grade = int(input('What is your number? '))

def get_letter_grade(x):
    
    
    if x >= 90: 
        print('A')
    
    elif x >= 80:
        print('B')
        
    elif x >= 70:
        print('C')
        
    elif x >= 60:
        print('D')
        
    else:
        print('F')
        
        
get_letter_grade(grade)


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[214]:





def remove_vowel(word):
    new_word = input("Please type a word: ")
    is_vowel = ('a', 'e', 'i', 'o', 'u')
    for x in word.lower():
        if x in is_vowel:
            word = word.replace(x,"")
            word = word.upper()
    print(word)        
    

    remove_vowel(new_word)


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#  - anything that is not a valid python identifier should be removed
#  - leading and trailing whitespace should be removed
#  - everything should be lowercase
#  - spaces should be replaced with underscores
# for example:
#  - Name will become name
#  - First Name will become first_name
#  - % Completed will become completed

# In[207]:


def normalize_name(string):
    string = string.replace("$", "")
    string = string.replace("%", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    string = string.replace(" ", "_")
    string = string.lower()
    
    return string




# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#  - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#  - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# 

# In[221]:



def cumulative_sum(nums):
    new_list = []
    x = 0
    for num in nums:
        x += num
    
        new_list.append(x)
     
    return (new_list)




if __name__ == '__main__':
    print('Hello, World!')

