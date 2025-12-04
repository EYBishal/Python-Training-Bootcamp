LIST – Exercises (5)

Exercise 1
Given a list of integers, rearrange the list so that all negative numbers appear first and all positive
numbers appear later, without using additional predefined functions like sort().
  
def rearrange_neg_pos(lst):
    negatives = []
    non_negatives = []
    for x in lst:
        if x < 0:
            negatives.append(x)
        else:
            non_negatives.append(x)
    return negatives + non_negatives


print(rearrange_neg_pos([3, -1, 0, -7, 2, -5])) 


Exercise 2
Given a list, create a new list that contains only those elements which appear more than once. Do not
use set().


def duplicates_only(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1

    result = []
    added = [] 
    for x in lst:
        if freq[x] > 1 and x not in added:
            result.append(x)
            added.append(x)
    return result


print(duplicates_only([1, 2, 3, 2, 4, 1, 5, 1])) 


Exercise 3
Rotate a list to the left by N positions using only loops.


def rotate_left(lst, n):
    if not lst:
        return lst
    n = n % len(lst) 
    for _ in range(n):
        first = lst[0]
        for i in range(len(lst) - 1):
            lst[i] = lst[i + 1]
        lst[-1] = first
    return lst


print(rotate_left([1, 2, 3, 4, 5], 2))  


Exercise 4
Given a list of strings, remove all strings whose length is less than 3.


def remove_short_strings(strings):
    result = []
    for s in strings:
        if isinstance(s, str) and len(s) >= 3:
            result.append(s)
    return result


print(remove_short_strings(["a", "ab", "abc", "hello", "", "go"])) 


Exercise 5
Flatten a nested list using loops only.


def flatten_nested_list(nested):
    flat = []
    stack = [nested]  
    while stack:
        current = stack.pop()
        
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            flat.append(current)
    flat.reverse()
    return flat


print(flatten_nested_list([[1, 2], [3, 4], [5]]))  


TUPLE – Exercises (5)

Exercise 1
Given a tuple containing both numbers and strings, separate them into two tuples: one containing only
numbers and one containing only strings.


def separate_numbers_strings(tpl):
    nums = []
    strs = []
    for x in tpl:
        if isinstance(x, (int, float)):
            nums.append(x)
        elif isinstance(x, str):
            strs.append(x)
    return tuple(nums), tuple(strs)


print(separate_numbers_strings((10, "apple", 3.5, "banana"))) 


Exercise 2
Given a tuple of numbers, determine whether it is strictly increasing.


def is_strictly_increasing(tpl):
    if len(tpl) < 2:
        return True
    for i in range(1, len(tpl)):
        if tpl[i] <= tpl[i - 1]:
            return False
    return True


print(is_strictly_increasing((1, 2, 3, 4))) 
print(is_strictly_increasing((1, 2, 2, 3))) 


Exercise 3
Create a tuple of words and return a new tuple where each word is reversed.


def reverse_words_tuple(tpl):
    result = []
    for w in tpl:
        result.append(w[::-1])
    return tuple(result)


print(reverse_words_tuple(("python", "cloud", "data"))) 


Exercise 4
Write a program to find the index positions of a given value inside a tuple, without using index().


def indices_of_value(tpl, value):
    positions = []
    i = 0
    for x in tpl:
        if x == value:
            positions.append(i)
        i += 1
    return positions


print(indices_of_value((1, 2, 3, 2, 4, 2), 2))


Exercise 5
Given a tuple (10, (20, 30), (40, (50, 60))), print all integers using recursion.


def print_integers_recursive(t):
    if isinstance(t, tuple):
        for item in t:
            print_integers_recursive(item)
    else:
        if isinstance(t, int):
            print(t)


print_integers_recursive((10, (20, 30), (40, (50, 60))))



SET – Exercises (5)

Exercise 1
Given two sets, print the elements that are present in the union but not in the intersection.
(Equivalent to symmetric difference but do not use ^.)


def union_minus_intersection(a, b):
    result = set()
    for x in a:
        if x not in b:
            result.add(x)
    for y in b:
        if y not in a:
            result.add(y)
    return result


print(union_minus_intersection({1, 2, 3}, {3, 4})) 


Exercise 2
Given a list with duplicates, convert it to a set and then back to a list, preserving the original order of
first occurrences.


def list_to_set_back_preserve_order(lst):
    seen = set()
    ordered_unique = []
    for x in lst:
        if x not in seen:
            ordered_unique.append(x)
            seen.add(x)
    return ordered_unique


print(list_to_set_back_preserve_order([3, 1, 3, 2, 1, 4])) 


Exercise 3
Given a set of numbers, find all pairs that sum up to a target number.


def pairs_with_sum(s, target):
    pairs = []
    for x in s:
        y = target - x
        if y in s and x <= y:
            pairs.append((x, y))
    return pairs


print(pairs_with_sum({2, 4, 6, 8, 10}, 12)) 


Exercise 4
Check whether two sets are disjoint without using the built-in method.


def are_disjoint(a, b):
    for x in a:
        if x in b:
            return False
    return True


print(are_disjoint({1, 2}, {3, 4}))  
print(are_disjoint({1, 2}, {2, 3})) 


Exercise 5
Given a list of words, find all unique characters across all words combined, using sets.


def unique_chars(words):
    chars = set()
    for w in words:
        for ch in w:
            chars.add(ch)
    return chars

print(unique_chars(["apple", "banana"]))  


DICTIONARY – Exercises (5)

Exercise 1
Given a dictionary of student marks:
{"A": 85, "B": 92, "C": 78, "D": 92}
Print all keys that have the maximum value without using max().

def keys_with_max_value(d):
    first = True
    max_val = None
    for k in d:
        v = d[k]
        if first:
            max_val = v
            first = False
        else:
            if v > max_val:
                max_val = v
    
    result = []
    for k in d:
        if d[k] == max_val:
            result.append(k)
    return result


marks = {"A": 85, "B": 92, "C": 78, "D": 92}
print(keys_with_max_value(marks)) 


Exercise 2
Invert a dictionary (swap key and value). If duplicate values exist, group keys into a list.


def invert_dict_group(d):
    inv = {}
    for k in d:
        v = d[k]
        if v in inv:
            inv[v].append(k)
        else:
            inv[v] = [k]
    return inv


print(invert_dict_group({"a": 1, "b": 2, "c": 1}))


Exercise 3
Merge two dictionaries, but if a key appears in both, store the values in a list.


def merge_with_lists(d1, d2):
    merged = {}
   
    for k in d1:
        merged[k] = d1[k]
    
    for k in d2:
        if k in merged:
            merged[k] = [merged[k], d2[k]]
        else:
            merged[k] = d2[k]
    return merged


print(merge_with_lists({"a": 1, "b": 2}, {"b": 3, "c": 4})) 


Exercise 4
Given a dictionary representing items and prices, remove all items whose price is below 100.


def remove_below_100(prices):
    filtered = {}
    for item in prices:
        if prices[item] >= 100:
            filtered[item] = prices[item]
    return filtered


print(remove_below_100({"pen": 25, "bag": 450, "notebook": 80})) 


Exercise 5
Given a nested dictionary of employees, count how many employees belong to each department.


def count_by_department(employees):
    counts = {}
    for emp_id in employees:
        dept = employees[emp_id].get("dept")
        if dept is not None:
            if dept in counts:
                counts[dept] += 1
            else:
                counts[dept] = 1
    return counts


data = {
    "e1": {"dept": "IT"},
    "e2": {"dept": "HR"},
    "e3": {"dept": "IT"},
}
print(count_by_department(data)) 
