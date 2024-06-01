from tkinter import *
import time


def end():
    global end_time
    end_time = time.time()
    elapsed_time = end_time - start_time

    accuracy = (((len(TEXT) - len(mismatches)) / len(TEXT)) * 100)
    error_count = len(mismatches)
    total_chars = len(TEXT)
    speed = len(TEXT) * (60 / elapsed_time)

    print(f"Аккуратность: {accuracy:.2f}%")
    print(f"Ошибок {error_count} из {total_chars} символов")
    print(f"Заняло времени {elapsed_time:.2f} сек.")
    print(f"Скорость {speed:.2f} символов в минуту")

    root.destroy()


def on_key_press(event):
    global start_time

    if start_time is None:
        start_time = time.time()

    if event.keysym == "Return":
        return "break"


def on_key_release(event):
    global start_time
    global mismatches

    if event.keysym == "Return":
        return "break"

    text = text_widget.get("1.0", END).strip()
    idx = len(text) - 1

    if 0 <= idx < len(TEXT):
        if text[idx] != TEXT[idx]:
            mismatches.add(idx)
            text_widget.tag_add("mistake", f"1.{idx}", f"1.{idx+1}")
        else:
            text_widget.tag_remove("mistake", f"1.{idx}", f"1.{idx+1}")

    if text == "":
        start_time = None
        mismatches.clear()
        text_widget.tag_remove("mistake", "1.0", END)
    elif text == TEXT:
        end()


TEXT = "hello world"

root = Tk()
root.title("Typing speed")
root.geometry("400x200")

start_time = None
end_time = None
mismatches = set()

display_widget = Text(root, height=1, wrap="none", font=("Helvetica", 18))
display_widget.insert("1.0", TEXT)
display_widget.configure(state=DISABLED)
display_widget.pack(anchor="nw")

text_widget = Text(root, font=("Helvetica", 18))
text_widget.pack(expand=True)
text_widget.bind("<KeyPress>", on_key_press)
text_widget.bind("<KeyRelease>", on_key_release)

text_widget.tag_configure("mistake", underline=True, foreground="red")

root.mainloop()
