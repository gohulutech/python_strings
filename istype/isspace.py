# Checks if all characters are white spaces.
text = ' '
print(text.isspace())

text = ' \f\n\r\t\v'
print(text.isspace())

text = '            '
print(text.isspace())

text = ''
print(text.isspace())

text = 'This is a regular text'
print(text.isspace())
