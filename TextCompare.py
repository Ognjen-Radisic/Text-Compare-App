import tkinter as tk
from tkinter import filedialog
import string
import math

WIDTH = 800
HEIGHT = 600


# FUNCTIONS

# BUTTON FUNCTIONS #######################################################################################
def _open1():
    global label_file1  # global for clear function
    global file1_path  # global for compare function
    root.filename = filedialog.askopenfilename(initialdir='C:/', title='Open txt file for comparing',
                                               filetypes=(('txt files', '*.txt'), ('all files', '*.*')))
    file1_path = root.filename

    # label 1 left
    folders_path = file1_path.split('/')
    label_name = folders_path[-1]
    # error check
    if label_name[-4:] == '.txt':
        label_file1 = tk.Label(frame, text=label_name)
        label_file1.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.15)
    else:
        label_file1 = tk.Label(frame, text='You are not loading txt file, try again')
        label_file1.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.15)
    button1['state'] = 'disabled'
    button_compare['state'] = 'normal'


def _clear1():
    label_file1.destroy()
    button1['state'] = 'normal'
    if label_final.winfo_exists() == 1:
        label_final.destroy()
        button_compare['state'] = 'normal'


def _open2():
    global label_file2
    global file2_path
    root.filename = filedialog.askopenfilename(initialdir='C:/', title='Open txt file for comparing',
                                               filetypes=(('txt files', '*.txt'), ('all files', '*.*')))
    file2_path = root.filename

    # label 2 right
    folders_path = file2_path.split('/')
    label_name = folders_path[-1]
    # error check
    if label_name[-4:] == '.txt':
        label_file2 = tk.Label(frame, text=label_name)
        label_file2.place(relwidth=0.4, relheight=0.1, relx=0.55, rely=0.15)
    else:
        label_file2 = tk.Label(frame, text='You are not loading txt file, try again')
        label_file2.place(relwidth=0.4, relheight=0.1, relx=0.55, rely=0.15)
    button2['state'] = 'disabled'
    button_compare['state'] = 'normal'


def _clear2():
    label_file2.destroy()
    button2['state'] = 'normal'
    if label_final.winfo_exists() == 1:
        label_final.destroy()
        button_compare['state'] = 'normal'


def _reset():
    if label_file1.winfo_exists() == 1:
        label_file1.destroy()
        button1['state'] = 'normal'
    if label_file2.winfo_exists() == 1:
        label_file2.destroy()
        button2['state'] = 'normal'
    label_final.destroy()
    button_compare['state'] = 'normal'


def _compare():
    global label_final

    if button2['state'] == 'normal' or button1['state'] == 'normal':
        print("Chose two text files.\nPress RESET button and try again")
        label_text = "Chose two text files.\nPress RESET button and try again"
        label_final = tk.Label(frame, text=label_text)
        label_final.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.55)
        button_compare['state'] = 'disabled'
        return

    path_of_file_1 = None
    path_of_file_2 = None
    if file1_path[-4:] == '.txt':
        path_of_file_1 = file1_path
    if file2_path[-4:] == '.txt':
        path_of_file_2 = file2_path
    if path_of_file_1 != None and path_of_file_2 != None:
        sorted_word_list_1 = word_frequencies_for_file(path_of_file_1)
        sorted_word_list_2 = word_frequencies_for_file(path_of_file_2)
        similarity_in_percent = vector_angle(sorted_word_list_1, sorted_word_list_2)
        print(f"These two texts are {similarity_in_percent}% similar")
        if similarity_in_percent == 100:
            label_text = 'Given text files are IDENTICAL'
        else:
            percent_sign = '%'
            label_text = 'Given text files are: %s %s similar' % (similarity_in_percent, percent_sign)
        label_final = tk.Label(frame, text=label_text)
        label_final.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.55)
    else:
        print('Something went wrong! PRESS RESET button and try loading .txt files again')
        label_text = 'Something went wrong!\nPRESS RESET button and try loading .txt files again'
        label_final = tk.Label(frame, text=label_text)
        label_final.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.55)
        button_compare['state'] = 'disabled'

    button_compare['state'] = 'disabled'


# COMPARE FUNCTIONS #################################################################################

def word_frequencies_for_file(filePath):  # called by func _compare
    line_list = read_file(filePath)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    list_for_path = filePath.split('/')
    filename = list_for_path[-1]

    print("File", filename, ":")
    print(len(line_list), "lines,")
    print(len(word_list), "words,")
    print(len(freq_mapping), "distinct words")
    print()

    return freq_mapping


##################################
# Function 1: read a text file ##
##################################
def read_file(filePath):  # called by func word_frequencies_for_file
    with open(filePath, 'r') as f:
        return f.read()


#################################################
# Function 2: split the text lines into words ##
#################################################
def get_words_from_line_list(text):  # called by func word_frequencies_for_file
    # translation table maps upper case to lower case and punctuation to spaces

    translation_table = text.maketrans(string.punctuation + string.ascii_uppercase,
                                       " " * len(string.punctuation) + string.ascii_lowercase)
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


##############################################
# Function 3: count frequency of each word ##
##############################################
def count_frequency(word_list):  # called by func word_frequencies_for_file
    dictionary_of_words = {}
    for new_word in word_list:
        if new_word in dictionary_of_words:
            dictionary_of_words[new_word] = dictionary_of_words[new_word] + 1
        else:
            dictionary_of_words[new_word] = 1
    return dictionary_of_words


def inner_product(D1, D2):  # called by func vector angle
    total_sum = 0.0
    for key in D1:
        if key in D2:
            total_sum += D1[key] * D2[key]
    return total_sum


def vector_angle(D1, D2):  # called by func _compare
    numerator = inner_product(D1, D2)  # a ovo je razlika izmedju ta dva vektora
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))  # d1*d1 je duzina vektora
    similarity = int(100 * round(numerator / denominator, 2))
    return similarity

    # kosinus izmedju vektora D1 i D2 = {  (D1*D2) / koren[((D1*D1)*(D2*D2))]  }


# Tkinter APP #######################################################################################
root = tk.Tk()
root.title('Text Compare Program')
# fixed size of the opened window
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

frame = tk.Frame(root, bg='#32a893')
frame.place(relwidth=1, relheight=1)

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

# left button pair
button1 = tk.Button(frame, text='BROWSE TXT FILE 1', font=50, command=_open1)
button1.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.3)
button1_clear = tk.Button(frame, text='CLEAR', font=50, command=_clear1)
button1_clear.place(relwidth=0.2, relheight=0.1, relx=0.15, rely=0.42)

# right button pair
button2 = tk.Button(frame, text='BROWSE TXT FILE 2', font=50, command=_open2)
button2.place(relwidth=0.4, relheight=0.1, relx=0.55, rely=0.3)
button2_clear = tk.Button(frame, text='CLEAR', font=50, command=_clear2)
button2_clear.place(relwidth=0.2, relheight=0.1, relx=0.65, rely=0.42)

# bottom button pair
button_compare = tk.Button(frame, text='COMPARE', font=50, state='disabled', command=_compare)
button_compare.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.7)
button_reset = tk.Button(frame, text='RESET', font=50, command=_reset)
button_reset.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.82)

root.mainloop()