import re


# Read the input file
def read_input_file(input_file_path: str) -> str:
    file_ref = open(input_file_path, 'r')
    input_text = file_ref.read()
    file_ref.close()
    return input_text


# Prepare the text and convert it to list
def prepare_text(text: str) -> list:
    return re.findall(r'\w+', text.lower())



 



    


#

