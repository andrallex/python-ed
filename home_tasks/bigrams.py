import re
from nltk import ngrams

text = "Анализ данных, помогает извлекать полезную, информацию из данных."
#text = 'мама мыла раму мама мыла'
words = re.findall(r'\w+', text.lower())
print('The list of words: ', words)

# 1) without using ngrams
odd_index = [i for i, x in enumerate(words) if i % 2 == 1]
list_of_tupples = []
for i in odd_index:
    list_of_tupples.append((words[i-1], words[i]))
    if i < len(words) - 1:
        list_of_tupples.append((words[i], words[i+1]))
        
print('The list of tuples without using ngrams: ', list_of_tupples)        
        
# 2) using ngrams        
ngr = ngrams(words, 2)
bigrams = list(ngrams(words, 2))
print('The list of tuples with bigrams: ', bigrams)

    



