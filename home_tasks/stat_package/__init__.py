import tkinter as tk
import pandas as pd
from read_and_prepare import read_input_file, prepare_text
from process_and_write import count_word_occurences, count_target_word_occurences

file_path = '/home/andrallex/lingua-latina/stat_package/input_text_file.txt'

class StatAnalysis:
    def __init__(self, word_list: list):
        
        # Create the attribute to store intermediate states
        self.__prepared_word_list = word_list
        
        # Create the root window.
        self.root_window = tk.Tk()
        self.root_window.title("Статистический анализ текста")
        self.root_window.geometry("1100x220")
        
        #========Creating frames===================================
        # Create frames to enter input file path.
        self.input_file_path_frame = tk.Frame(self.root_window)
        
        # Create frames to enter the list of target words to be analysed.
        self.target_words_list_frame = tk.Frame(self.root_window)
        
        # Create frames to enter output file path.
        self.output_file_path_frame = tk.Frame(self.root_window)
        
        # Create the frame to quit
        self.quit_frame = tk.Frame(self.root_window)

        #========Creating and packing widgets=======================
        # Create and pack widgets for entering input file path.
        self.input_file_path_label = tk.Label(self.input_file_path_frame, 
                                     text="Путь к исходному файлу:",
                                     borderwidth=3, relief="ridge", font=("Arial", 10),  width=20)
        self.input_file_path_entry = tk.Entry(self.input_file_path_frame,
                                    borderwidth=3, relief="groove", font=("Arial", 10), width=35)
        self.input_clean_button = tk.Button(self.input_file_path_frame, text='Очистить',
                                      command=self.input_clean_entry,
                                      borderwidth=3, relief="raised", font=("Arial", 8), width=4)
        self.read_prepare_button = tk.Button(self.input_file_path_frame, text='1. Прочитать и подготовить',
                                      command=self.read_and_prepare,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=20)
        self.count_words_button = tk.Button(self.input_file_path_frame, text='2. Подсчитать частоты слов',
                                      command=self.count_words,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=20)

        self.input_file_path_label.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.input_file_path_entry.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.input_clean_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.read_prepare_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.count_words_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        
        # Create and pack widgets for entering target words list.
        self.target_words_list_label = tk.Label(self.target_words_list_frame, 
                                     text="Список целевых слов:",
                                     borderwidth=3, relief="ridge", font=("Arial", 10),  width=20)
        self.target_words_list_entry = tk.Entry(self.target_words_list_frame,
                                    borderwidth=3, relief="groove", font=("Arial", 10), width=35)
        self.target_words_list_clean_button = tk.Button(self.target_words_list_frame, text='Очистить',
                                      command=self.input_clean_entry,
                                      borderwidth=3, relief="raised", font=("Arial", 8), width=4)
        self.count_target_words_button = tk.Button(self.target_words_list_frame, text='3. Подсчитать количество вхождений целевых слов',
                                      command=self.count_target_words,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=50)

        self.target_words_list_label.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.target_words_list_entry.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.target_words_list_clean_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.count_target_words_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        
        # Create and pack widgets for entering output file path.
        self.output_file_path_label = tk.Label(self.output_file_path_frame, text="Путь к выходному файлу:",
                                             borderwidth=3, relief="ridge", font=("Arial", 10), width=20)
        self.output_file_path_entry = tk.Entry(self.output_file_path_frame,
                                    borderwidth=3, relief="groove", font=("Arial", 10), width=35)
        self.output_clean_button = tk.Button(self.output_file_path_frame, text='Очистить',
                                      command=self.output_clean_entry,
                                      borderwidth=3, relief="raised", font=("Arial", 8), width=4)
        self.process_write_button = tk.Button(self.output_file_path_frame, text='4. Обработать и записать в файл',
                                      command=self.process_and_write,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=50)
        
        self.output_file_path_label.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.output_file_path_entry.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.output_clean_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.process_write_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)

        # Create and pack widgets for quit
        self.quit_button = tk.Button(self.quit_frame, text='Выход',
                                     borderwidth=3, relief="raised", font=("Arial", 12), width=15,
                                     command=self.root_window.destroy)
        self.quit_button.pack(side=tk.RIGHT, ipadx=5, ipady=5, padx=5, pady=5)

        # Pack the frames created before.
        self.input_file_path_frame.pack(expand=False)
        self.target_words_list_frame.pack(expand=False)
        self.output_file_path_frame.pack(expand=False)
        self.quit_frame.pack(expand=False)

        # Start the main loop.
        tk.mainloop()
        
    # This method is a callback function for the clean_button widgets
    def input_clean_entry(self):
        self.input_file_path_entry.delete(0, tk.END)
     
     
    def output_clean_entry(self):
        self.output_file_path_entry.delete(0, tk.END)    
    
    
    # This method is a callback function to open and prepare the input file
    def read_and_prepare(self):
        input_file_path = self.input_file_path_entry.get()
        raw_text = read_input_file(input_file_path)
        self.__prepared_word_list = prepare_text(raw_text)
        print("*****The initial text converted to list****************************************************")
        print(self.__prepared_word_list)
        print("=====The end of list=======================================================================")
        
        
    def count_words(self):
        word_occurences = count_word_occurences(self.__prepared_word_list)
        df_word_occurences = pd.DataFrame(word_occurences).T.sort_values(by=[0], ascending=False)
        df_word_occurences = df_word_occurences.rename(columns={0: 'Количество вхождений слов'})
        print("*****The prepared word list converted to dictionaty (then to df), where key = the word and value = the number of occurences*****")
        print(df_word_occurences)
        print("=====The end of dictionary=================================================================")
        
        
    def count_target_words(self):
        target_words = self.target_words_list_entry.get().replace(" ", "")
        target_word_list = target_words.split(",")
        target_word_occurences = count_target_word_occurences(self.__prepared_word_list, target_word_list)
        df_target_word_occurences = pd.DataFrame(target_word_occurences).T.sort_values(by=[0], ascending=False)
        df_target_word_occurences = df_target_word_occurences.rename(columns={0: 'Количество вхождений целевых слов'})
        print("*****The dictionary of the target words occurences converted to df****************************************")
        print(df_target_word_occurences)
        print("=====The end of dictionary=================================================================")
    
    
    def process_and_write(self):
        pass
       
        
# Create an instance of the StatAnalysis class
if __name__ == '__main__':
    stat_analysis = StatAnalysis([])