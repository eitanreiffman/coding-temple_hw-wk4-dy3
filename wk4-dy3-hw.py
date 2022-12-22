# Exercise 1:
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
same_words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_list(a_list, i1, i2, i3, i4, i5):
    a_list[i1], a_list[i2], a_list[i3], a_list[i4], a_list[i5] = a_list[i5], a_list[i4], a_list[i3], a_list[i2], a_list[i1]
    return a_list

def string_reversal(a_list, i1, i2, i3, i4, i5):
    a_list[i1], a_list[i2], a_list[i3], a_list[i4], a_list[i5] = a_list[i5], a_list[i4][::-1], a_list[i3], a_list[i2][::-1], a_list[i1][::-1]
    return a_list

print("Before The Sort:")
print(words)
print("="*50)
reverse_list(words, 0, 1, 2, 3, 4)
print("After The Sort:")
print(words)
string_reversal(same_words, 0, 1, 2, 3, 4)
print("="*50)
print("With Reversed Strings:")
print(same_words)


# Exercise 2:
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary
# with the words as the key and the value as the amount of times that word appears in the string.
# Example Output: {'in': 1, 'computing': 1, 'a': 5, ...}

import re

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_counter(long_text):
    word_dict = {}
    pattern_search = re.compile("\w+")
    find_words = pattern_search.findall(long_text.lower())
    # print(find_words)
    print("\nHere is our official tally of words and their count:\n")
    for word in find_words:
        word_count = find_words.count(word)
        if word not in word_dict:
            word_dict[word] = word_count
            print(f"\t{word} : {word_dict[word]}\n")

word_counter(a_text)

# Exercise 3:
# Write a function implementing a Linear Search Algorithm.
# A linear search is a method for finding an element within a list.
# It sequentially checks each element of the list until a match is found or the whole list has been searched.
# If you do not find a match, return -1
# If number is not present return -1

nums_list = [10,23,45,11,15,87,70,64]
target = 70
index = 0

def find_num(our_list, target_num, our_index):
    if our_list[our_index] == target_num:
        print(f"\nThe number {target_num} is at index {our_index}!\n")
    else:
        if our_list[our_index] == our_list[-1]:
            print(-1)
        else:
            our_index += 1
            find_num(our_list, target_num, our_index)
    return our_list

find_num(nums_list, target, index)


# def find_num(our_list, target_num):
#     # for index, num in enumerate(our_list):
#     if our_list[0] == target_num:
#         print(f"\nThe number {target_num} is in the list!\n")
#     else:
#         our_list.remove(our_list[0])
#         if len(our_list) != 0:
#             find_num(our_list, target_num)            
#         else:
#             return -1       

# find_num(nums_list, target)