import datetime


class HistoryManager:
	def __init__(self, file_path="data/history.txt"):
		self.file_path = file_path

	def save_result(self, count_word, error_count, total_chars, accuracy, elapsed_time, speed):
		with open(self.file_path, "a", encoding="utf-8") as f:
			f.write(f"{count_word} {error_count}/{total_chars} {accuracy:.2f} {elapsed_time:.2f} {speed:.2f} "
					f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

	def get_history(self):
		with open(self.file_path, "r", encoding="utf-8") as f:
			lines = f.readlines()
			lines.reverse()
			return [line.split() for line in lines]
