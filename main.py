import os
import sys
from tkinter import *
import time
from get_words_file import get_words_from_file, split_line


def end():
    global end_time

    end_time = time.time()
    elapsed_time = end_time - start_time

    error_count = len(mismatches)
    total_chars = len(TEXT)
    accuracy = ((total_chars - error_count) / total_chars) * 100
    speed = 60 * len(TEXT) / elapsed_time

    result_text = (
        f"Аккуратность: {accuracy:.2f}%\n"
        f"Ошибок: {error_count} из {total_chars} символов\n"
        f"Заняло времени: {elapsed_time:.2f} сек.\n"
        f"Скорость: {speed:.2f} символов в минуту"
    )

    show_result(result_text)


def show_result(result_text):
    for widget in root.winfo_children():
        widget.destroy()

    result_label = Label(root, text=result_text, font=("Helvetica", 14))
    result_label.pack(expand=True)


def on_key_press(event):
    global start_time

    if start_time is None:
        start_time = time.time()

    if event.keysym == "Return":
        return "break"


def on_key_release(event):
    global start_time
    global mismatches
    global idx_line

    if event.keysym == "Return":
        return "break"

    text = text_widget.get(f"1.0", END)[:-1]

    idx = len(text) - 1
    print(idx_line, len(TEXT_SPLIT))
    if text == TEXT_SPLIT[idx_line - 1]:
        display_widget.configure(state=NORMAL)
        display_widget.delete(f"{idx_line}.0", f"{idx_line + 1}.0")
        display_widget.configure(state=DISABLED)
        text_widget.delete("1.0", END)
        idx_line += 1

    if text == "":
        start_time = None
        mismatches.clear()
        text_widget.tag_remove("mistake", "1.0", END)
    elif idx_line == len(TEXT_SPLIT) + 1:
        end()

    if idx_line < len(TEXT_SPLIT) + 1 and 0 <= idx < len(TEXT_SPLIT[idx_line - 1]):
        if text[idx] != TEXT_SPLIT[idx_line - 1][idx]:
            mismatches.add(idx)
            text_widget.tag_add("mistake", f"1.{idx}", f"1.{idx+1}")
        else:
            text_widget.tag_remove("mistake", f"1.{idx}", f"1.{idx+1}")



def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def on_ctrl_r(event):
    restart()


words = get_words_from_file("eng_words.txt", 10)
TEXT = split_line(words)
TEXT_SPLIT = [x + " " for x in TEXT.split('\n')]
TEXT_SPLIT[-1] = TEXT_SPLIT[-1][:-1]

root = Tk()
root.title("Typing speed")
root.geometry("600x400")

start_time = None
end_time = None
mismatches = set()
idx_line = 1

root.bind("<Control-r>", on_ctrl_r)

text_widget = Text(root, height=1, font=("Helvetica", 18, "bold"))
text_widget.pack(expand=True)
text_widget.bind("<KeyPress>", on_key_press)
text_widget.bind("<KeyRelease>", on_key_release)

text_widget.tag_configure("mistake", underline=True, foreground="red")

display_widget = Text(root, wrap="word", font=("Helvetica", 18, "bold"))
display_widget.insert("1.0", TEXT)
display_widget.configure(state=DISABLED)
display_widget.pack(anchor="nw", pady=10)

root.mainloop()
