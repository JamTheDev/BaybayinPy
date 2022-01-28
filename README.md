# BaybayinPy
 An Open-Source, free to use python library used to convert tagalog into **baybayin**, a writing system native to the Philippines, attested from before Spanish colonization through to at least the eighteenth century.
 
 # Cloning
 
 ```
  git clone https://github.com/JamTheDev/BaybayinPy
 ```
 
# How to use it?
```py
# Import The Library
from BConv import TagToBaybayin

# Create a new object
converter = TagToBaybayin()

# Input string (Must be in tagalog)
str1 = "Kamusta ka, kaibigan?" # How are you, friend?

# Call the converter instance and convert the string
converted_str = converter.convert(str1)

# Output
print(converted_str)
```
