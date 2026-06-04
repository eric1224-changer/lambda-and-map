def cube(x):
    # x -> x cubed
    return x ** 3

def is_positive(n):
    # n -> True if n > 0, else False
    return n > 0

def full_name(first, last):
    # (first, last) -> "first last"
    return first + " " + last

def is_even(n):
    # n -> True if n is even, else False
    return n % 2 == 0

def max_of_two(a, b):
    # (a, b) -> whichever is larger
    return a if a > b else b

def starts_with_vowel(word):
    # word -> True if word's first letter is a vowel (case-insensitive)
    return word[0].lower() in "aeiou"

cube_lambda = lambda x:x**3             # implement: same behavior as cube()
is_positive_lambda = lambda x:x>0       # implement: same behavior as is_positive()
full_name_lambda = lambda x,y:x+" "+y         # implement: same behavior as full_name()
is_even_lambda = lambda x:x%2 ==0           # implement: same behavior as is_even()
max_of_two_lambda = lambda x,y:x if x>y else y        # implement: same behavior as max_of_two()
starts_with_vowel_lambda = lambda x: x[0].lower()in"aeiou" # implement: same behavior as starts_with_vowel()


# Test your implementations
print(cube_lambda(3))                        # expected: 27
print(is_positive_lambda(-4))                # expected: False
print(full_name_lambda("Ada", "Lovelace"))   # expected: Ada Lovelace
print(is_even_lambda(10))                    # expected: True
print(max_of_two_lambda(7, 12))              # expected: 12
print(starts_with_vowel_lambda("apple"))     # expected: True
print(starts_with_vowel_lambda("banana"))    # expected: False

# Try a few more cases on your own:
# - Does full_name_lambda still work if one of the names is empty?
# - What does max_of_two_lambda return when both values are equal?
print(cube_lambda(0))  
print(cube_lambda(-4))  
print(is_positive_lambda(0)) 
print(is_positive_lambda(5)) 
print(full_name_lambda("", "Lovelace"))
print(full_name_lambda("Ada", ""))
print(full_name_lambda("", ""))
print(is_even_lambda(0))    
print(is_even_lambda(-4))    
print(is_even_lambda(7))   
print(max_of_two_lambda(7, 7))  
print(max_of_two_lambda(-7, -12)) 
print(starts_with_vowel_lambda("train"))   
print(starts_with_vowel_lambda("AAA"))   

