import re
import random as rnd


text = "Анализ данных, помогает извлекать полезную, информацию из данных."

# Create the list of words
words = re.findall(r'\w+', text.lower())

print('The list of words: ', words)

# Create the list of tuples
odd_index = [i for i, x in enumerate(words) if i % 2 == 1]
list_of_tuples = []
for i in odd_index:
    list_of_tuples.append((words[i-1], words[i]))
    if i < len(words) - 1:
        list_of_tuples.append((words[i], words[i+1]))
    else:
        list_of_tuples.append((words[i], "END")) 
        
print('The list of tuples: ', list_of_tuples)          

# Create the bigram dictionary
word_dict = {}
for pair in list_of_tuples:
    if pair[0] not in word_dict:
        word_dict[pair[0]] = [pair[1]]
    else:
        word_dict[pair[0]].append(pair[1])
        
print('The dictionary: ', word_dict) 

# Generate a random text        
results = ["извлекать"]
for _ in range(100):
    possible_list = word_dict.get(results[-1],[])
    if not possible_list:
        break
    next_word = rnd.choice(possible_list)
    if next_word == "END":
        break
    results.append(next_word)
    
print('The text generated: ', " ".join(results))
            
    



