# 1. Create a window
# 2. Frame and "add" button
# 3. Implement an "add" function
# 4. Implement a "delete" function with "delete" buttons
# 5. Check for possible errors in code. Optimize the code

import tkinter as tk
from tkinter.simpledialog import askstring

counter = 1

mydict = {}


def add(window):
    global counter

    try:
        check = tk.Checkbutton(window, text="Done")
        check.grid(row=counter, column=1)

        todo_title = askstring("Input", "Enter the title of an activity to do")
        text_edit = tk.Label(window, text=todo_title, relief=tk.RAISED)
        text_edit.grid(row=counter, column=2, pady=4)

        delete_button = tk.Button(window, text="🗑", command=lambda idx=counter: delete(idx))
        delete_button.grid(row=counter, column=3, padx=5)

        mydict[counter] = [check, text_edit, delete_button]

        counter += 1
    except Exception as e:
        print(e)


def delete(idx):
    for widget in mydict[idx]:
        widget.destroy()

    del mydict[idx]


def main():
    window = tk.Tk()
    window.title("Todo list")
    window.geometry("500x300")

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    add_button = tk.Button(frame, text="Add", command=lambda: add(window))
    add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    frame.grid(row=0, column=0, sticky="ns")

    window.mainloop()


main()
