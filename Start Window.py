import tkinter as tk

def start_game():
    print("Game is starting...")

def exit_game():
    root.destroy()

root = tk.Tk()
root.title("Game Menu")

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

exit_button = tk.Button(root, text="Exit Game", command=exit_game)
exit_button.pack()

root.mainloop()
