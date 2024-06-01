from tkinter import *
from tkinter import ttk
import time


def end():
    global end_time
    end_time = time.time()
    elapsed_time = end_time - start_time

    matches = sum(
        char_first == char_second for char_first, char_second in zip(entry.get(), TEXT)
    )

    print(f"Аккуратность {((matches / len(TEXT)) * 100):.2f}%")
    print(f"Заняло времени {elapsed_time:.2f} секунд")
    print(f"Скорость {len(TEXT) * (60 / elapsed_time):.2f} символов в минуту")
    root.destroy()


def on_key_press(event):
    global start_time
    if start_time is None:
        start_time = time.time()


def on_key_release(event):
    global start_time
    if entry.get() == "":
        start_time = None


def on_enter(event):
    end()


TEXT = "hello world"

root = Tk()
root.title("Typing speed")
root.geometry("250x150")

start_time = None
end_time = None

label = ttk.Label(text=TEXT)
label.pack(anchor="center")

entry = ttk.Entry()
entry.pack(expand=True)
entry.bind("<KeyPress>", on_key_press)
entry.bind("<KeyRelease>", on_key_release)
entry.bind("<Return>", on_enter)

root.mainloop()
