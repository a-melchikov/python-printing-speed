import time
from tkinter import *
from file_utils import FileUtils
from typing_test_logic import TypingTestLogic
from history_manager import HistoryManager
from typing_test_ui import TypingTestUI


class TypingSpeedTest:
	def __init__(self, root, count_word: int = 10, max_len_line: int = 20):
		self.root = root
		self.root.title("Тест скорости печати")
		self.root.geometry("800x600")

		self.COUNT_WORD = count_word
		self.MAX_LEN_LINE = max_len_line

		self.file = FileUtils("data/eng_words.txt")
		self.text = self.file.get_text(self.COUNT_WORD, self.MAX_LEN_LINE)
		self.text_split = self.file.split_text(self.text)

		self.logic = TypingTestLogic(self.text_split)
		self.ui = TypingTestUI(self.root, self.text, self.on_key_press, self.on_key_release)
		self.history_manager = HistoryManager()

		self.root.bind("<Control-h>", self.show_history)
		self.root.bind("<Control-r>", self.update_text)
		self.root.bind("<Control-z>", self.exit_app)

	def on_key_press(self, event):
		if self.logic.start_time is None:
			self.logic.start_time = time.time()
		if event.keysym == "Return":
			return "break"

	def on_key_release(self, event):
		if event.keysym == "Return":
			return "break"
		self.logic.process_key_release(event, self.ui, self.end_test)

	def end_test(self):
		elapsed_time, error_count, total_chars, accuracy, speed = self.logic.calculate_results()

		result_text = (
			f"Аккуратность: {accuracy:.2f}%\n"
			f"Ошибок: {error_count} из {total_chars} символов\n"
			f"Заняло времени: {elapsed_time:.2f} сек.\n"
			f"Скорость: {speed:.2f} символов в минуту"
		)

		self.history_manager.save_result(self.COUNT_WORD, error_count, total_chars, accuracy, elapsed_time, speed)
		self.ui.show_result(result_text)

	def reset_ui(self):
		for widget in self.root.winfo_children():
			widget.destroy()
		self.ui = TypingTestUI(self.root, self.text, self.on_key_press, self.on_key_release)

	def update_text(self, event=None):
		self.text = self.file.get_text(self.COUNT_WORD, self.MAX_LEN_LINE)
		self.text_split = self.file.split_text(self.text)
		self.logic = TypingTestLogic(self.text_split)
		self.reset_ui()
		self.ui.update_display_widget(self.text)

	def show_history(self, event=None):
		self.ui.show_history_window(self.history_manager)

	def exit_app(self, event=None):
		self.root.quit()


if __name__ == "__main__":
	root = Tk()
	TypingSpeedTest(root, 5, 45)
	root.mainloop()
