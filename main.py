import datetime
import os
import sys
import time
from tkinter import *
from tkinter.ttk import Treeview
from get_words_file import get_words_from_file, split_line


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест скорости печати")
        self.root.geometry("600x400")

        self.COUNT_WORD = 5
        self.MAX_LEN_LINE = 15

        self.text = self.get_text(self.COUNT_WORD, self.MAX_LEN_LINE)
        self.text_split = self.split_text(self.text)
        self.start_time = None
        self.end_time = None
        self.mismatches = set()
        self.idx_line = 1

        self.display_widget = None
        self.text_widget = None

        self.setup_ui()
        self.root.bind("<Control-r>", self.restart)
        self.root.bind("<Control-h>", self.history)

    @staticmethod
    def get_text(count_word=10, max_len_line=45):
        words = get_words_from_file("eng_words.txt", count_word)
        return split_line(words, max_len_line)

    @staticmethod
    def split_text(text):
        text_split = [x + " " for x in text.split('\n')]
        text_split[-1] = text_split[-1][:-1]
        return text_split

    def setup_ui(self):
        self.text_widget = Text(self.root, height=1, font=("Helvetica", 18, "bold"))
        self.text_widget.pack(expand=True)
        self.text_widget.bind("<KeyPress>", self.on_key_press)
        self.text_widget.bind("<KeyRelease>", self.on_key_release)
        self.text_widget.tag_configure("mistake", underline=True, foreground="red")

        self.display_widget = Text(self.root, wrap="word", font=("Helvetica", 18, "bold"))
        self.display_widget.insert("1.0", self.text)
        self.display_widget.configure(state=DISABLED)
        self.display_widget.pack(anchor="nw", pady=10)

    def on_key_press(self, event):
        if self.start_time is None:
            self.start_time = time.time()

        if event.keysym == "Return":
            return "break"

    def on_key_release(self, event):
        if event.keysym == "Return":
            return "break"

        text = self.text_widget.get("1.0", END)[:-1]

        if text == self.text_split[self.idx_line - 1]:
            self.display_widget.configure(state=NORMAL)
            self.display_widget.delete("1.0", "2.0")
            self.display_widget.configure(state=DISABLED)
            self.text_widget.delete("1.0", END)
            self.idx_line += 1

        if text == "" and self.idx_line == 1:
            self.start_time = None
            self.mismatches.clear()
            self.text_widget.tag_remove("mistake", "1.0", END)
        elif self.idx_line == len(self.text_split) + 1:
            self.end()

        idx = len(text) - 1
        if self.idx_line < len(self.text_split) + 1 and 0 <= idx < len(self.text_split[self.idx_line - 1]):
            if text[idx] != self.text_split[self.idx_line - 1][idx]:
                self.mismatches.add(idx)
                self.text_widget.tag_add("mistake", f"1.{idx}", f"1.{idx+1}")
            else:
                self.text_widget.tag_remove("mistake", f"1.{idx}", f"1.{idx+1}")

    def end(self):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time

        error_count = len(self.mismatches)
        total_chars = len(self.text)
        accuracy = ((total_chars - error_count) / total_chars) * 100
        speed = 60 * len(self.text) / elapsed_time

        result_text = (
            f"Аккуратность: {accuracy:.2f}%\n"
            f"Ошибок: {error_count} из {total_chars} символов\n"
            f"Заняло времени: {elapsed_time:.2f} сек.\n"
            f"Скорость: {speed:.2f} символов в минуту"
        )

        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"{self.COUNT_WORD} {error_count}/{total_chars} {accuracy:.2f} {elapsed_time:.2f}"
                    f" {speed:.2f} {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")

        self.show_result(result_text)

    def show_result(self, result_text):
        for widget in self.root.winfo_children():
            widget.destroy()

        result_label = Label(self.root, text=result_text, font=("Helvetica", 14))
        result_label.pack(expand=True)

    def restart(self, event=None):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def history(self, event=None):
        history_window = Toplevel(self.root)
        history_window.title("История тестов")
        history_window.geometry("900x200")  # Установите желаемый размер окна

        tree = Treeview(history_window)
        tree["columns"] = ("Count Word", "Errors", "Accuracy", "Time", "Speed", "Date", "Date(h:m:s)")
        tree.heading("#0", text="ID")
        tree.heading("Count Word", text="Кол-во слов")
        tree.heading("Errors", text="Ошибки/Символы")
        tree.heading("Accuracy", text="Аккуратность %")
        tree.heading("Time", text="Время сек.")
        tree.heading("Speed", text="Скорость сим./мин.")
        tree.heading("Date", text="Дата")
        tree.heading("Date(h:m:s)", text="Дата (ч:м:с)")

        tree.column("#0", width=30)
        tree.column("Count Word", width=90)
        tree.column("Errors", width=130)
        tree.column("Accuracy", width=110)
        tree.column("Time", width=80)
        tree.column("Speed", width=130)
        tree.column("Date", width=110)
        tree.column("Date(h:m:s)", width=110)

        with open("history.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            lines.reverse()

        for idx, line in enumerate(lines, start=1):
            data = line.split()
            tree.insert("", "end", text=str(idx), values=data)

        tree.pack(expand=True, fill="both")


if __name__ == "__main__":
    root = Tk()
    TypingSpeedTest(root)
    root.mainloop()
