from collections import Counter, defaultdict
import random as rnd


# Create bigram dictionary and count the number of occurences of words
def create_bigram_dict(word_list: list) -> dict:
    bigram_dict = defaultdict(Counter)
    for i in range(len(word_list) - 1):
        bigram_dict[word_list[i]][word_list[i+1]] += 1
        
    return bigram_dict 


# Generate text using the number of occurences of words for random choice
def generate_text(bigram_dict: dict, start_word: str, num_words: int=10):
    current_word = start_word
    result = [current_word]
    for _ in range(num_words-1):
        if current_word not in bigram_dict:
            break
        next_word = rnd.choices(list(bigram_dict[current_word].keys()), 
                               weights=bigram_dict[current_word].values())[0]
        result.append(next_word)
        current_word = next_word
        
    return ' '.join(result)

      
