import pandas as pd
import string
import re

doc1 = "Иван любит смотреть фильмы. Мария тоже любит фильмы."
doc2 = "Иван также любит смотреть футбольные матчи."
all_docs = doc1 + " " + doc2
print("all_docs: ", all_docs)

# Constructs the reference vector
def construct_reference_vector(all_docs):
    table = str.maketrans("", "", string.punctuation)
    all_docs_without_punctuation = all_docs.translate(table)
    all_docs_all_words_list = all_docs_without_punctuation.split(" ")
    all_docs_unic_words_list = list(set(all_docs_all_words_list))
    print("**************construct_reference_vector visual control**********************")
    print("all_docs_without_punctuation: ", all_docs_without_punctuation)
    print("all_docs_all_words_list: ", all_docs_all_words_list)
    print("all_docs_unic_words_list: ", all_docs_unic_words_list)

    index_dict = {}
    for i in range(len(all_docs_unic_words_list)):
        index_dict[all_docs_unic_words_list[i]] = len(re.findall(all_docs_unic_words_list[i], all_docs_without_punctuation))
        
    sorted_index_tuple = sorted(index_dict.items(), key=lambda item: item[1], reverse=True)
    print("sorted_index_tuple: ", sorted_index_tuple)
    return pd.DataFrame(sorted_index_tuple, columns=['All_words', "All_occurs"])  
       
# Constructs a document vector
def construct_doc_vector(doc):
    table = str.maketrans("", "", string.punctuation)
    doc_without_punctuation = doc.translate(table)
    doc_all_words_list = doc_without_punctuation.split(" ")
    doc_unic_words_list = list(set(doc_all_words_list))
    print("**************construct_doc_vector visual control***************************")
    print("doc_without_punctuation: ", doc_without_punctuation)
    print("doc_all_words_list: ", doc_all_words_list)
    print("doc_unic_words_list: ", doc_unic_words_list)

    index_dict = {}
    for i in range(len(doc_unic_words_list)):
        index_dict[doc_unic_words_list[i]] = len(re.findall(doc_unic_words_list[i], doc_without_punctuation))
        
    print("index_dict: ", index_dict)
    return index_dict  
   
def main():
    # 1. Building a reference vector
    d_frame = construct_reference_vector(all_docs)
    
    # 2. Appending the 1-st document vector
    doc_column_dict1 = construct_doc_vector(doc1)
    d_frame["Doc_occur1"] = d_frame["All_words"].map(doc_column_dict1)
    d_frame["Doc_occur1"] = d_frame["Doc_occur1"].fillna(0) # filling None values with zeros
     
    # 3. Appending the 2-d document vector
    doc_column_dict2 = construct_doc_vector(doc2)
    d_frame["Doc_occur2"] = d_frame["All_words"].map(doc_column_dict2)
    d_frame["Doc_occur2"] = d_frame["Doc_occur2"].fillna(0) # filling None values with zeros
    
        
    print("**************result dataframe visual control*********************************")
    print(d_frame)
    

if __name__ == '__main__':
    main()