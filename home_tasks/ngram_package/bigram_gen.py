from read_and_split import read_input_file, prepare_text
from ngrams_model import create_bigram_dict, generate_text


#text = "Анализ данных, помогает извлекать полезную, информацию из анализ данных."
#text = read_input_file("/home/andrallex/python-ed/home_tasks/ngram_package/input_text_file.txt")
text = read_input_file("/home/andrallex/python-ed/home_tasks/ngram_package/pushkin_onegin.txt")

list_of_words = prepare_text(text)
print(list_of_words)

bigram_dict = create_bigram_dict(list_of_words)
print(bigram_dict)

start_word = "дядя"
num_words = 50
gen_text = generate_text(bigram_dict, start_word, num_words)
print(gen_text)
