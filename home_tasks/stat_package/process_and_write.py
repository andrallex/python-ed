from collections import Counter


# Count the number of occurences of words
def count_word_occurences(word_list: list) -> dict:
    word_occurences = Counter(word_list) 
    dict_word_occurences = {k:[v] for k,v in word_occurences.items()}
    return dict_word_occurences
  

# Count the number of occurences of the target words
def count_target_word_occurences(word_list: list, target_word_list: list) -> dict:
    word_counts_dict = count_word_occurences(word_list)
    return {word: word_counts_dict.get(word, 0) for word in target_word_list}


