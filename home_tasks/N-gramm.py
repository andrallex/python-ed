import re

#text = 'мама мыла раму мама мыла'
file_path = '/home/andrallex/lingua-latina/text.txt' # указать путь к своему файлу с текстом
file_ref = open(file_path, 'r')
text = file_ref.read()
file_ref.close()

list_of_words = re.findall(r'\w+', text.lower())
print(list_of_words)

dict1 = {}
for index in range(len(list_of_words)-1):
    if index == 0:
        fw = list_of_words[index]
        sw = list_of_words[index+1]
        dict1[fw] = sw
        key_list = [fw, sw]
    else:
        sw = list_of_words[index+1]
        dict1[tuple(key_list)] = sw
        key_list.append(sw)
  
print(dict1)



 



    


#

