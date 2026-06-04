def strings_to_ints(str_nums):
    # str -> int, for each element
    # Example: ["1", "2", "3"] -> [1, 2, 3]
    # (You could write map(int, str_nums) here, but use a lambda instead.)
    return list(map(lambda x:int(x),str_nums))

def ints_to_strings(nums):
    # int -> str, for each element
    # Example: [1, 2, 3] -> ["1", "2", "3"]
    return list(map(lambda x:str(x),nums))

def square_all(nums):
    # n -> n squared
    # Example: [1, 2, 3, 4] -> [1, 4, 9, 16]
    return list(map(lambda x: x**2,nums))

def square_plus_one(nums):
    # n -> n squared + 1
    # Example: [1, 2, 3] -> [2, 5, 10]
    return list(map(lambda x: x**2+1,nums))

def add_exclamation(words):
    # word -> word + "!"
    # Example: ["hi", "hello"] -> ["hi!", "hello!"]
    return list(map(lambda x: x+"!",words))

def first_chars(words):
    # word -> first character of word
    # Example: ["apple", "banana"] -> ["a", "b"]
    return list(map(lambda x:x[0],words ))

def celsius_to_fahrenheit(temps):
    # c -> c * 9/5 + 32
    # Example: [0, 100] -> [32.0, 212.0]
    return list(map(lambda x:x*9/5+32,temps))

def fahrenheit_to_celsius(temps):
    # f -> (f - 32) * 5/9
    # Example: [32, 212] -> [0.0, 100.0]
    return list(map(lambda x:(x-32)*5/9,temps))


# Test your implementations
print(strings_to_ints(["1", "2", "3", "4"]))    # expected: [1, 2, 3, 4]
print(ints_to_strings([1, 2, 3, 4]))            # expected: ["1", "2", "3", "4"]
print(square_all([1, 2, 3, 4]))                 # expected: [1, 4, 9, 16]
print(square_plus_one([1, 2, 3]))               # expected: [2, 5, 10]
print(add_exclamation(["hi", "hello"]))         # expected: ["hi!", "hello!"]
print(first_chars(["apple", "banana", "cat"]))  # expected: ["a", "b", "c"]
print(celsius_to_fahrenheit([0, 100, 37]))      # expected: [32.0, 212.0, 98.6]
print(fahrenheit_to_celsius([32, 212, 98.6]))   # expected: [0.0, 100.0, 37.0]

# Try a few more cases on your own:
# - What happens if you pass an empty list?
# - What if every element is the same?
print(strings_to_ints([]))  
print(strings_to_ints(["5", "5", "5"]))
print(ints_to_strings([]))  
print(ints_to_strings([5, 5, 5]))    
print(square_all([]))
print(square_all([5,5,5,5,5]))
print(square_all([-1,-5,0]))
print(square_plus_one([]))
print(square_plus_one([5, 5, 5]))
print(square_plus_one([-5, -2, 0]))
print(add_exclamation([]))
print(add_exclamation(["thunder","spur"]))
print(first_chars([]))
print(first_chars(["kobe","bryant","k60"]))
print(celsius_to_fahrenheit([]))
print(celsius_to_fahrenheit([10,10,10]))
print(celsius_to_fahrenheit([-45,-20]))
print(fahrenheit_to_celsius([]))
print(fahrenheit_to_celsius([10,10,10]))
print(fahrenheit_to_celsius([-45,-20]))


