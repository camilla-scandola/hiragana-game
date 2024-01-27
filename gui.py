import tkinter as tk
from tkinter import messagebox
from functions import check_syllable, check_word, latin_to_hiragana, hiragana_english

def check_syllable_command():
    syllable = entry.get()
    result = check_syllable(syllable)
    result_label.config(text=result)

def check_word_command():
    word = entry.get()
    result = check_word(word)
    result_label.config(text=result)

def latin_to_hiragana_command():
    jpword = entry.get()
    hiragana_version = latin_to_hiragana(jpword)
    result_label.config(text=hiragana_version)

def hiragana_english_command():
    jpword = entry.get()
    result = hiragana_english(jpword)
    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Japanese Language Functions")

# Input entry
entry_label = tk.Label(root, text="Enter input:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# Buttons for each function
button1 = tk.Button(root, text="Check Syllable", command=check_syllable_command)
button1.pack()

button2 = tk.Button(root, text="Check Word", command=check_word_command)
button2.pack()

button3 = tk.Button(root, text="Latin to Hiragana", command=latin_to_hiragana_command)
button3.pack()

button4 = tk.Button(root, text="Hiragana and English", command=hiragana_english_command)
button4.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
