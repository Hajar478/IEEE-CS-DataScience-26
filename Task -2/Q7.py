file_path = "D://downloads//simple_text"

with open(file_path, "r") as file:
    text = file.read()

words = text.split()
long_words_count = sum(1 for word in words if len(word) > 5)

print( long_words_count)

