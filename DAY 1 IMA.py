#!/usr/bin/env python
# coding: utf-8

# #Exercise 1: Write a function that will take in a string parameter and return a string in its 
# equivalent Morse code.

# In[1]:


dict = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'.....'}
def morse(text):
    
    morse_code = ""
    text = text.upper()
    for letter in text:
        morse_code += dict[letter] + " "
    return(morse_code)
print(morse("Hello World"))


# #Exercise 2: Write a function that takes in a string parameter and returns a list and a count 
# of the unique letters in the string.

# In[2]:


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def unique_english_letters(word):
    word = word.upper()
    word_list=[]
    uniques = 0
    for letter in word:
        if letter not in word_list and letter in LETTERS:
            word_list.append(letter)
            uniques +=1
        else:
            pass
    return word_list,uniques

print(unique_english_letters("Hello World"))


# #Exercise3: Write a function that accepts a string and prints to screen the number of uppercase letters and lowercase letters.

# In[3]:


def unique_letters(word):
    stri_up=0
    stri_lo=0
    for letter in word:
        if letter.isupper():
            stri_up+=1
        elif letter.islower():
            stri_lo+=1
        else:
            pass
    return f"Uppercase: {stri_up}, Lowercase: {stri_lo}"


# In[4]:


test = unique_letters("Hello World")


# In[5]:


print(test)


# In[ ]:




