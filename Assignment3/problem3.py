sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])
    
#sample output
#Enter a sentence: apple mango apple banana mango apple

#Word Frequency:
#apple : 3
#mango : 2
#banana : 1