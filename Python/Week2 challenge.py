# Create a list of integers
numbers = list(map(int, input("Enter integers separated by space: ").split()))
# Compute the sum
print("The sum of all integers is:", sum(numbers))

# Tuple of favorite books
books = ("1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby", "Moby Dick")

# Print each book on a separate line
for book in books:
    print(book)

    # Dictionary to store information
person = {}

# Collect user input
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("Person's information:", person)

# Create two sets from user input
set1 = set(map(int, input("Enter integers for the first set separated by space: ").split()))
set2 = set(map(int, input("Enter integers for the second set separated by space: ").split()))

# Find common elements
common_set = set1.intersection(set2)
print("Common elements:", common_set)

# List of words
words = ["apple", "banana", "kiwi", "orange", "pear"]

# List comprehension to filter words with an odd number of characters
odd_char_words = [word for word in words if len(word) % 2 != 0]

print("Words with an odd number of characters:", odd_char_words)