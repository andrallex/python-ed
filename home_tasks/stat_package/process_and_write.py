from collections import Counter
import pandas as pd
import os
import shutil


# Count the number of occurences of words
def count_word_occurences(word_list: list) -> dict:
    return Counter(word_list) 
      

# Count the number of occurences of the target words
def count_target_word_occurences(word_list: list, target_word_list: list) -> dict:
    word_counts_dict = count_word_occurences(word_list)
    return {word: word_counts_dict.get(word, 0) for word in target_word_list}


# Configure the dictionary to transform it then to the dyad of tuple and list
def conf_dict_to_tuple_or_df(init_dict: dict) -> pd.DataFrame:
    max_value = max(init_dict.values())
    res_dict = {}
    len_list = []
    for i in range(1, max_value+1):
        eq_freq_word_list = list(({k for k, v in init_dict.items() if v == i}))
        len_val = len(eq_freq_word_list)
        if len_val > 0:
            res_dict[i] = sorted(eq_freq_word_list)
            len_list.append(len_val)
    
    max_len = max(len_list)  
    for k, v in res_dict.items():
        times = max_len - len(v)
        if times > 0:
            v += [""] * times
            
    df = pd.DataFrame(res_dict)
    df.columns.name = "Frequency"
    
    return df

# Copy cvs. files created before to the pointed directory
def write_cvs_files(output_dir_path: str, filename: str):
    output_file_path = output_dir_path + '/' + filename
        
    abs_dirpath = os.path.dirname(os.path.abspath(__file__))
    abs_filepath = abs_dirpath + '/' + filename
    
    shutil.copy(abs_filepath, output_file_path)
    
    
# Write the dataframe created to .csv file in the root directory
def write_df_to_cvs(dataframe: pd.DataFrame, filename: str):
    abs_dirpath = os.path.dirname(os.path.abspath(__file__))
    abs_filepath = abs_dirpath + '/' + filename
    
    dataframe.to_csv(abs_filepath, encoding='utf-8')
    
