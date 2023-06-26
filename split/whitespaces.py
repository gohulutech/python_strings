my_phrase = "let's go to the beach"
my_words = my_phrase.split(" ")

for word in my_words:
    print(word)

print(my_words)

# By default the split method splits by whitespaces so there is no need
# to send the whitespace as a parameter.
my_words = my_phrase.split();
for word in my_words:
    print(word)