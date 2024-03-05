def contains_alphabet(word):
    for char in word:
        if char.isalpha():
            return True
    return False

# Example usage:
word1 = "12345"
word2 = "Hello123"

result1 = contains_alphabet(word1)
result2 = contains_alphabet(word2)

print(f"{word1}: {result1}")
print(f"{word2}: {result2}")
