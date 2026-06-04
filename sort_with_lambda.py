def sort_by_last_char(words):
    # key: word -> last character of word
    # Sort alphabetically by last character.
    # Work out the expected result yourself before running the test.
    return sorted(words,key=lambda x:x[-1])

def sort_by_length(words):
    # key: word -> len(word)
    # Example: ["banana", "hi", "hello"] -> ["hi", "hello", "banana"]
    return sorted(words,key = lambda x:len(x))

def sort_students_by_grade(students):
    # students: list of (name, grade, age)
    # key: student -> grade (the second element)
    # Sort ascending.
    return sorted(students,key = lambda x:x[1])

def sort_students_by_age_desc(students):
    # students: list of (name, grade, age)
    # key: student -> age (the third element)
    # Sort descending (oldest first). Hint: sorted() takes a reverse=True argument.
    return sorted(students,key = lambda x:x[2],reverse =True)

def sort_by_distance_from_ten(nums):
    # key: n -> distance from 10 (i.e. abs(n - 10))
    # Example: [5, 12, 9, 20, 10] -> [10, 9, 12, 5, 20]
    return sorted(nums,key = lambda x:abs(x-10))

def sort_by_distance_from(nums, target):
    # key: n -> distance from target (i.e. abs(n - target))
    # Example: sort_by_distance_from([1, 5, 8, 3], 4) -> [3, 5, 1, 8]
    return sorted(nums,key = lambda x:(abs(x-target),x))


# Test your implementations
print(sort_by_last_char(["apple", "dog", "cat"]))
print(sort_by_length(["banana", "hi", "hello"]))   # expected: ["hi", "hello", "banana"]

students = [("Ada", 88, 16), ("Ben", 72, 17), ("Cleo", 95, 15)]
print(sort_students_by_grade(students))            # expected: sorted by grade ascending
print(sort_students_by_age_desc(students))         # expected: Ben (17), Ada (16), Cleo (15)

print(sort_by_distance_from_ten([5, 12, 9, 20, 10]))  # expected: [10, 9, 12, 5, 20]
print(sort_by_distance_from([1, 5, 8, 3], 4))         # expected: [3, 5, 1, 8]

# Try a few more cases on your own:
# - What if two students have the same grade?
# - What if the list is empty or has one element?
print(sort_by_last_char([]))
print(sort_by_length([]))
print(sort_students_by_grade([]))
print(sort_students_by_age_desc([]))
print(sort_by_distance_from_ten([]))
print(sort_by_distance_from([], 5))


print(sort_by_last_char(["wasd"]))
print(sort_by_length(["wasd"]))
print(sort_students_by_grade([("wasd", 80, 16)]))
print(sort_by_distance_from_ten([-4]))
print(sort_by_distance_from([7], 4))

students_same_grade = [("Alex", 85, 16), ("Kevin", 85, 19)]
print(sort_students_by_grade(students_same_grade))

print(sort_by_distance_from([5, 3], 4))       
print(sort_by_distance_from([9, 11], 10))     
print(sort_by_distance_from([-1, -5, 2], 0))
print(sort_by_distance_from_ten([0, 10, 20]))