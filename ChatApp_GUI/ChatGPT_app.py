
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = ("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")

import tkinter as tk
from tkinter import scrolledtext, END
from nltk.chat.util import Chat, reflections

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("ChatGPT GUI")

        # Create the chat window
        self.chat_window = scrolledtext.ScrolledText(master, state='disabled', height=50, width=70)
        self.chat_window.grid(column=0, row=0, padx=10, pady=10)

        # Create the input box
        self.input_box = tk.Entry(master, width=70)
        self.input_box.grid(column=0, row=1, padx=10, pady=10)
        self.input_box.bind('<Return>', self.send_message)


    def send_message(self, event):
            user_input = self.input_box.get()
            self.input_box.delete(0, END)
            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo", max_tokens=1000,    n=1,    stop=None,    temperature=0.5,
              messages=[{"role": "user", "content": user_input}]
            )
            # Get the chatbot's response
            response = []
            
            # Display the response in the chat window
            self.chat_window.configure(state='normal')
            self.chat_window.insert(tk.END, "You: " + user_input + "\n")
            for choice in completion.choices:
                self.chat_window.insert(tk.END, "ChatGPT: " + choice.message.content + "\n")
            self.chat_window.configure(state='disabled')
            self.chat_window.yview(tk.END)





'''

# Start the chat
print("Welcome to my ChatGPT app!")

        user_input = input("What may help you: ")


        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", max_tokens=1000,    n=1,    stop=None,    temperature=0.5,
          messages=[{"role": "user", "content": user_input}]
        )

        # Print the generated text
        for choice in completion.choices:
            print(choice.message.content)

'''

# Create the GUI
root = tk.Tk()
chatbot_gui = ChatbotGUI(root)
root.mainloop()

