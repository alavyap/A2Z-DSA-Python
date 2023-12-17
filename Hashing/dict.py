# here i have solved problems for dictionary

'''
Problem 1
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1} 
'''

def count_word_frequency(words):
    count ={}
    for i in  (words):
        count[i] = count.get(i,0)+ 1
    return count
   
print(count_word_frequency( ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] ))
        
        
# Problem 2

'''

Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''
def merge_dict(dict1,dict2):
    result = {}
    result = dict1.copy()
    for key,value in dict2.items():
        result[key] = result.get(key,0) + value
    
    return result


print(merge_dict( {'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))


#Problem 3

'''
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b

'''

def max_value_key(my_dict):
    # maxV= max(my_dict,key = lambda k:my_dict[k])
    
    return max(my_dict,key = my_dict.get)
print(max_value_key({'a': 5, 'b': 9, 'c': 2}))


# Problem 4 
'''
Reverse Key-Value Pairs
Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
Output:

{1: 'a', 2: 'b', 3: 'c'}

'''

def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}


print(reverse_dict( {'a': 1, 'b': 2, 'c': 3}))


# Problem 5
'''

Conditional Filter
Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
Output:

{'b': 2, 'd': 4}
'''

def filter_dict(my_dict,condition):
   return {k:v for k, v in my_dict.items() if condition(k,v)}
        
# print(filter_dict( {'a': 1, 'b': 2, 'c': 3, 'd': 4} ))


# Problem 6
'''
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False
'''

def check_same_frequency(list1,list2):
    for i in range (len(list2)):
        if list1[i] == list2[i]:
            return True
    return False


print(check_same_frequency( [1, 2, 3, 2, 1],[3, 1, 2, 1, 3]))