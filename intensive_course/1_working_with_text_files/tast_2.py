import re


# Читаем текст из файла
path = '/home/andrallex/python-ed/intensive_course/1_working_with_text_files/text_for_task_2.txt'
in_file = open(path, 'r', encoding = 'utf-8')
in_text = in_file.read()
in_file.close()

# Любые законченные предложения оканчиваются следующими знаками препинания: "."("..."), "?", "!"
sentences = re.split(r'[.!?]+', in_text)
split_sentences = [sent.strip().split() for sent in sentences if sent.strip().split()]
split_sentences.sort(key=len)
sentence_and_number_maps = [{" ".join(sent): len(sent)} for sent in split_sentences]
max_len_sentence = " ".join(split_sentences[-1])

print(f'Исходный текст из файла: {in_text}')
print(f'Исходные предложения: {sentences}')
print(f'Предложения разбитые по словам: {split_sentences}')
print(f'Предложения с указанием количества слов: {sentence_and_number_maps}')
print(f'Предложение с наибольшим количеством слов: {max_len_sentence}')

