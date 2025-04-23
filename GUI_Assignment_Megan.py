import tkinter as tk

def displayInput():
    user_input = entry.get()
    output_label.config(text=f"Words consumed: {user_input}")

# Creates the window and the text input box
root = tk.Tk()
root.title("Give us words so we can consume them!")
root.geometry("500x150")
entry = tk.Entry(root, width=50)
entry.pack(pady=15)

# Creates a button that uses the function to display the input
submit_button = tk.Button(root, text="Feed the word gods", command=displayInput)
submit_button.pack()
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Main loop that runs the program until its terminated
root.mainloop()
