phrase = "This is a regular text"

print(phrase.startswith('This is'))
print(phrase.startswith('text'))
print(phrase.startswith('regular', 10))
print(phrase.startswith('regular', 10, 22))
print(phrase.startswith('regular', 10, 15))

#Checking multiple strings at a time
print(phrase.startswith(('regular', 'This')))
print(phrase.startswith(('regular', 'text')))
print(phrase.startswith(('regular', 'text'), 10, 22))