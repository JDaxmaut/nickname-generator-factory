import tkinter as tk
import random

#lists of vowels and consonants
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
special_chars = "!@#$%^&*"

def generate_nickname(min_length, max_length, start_with_vowel=False, use_repeats=True, use_special_chars=False):
    length = random.randint(min_length, max_length)
    nickname = []

    is_vowel_turn = start_with_vowel

    for i in range(length):
        if is_vowel_turn:
            nickname.append(random.choice(vowels))
        else:
            nickname.append(random.choice(consonants))
        is_vowel_turn = not is_vowel_turn

        if use_repeats and random.random() < 0.2:
            nickname.append(nickname[-1])
        
        if use_special_chars and random.random() < 0.1:
            nickname.append(random.choice(special_chars))

    nickname = "".join(nickname)
    nickname = nickname.capitalize()

    return nickname

def on_generate():
    try:
        min_length = int(min_length_entry.get())
        max_length = int(max_length_entry.get())

        if max_length < min_length:
            result_label.config(text="Maximum length must be greater than minimum.")
            return

        start_with_vowel = start_with_vowel_var.get()
        use_special_chars = use_special_chars_var.get()

        result = "Generated Nicknames:\n" + "\n".join(
            generate_nickname(min_length, max_length, start_with_vowel, True, use_special_chars)
            for _ in range(5)
        )
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Please enter valid numbers for length.")

def on_button_press(event):
    generate_button.config(bg="#005cbf")  

def on_button_release(event):
    generate_button.config(bg="#448aff")  


#main window
root = tk.Tk()
root.title("Nickname Generator")
root.geometry("400x400")
root.configure(bg="#171515")

#variables
start_with_vowel_var = tk.BooleanVar()
use_special_chars_var = tk.BooleanVar()

#interface elements
min_length_label = tk.Label(root, text="Minimum Length:", bg="#171515", fg="white")
min_length_label.pack(pady=5)

min_length_entry = tk.Entry(root, bg="#333333", fg="white", insertbackground="white")
min_length_entry.pack(pady=5)

max_length_label = tk.Label(root, text="Maximum Length:", bg="#171515", fg="white")
max_length_label.pack(pady=5)

max_length_entry = tk.Entry(root, bg="#333333", fg="white", insertbackground="white")
max_length_entry.pack(pady=5)

start_with_vowel_check = tk.Checkbutton(root, text="Start with a vowel", variable=start_with_vowel_var, bg="#171515", fg="white", activebackground="#333333")
start_with_vowel_check.pack(pady=5)

use_special_chars_check = tk.Checkbutton(root, text="Use special characters", variable=use_special_chars_var, bg="#171515", fg="white", activebackground="#333333")
use_special_chars_check.pack(pady=5)

generate_button = tk.Button(root, text="Generate", command=on_generate, bg="#448aff", fg="white")
generate_button.pack(pady=10)

#bind button press and release events
generate_button.bind("<ButtonPress>", on_button_press)
generate_button.bind("<ButtonRelease>", on_button_release)

result_label = tk.Label(root, text="", bg="#171515", fg="white", justify=tk.LEFT)
result_label.pack(pady=5)


root.mainloop()