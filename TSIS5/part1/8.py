def longest_words(file_name):
    with open(file_name, 'r') as f:
        words = f.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_words('test.txt'))