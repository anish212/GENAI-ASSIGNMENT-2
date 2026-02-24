def analyze_text(text):
    words = text.split()
    word_count = len(words)
    
    vowels = 0
    for char in text.lower():
        if char in "aeiou":
            vowels = vowels + 1
            
    print("Words:", word_count)
    print("Vowels:", vowels)
    print("Reversed:", text[::-1])

user_text = input("Enter text: ")
analyze_text(user_text)