import string

def word_frequency(sentence):
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator).lower()
    
    words = sentence.split()

    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
