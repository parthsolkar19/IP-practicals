# Q1
text = "Python"

print("String:", text)
print("First character:", text[0])
print("Second character:", text[1])
print("Third character:", text[len(text) // 2])


# Q2
text = "Programming"

print("First 5 characters:", text[:5])
print("Last 4 characters:", text[-4:])
print("Substring (2 to 7):", text[2:8])


# Q3
text = "Assignment"

print("Alternate characters:", text[::2])
print("Reverse string:", text[::-1])


# Q4
text = "Python"

# new_text = text[0] = "J"  # This causes an error

new_text = "J" + text[1:]
print(new_text)


# Q5
text = "Python Programming"

if "Python" in text:
    print("Substring found")
else:
    print("Substring not found")

if "Java" not in text:
    print("Java is not present")


# Q6
text = "Python Programming"

print(text.find("Programming"))
print(text.find("Java"))
print(text.index("Python"))


# Q7
text = "banana"

print("Count of 'a':", text.count("a"))
print("Count of 'na':", text.count("na"))


# Q8
text = "Python Programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())


# Q9
text = "  Hello Python  "
print("Strip:", text.strip())

sentence = "I like Java"
print(sentence.replace("Java", "Python"))

name = "Rahul"
marks = 90

print(f"{name} scored {marks} marks")


# Q10
sentence = "Python is easy to learn"

words = sentence.split()
print(words)

joined = "-".join(words)
print(joined)


# Q11
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q12
paragraph = input("Enter a paragraph: ")

words = paragraph.split()

print("Word count:", len(words))
print("Character count:", len(paragraph))

frequency = {}

for word in words:
    word = word.lower()

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_word = max(frequency, key=frequency.get)

print("Most frequent word:", most_word)
print("Frequency:", frequency[most_word])