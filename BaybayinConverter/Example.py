# Import The Library
from BConv import TagToBaybayin

# Create a new object
converter = TagToBaybayin()

# Input (Must be in tagalog)
str1 = "Kamusta ka, kaibigan?" # How are you, friend?

# Convert
converted_str = converter.convert(str1)

# Output
print(converted_str)