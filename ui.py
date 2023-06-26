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

        def add_symbol(symbol):
            if symbol == "=":
                process_input()
            else:
                entry.insert(tk.END, symbol)
            entry.focus_set()  # Return focus to the entry line

        root = tk.Tk()
        root.title("Calculator")
        # root.resizable(False, False)  # Lock window size

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
        entry = ttk.Entry(root, width=60)
        entry.bind("<Return>", lambda event: process_input())  # Bind "Return" key to process input
        entry.pack(pady=10)


        # Create calculator keyboard
        keyboard_frame = ttk.Frame(root)
        keyboard_frame.pack(side=tk.LEFT, padx=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for i, button in enumerate(buttons):
            btn = ttk.Button(keyboard_frame, text=button, width=6, command=lambda symbol=button: add_symbol(symbol))
            btn.grid(row=i // 4, column=i % 4)

        # Create function keyboard
        function_frame = ttk.Frame(root)
        function_frame.pack(side=tk.RIGHT, padx=10)

        buttons = [
            'sin', 'cos', 'tan',
            'asin', 'acos', 'atan',
            'sqrt', 'log', 'exp',
            '(', ')', 'pi'
        ]

        for i, button in enumerate(buttons):
            btn = ttk.Button(function_frame, text=button, width=10, command=lambda symbol=button: add_symbol(symbol))
            btn.grid(row=i // 3, column=i % 3)

        root.mainloop()
