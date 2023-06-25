from expression import Expression
import tkinter as tk
from tkinter import ttk

class UI:
    def __init__(self):
        pass

    def run(self):


        def process_input():
            input_line = entry.get()
            # Process the expression here (e.g., evaluate, analyze, etc.)
            # In this example, we simply display "Ok." as the computer's answer
            response = Expression(input_line).evaluate()
            conversation_text.configure(state='normal')
            conversation_text.insert(tk.END, "> " + input_line + "\n")
            conversation_text.insert(tk.END, response + "\n")
            conversation_text.configure(state='disabled')
            entry.delete(0, tk.END)  # Clear the input field
            conversation_text.yview(tk.END)  # Automatically scroll to the end

        root = tk.Tk()
        root.title("Console-like Application")

        # Create conversation display
        conversation_frame = ttk.Frame(root)
        conversation_frame.pack(fill=tk.BOTH, expand=True)

        conversation_text = tk.Text(conversation_frame, height=20, width=50)
        conversation_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create scrollbar for conversation display
        scrollbar = ttk.Scrollbar(conversation_frame, command=conversation_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        conversation_text.configure(yscrollcommand=scrollbar.set)
        conversation_text.configure(state='disabled')

        # Create input field
        entry = tk.Entry(root, width=50)
        entry.bind("<Return>", lambda event: process_input())  # Bind "Return" key to process input
        entry.pack()

        # Create Enter button
        button = tk.Button(root, text="Enter", command=process_input)
        button.pack()

        root.mainloop()
