import tkinter as tk
import threading

def start_game():
    root.destroy()
    threading.Thread(target=pygame_main).start()

root = tk.Tk()
root.title("Game Menu")

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

root.mainloop()