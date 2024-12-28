import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from read_and_prepare import read_input_file, prepare_text
from process_and_write import count_word_occurences, count_target_word_occurences, conf_dict_to_tuple_or_df
from process_and_write import write_cvs_files, write_df_to_cvs
from lemmatize import lemmatize_words


class StatAnalysis(tk.Tk):
    def __init__(self, word_list_prepared: list = None, dataframe_to_display: pd.DataFrame = None):
        
        pd.set_option('display.max_rows', None)
        
        # Create attributes to store intermediate states
        self.__prepared_word_list = word_list_prepared
        self.__df_to_display = dataframe_to_display
        
        # Create the root window.
        self.root_window = tk.Tk()
        self.root_window.title("Статистический анализ текста")
        self.root_window.geometry("1160x550") 
        
        #========Creating frames===================================
         # Create a frame to show radiobuttons to choose lemmatization
        self.lemmatization_options_frame = tk.Frame(self.root_window)
        
        # Create a frame to enter input file path.
        self.input_file_path_frame = tk.Frame(self.root_window)
        
        # Create a frame to enter the list of target words to be analysed.
        self.target_words_list_frame = tk.Frame(self.root_window)
        
        # Create a frame to enter output file path.
        self.output_file_path_frame = tk.Frame(self.root_window)
        
        # Create a frame to display DataFrame (all words)
        self.display_all_words_table_frame = tk.Frame(self.root_window)
        
        # Create a frame to display DataFrame (target words)
        self.display_target_words_table_frame = tk.Frame(self.root_window)
        
        # Create a frame to quit
        self.quit_frame = tk.Frame(self.root_window)

        #========Creating and packing widgets=======================
        # Create and pack widgets for lemmatization options
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.rb1 = tk.Radiobutton(self.lemmatization_options_frame,
                                 text="не использовать лемматизацию",
                                 variable=self.radio_var,
                                 value=1)
        self.rb2 = tk.Radiobutton(self.lemmatization_options_frame,
                                 text="применить лемматизацию",
                                 variable=self.radio_var,
                                 value=2)
        self.rb1.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.rb2.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        
        
                
        # Create and pack widgets for entering input file path.
        self.input_file_path_label = tk.Label(self.input_file_path_frame, 
                                     text="Путь к исходному файлу:",
                                     borderwidth=3, relief="ridge", font=("Arial", 10),  width=20)
        self.input_file_path_entry = tk.Entry(self.input_file_path_frame,
                                    borderwidth=3, relief="groove", font=("Arial", 10), width=35)
        self.input_clean_button = tk.Button(self.input_file_path_frame, text='Очистить',
                                      command=self.input_clean_entry,
                                      borderwidth=3, relief="raised", font=("Arial", 8), width=4)
        self.read_prepare_button = tk.Button(self.input_file_path_frame, text='1. Подсчитать частоты слов',
                                      command=self.read_prepare_count_words,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=30)
        self.count_words_and_display_table_button = tk.Button(self.input_file_path_frame, text='2. Отобразить в таблице',
                                      command=self.display_table_all_words,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=20)

        self.input_file_path_label.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.input_file_path_entry.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.input_clean_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.read_prepare_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.count_words_and_display_table_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        
        # Create and pack widgets for entering target words list.
        self.target_words_list_label = tk.Label(self.target_words_list_frame, text="Список целевых слов:",
                                     borderwidth=3, relief="ridge", font=("Arial", 10),  width=20)
        self.target_words_list_entry = tk.Entry(self.target_words_list_frame,
                                    borderwidth=3, relief="groove", font=("Arial", 10), width=35)
        self.target_words_list_clean_button = tk.Button(self.target_words_list_frame, text='Очистить',
                                      command=self.input_clean_entry,
                                      borderwidth=3, relief="raised", font=("Arial", 8), width=4)
        self.count_target_words_button = tk.Button(self.target_words_list_frame, text='3. Подсчитать частоты целевых слов',
                                      command=self.count_target_words,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=30)
        self.display_table_target_words_button = tk.Button(self.target_words_list_frame, text='4. Отобразить в таблице',
                                      command=self.display_table_target_words,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=20)

        self.target_words_list_label.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.target_words_list_entry.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.target_words_list_clean_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.count_target_words_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.display_table_target_words_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        
        # Create and pack widgets for entering output file path.
        self.output_file_path_label = tk.Label(self.output_file_path_frame, text="Путь к вых. директории:",
                                             borderwidth=3, relief="ridge", font=("Arial", 10), width=20)
        self.output_dir_path_entry = tk.Entry(self.output_file_path_frame,
                                    borderwidth=3, relief="groove", font=("Arial", 10), width=35)
        self.output_clean_button = tk.Button(self.output_file_path_frame, text='Очистить',
                                      command=self.output_clean_entry,
                                      borderwidth=3, relief="raised", font=("Arial", 8), width=4)
        self.process_write_button = tk.Button(self.output_file_path_frame, text='5. Записать выходные файлы в указанную директорию',
                                      command=self.process_and_write,
                                      borderwidth=3, relief="raised", font=("Arial", 10), width=100)
        
        self.output_file_path_label.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.output_dir_path_entry.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.output_clean_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
        self.process_write_button.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5, pady=5)
                    
        # Create and pack widgets for quit
        self.quit_button = tk.Button(self.quit_frame, text='Выход',
                                     borderwidth=3, relief="raised", font=("Arial", 12), width=15,
                                     command=self.root_window.destroy)
        self.quit_button.pack(side=tk.RIGHT, ipadx=5, ipady=5, padx=5, pady=5)

        # Pack the frames created before.
        self.lemmatization_options_frame.pack(expand=False)
        self.input_file_path_frame.pack(expand=False)
        self.target_words_list_frame.pack(expand=False)
        self.output_file_path_frame.pack(expand=False)
        self.display_all_words_table_frame.pack(expand=True)
        self.display_target_words_table_frame.pack(expand=True)
        #self.quit_frame.pack(expand=False)

        # Start the main loop.
        tk.mainloop()
        
    # ===================Description of the class methods===================================================
    # Check to lemmatize text or not        
    def is_applay_lemmatization(self) -> bool:
        return True if self.radio_var.get() == 2 else False
        
    # This method is a callback function for the clean_button widgets
    def input_clean_entry(self):
        self.input_file_path_entry.delete(0, tk.END)
     
     
    def output_clean_entry(self):
        self.output_dir_path_entry.delete(0, tk.END)    
    
    
    # This method is a callback function to open and prepare the input file
    def read_prepare_count_words(self):
        # Prepare and store the word lisf form the input file
        input_file_path = self.input_file_path_entry.get()
        raw_text = read_input_file(input_file_path)
        self.__prepared_word_list = prepare_text(raw_text)
        if self.is_applay_lemmatization():
            self.__prepared_word_list = lemmatize_words(self.__prepared_word_list)
        print("***** The initial text converted to list **************************************************")
        print(self.__prepared_word_list)
        print("===== The end of list =====================================================================")
               
        # Prepare the dictionary of word occurences and print it as DataFrame
        word_occurences = count_word_occurences(self.__prepared_word_list)
        dict_word_occurences = {k:[v] for k,v in word_occurences.items()}
        df_word_occurences = pd.DataFrame(dict_word_occurences).T.sort_values(by=[0], ascending=False)
        df_word_occurences = df_word_occurences.rename(columns={0: 'Количество вхождений слов'})
        print("***** The word list prepared and converted to dictionaty (then to df), where key = the word and value = the number of occurences *****")
        print(df_word_occurences)
        print("===== The end of dictionary ===============================================================")
        
        # Prepare and store the data to be displayed as a table
        self.__df_to_display = conf_dict_to_tuple_or_df(word_occurences)
        #print("***** The data to be displayed as a table *************************************************")
        #print("__df_to_display: ",  self.__df_to_display)
        #print("===== The end of table data ===============================================================")
        
        # Write the dataframe created to .csv file in the root directory
        write_df_to_cvs(self.__df_to_display, 'df_all_words_occurences.csv')
        
                
    # This method is a callback function to display the table of all word occurences
    def display_table_all_words(self):
        self.table_title_label = tk.Label(self.display_all_words_table_frame, text="Распределение слов по частоте встречаемости в тексте", 
                                          borderwidth=3, relief=tk.FLAT, font=("Arial", 12), width=1000)
        self.table_title_label.pack(side=tk.TOP)
      
        columns = tuple(self.__df_to_display.columns.tolist())
        self.tw_tree = ttk.Treeview(self.display_all_words_table_frame, columns=columns, show="headings")
                
        for i in columns:
            self.tw_tree.heading(i, text=str(i), anchor=tk.W)
            
        for index_column in range(len(columns)):
            index_column = f'#{index_column}'
            self.tw_tree.column(index_column, stretch=tk.NO, width=80)
        
        # Convert df to a list of tuples 
        list_of_tuples = []
        for i in self.__df_to_display.index:
            list_of_tuples.append(tuple(self.__df_to_display.iloc[i]))
                
        # Add tuples to the tree    
        for item_tuple in list_of_tuples:
            self.tw_tree.insert("", tk.END, values=item_tuple)
         
        self.scrollbar = ttk.Scrollbar(self.display_all_words_table_frame, orient=tk.VERTICAL, command=self.tw_tree.yview)   
        self.tw_tree.configure(yscroll=self.scrollbar.set)
        
        #self.table_title_label.pack(side=tk.TOP)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tw_tree.pack(fill=tk.BOTH, expand=True)           
    
    def count_target_words(self):
        # Prepare the dictionary of word occurences and print it as DataFrame
        target_words = self.target_words_list_entry.get().replace(" ", "")
        target_word_list = target_words.lower().split(",")
        target_word_occurences = count_target_word_occurences(self.__prepared_word_list, target_word_list)
        dict_target_word_occurences = {k:[v] for k,v in target_word_occurences.items()}
        df_target_word_occurences = pd.DataFrame(dict_target_word_occurences).T.sort_values(by=[0], ascending=False)
        df_target_word_occurences = df_target_word_occurences.rename(columns={0: 'Количество вхождений целевых слов'})
        print("*****The dictionary of the target words occurences converted to df****************************************")
        print(df_target_word_occurences)
        print("=====The end of dictionary=================================================================")
        
        #Prepare and store the data to be displayed as a table
        self.__df_to_display = conf_dict_to_tuple_or_df(target_word_occurences)
        #print("***** The data to be displayed as a table *************************************************")
        #print("__df_to_display: ",  self.__df_to_display)
        #print("===== The end of table data ===============================================================")
        
        # Write the dataframe created to .csv file in the root directory
        write_df_to_cvs(self.__df_to_display, 'df_target_words_occurences.csv')
        
                   
    # This method is a callback function to display the table of torget word occurences
    def display_table_target_words(self):
        self.table_title_label = tk.Label(self.display_target_words_table_frame, text="Распределение целевых слов по частоте встречаемости в тексте", 
                                          borderwidth=3, relief=tk.FLAT, font=("Arial", 12), width=1000)
        self.table_title_label.pack(side=tk.TOP)
        
        columns = tuple(self.__df_to_display.columns.tolist())
        self.tw_tree = ttk.Treeview(self.display_target_words_table_frame, columns=columns, show="headings")
                
        for i in columns:
            self.tw_tree.heading(i, text=str(i), anchor=tk.W)
            
        for index_column in range(len(columns)):
            index_column = f'#{index_column}'
            self.tw_tree.column(index_column, stretch=tk.NO, width=80)
         
        # Convert df to a list of tuples 
        list_of_tuples = []
        for i in self.__df_to_display.index:
            list_of_tuples.append(tuple(self.__df_to_display.iloc[i]))
                
        # Add tuples to the tree 
        for item_tuple in list_of_tuples:
            self.tw_tree.insert("", tk.END, values=item_tuple)
         
        self.scrollbar = ttk.Scrollbar(self.display_target_words_table_frame, orient=tk.VERTICAL, command=self.tw_tree.yview)   
        self.tw_tree.configure(yscroll=self.scrollbar.set)
        
        #self.table_title_label.pack(side=tk.TOP)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tw_tree.pack(fill=tk.BOTH, expand=True)
        
    # This method is a callback function to write csv. files to the user pointed directory       
    def process_and_write(self):
        try:
            write_cvs_files(self.output_dir_path_entry.get(), 'df_all_words_occurences.csv')
            write_cvs_files(self.output_dir_path_entry.get(), 'df_target_words_occurences.csv')
            print(f'Файлы "df_all_words_occurences.csv",  "df_target_words_occurences.csv" успешно записаны в указанную директорию')
        except:
            print(f'Не удалось записать файлы "df_all_words_occurences.csv",  "df_target_words_occurences.csv" в указанную директорию')
            
           
# Create an instance of the StatAnalysis class
if __name__ == '__main__':
    stat_analysis = StatAnalysis()
 
