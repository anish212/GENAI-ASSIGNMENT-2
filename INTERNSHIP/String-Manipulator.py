text = input("Enter a sentence: ")

words = text.split()

print("Original:", text)
print("Characters (with spaces):", len(text))
print("Characters (without spaces):", len(text.replace(" ", "")))
print("Words:", len(words))
print("UPPERCASE:", text.upper())
print("lowercase:", text.lower())
print("Title Case:", text.title())
print("First word:", words[0])
print("Last word:", words[-1])
print("Reversed:", text[::-1])