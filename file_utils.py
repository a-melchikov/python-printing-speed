import os
import random


class FileUtils:
	"""
	Класс для работы с файлами.
	"""

	def __init__(self, filename: str) -> None:
		self.filename: str = filename

	@property
	def filename(self) -> str:
		return self.__filename

	@filename.setter
	def filename(self, name: str) -> None:
		if not isinstance(name, str):
			raise ValueError("Имя файла должно быть типа str")
		if not os.path.isfile(name):
			raise FileNotFoundError(f"Файл '{name}' не найден")
		self.__filename = name

	def get_text(self, count_word: int = 10, max_len_line: int = 45) -> str:
		"""
		Получение текста из файла.

		Args:
			count_word (int): Количество слов. По умолчанию 10.
			max_len_line (int): Максимальная длина строки. По умолчанию 45.

		Returns:
			str: Текст из файла.
		"""
		words = self.get_words_from_file(count_word)
		return self.split_line(words, max_len_line)

	@staticmethod
	def split_text(text) -> list[str]:
		"""
		Разбиение текста на строки.

		Args:
			text (str): Текст.

		Returns:
			list[str]: Список строк.
		"""
		text_split = [x + " " for x in text.split('\n')]
		text_split[-1] = text_split[-1][:-1]
		return text_split

	def get_words_from_file(self, count_word: int = 20) -> str:
		"""
		Получение случайных слов из файла.

		Args:
			count_word (int): Количество слов. По умолчанию 20.

		Returns:
			str: Слова из файла.
		"""
		with open(self.filename, "r", encoding="utf-8") as f:
			lines = f.readlines()
		return " ".join(map(str.strip, random.choices(lines, k=count_word)))

	@staticmethod
	def split_line(text: str, max_len: int = 45) -> str:
		"""
		Разбиение текста на строки.

		Args:
			text (str): Текст.
			max_len (int): Максимальная длина строки. По умолчанию 45.

		Returns:
			str: Текст, разбитый на строки.
		"""
		words = text.split()
		current_line = []
		lines = []

		for word in words:
			if sum(len(w) for w in current_line) + len(current_line) + len(word) > max_len:
				lines.append(" ".join(current_line))
				current_line = [word]
			else:
				current_line.append(word)

		if current_line:
			lines.append(" ".join(current_line))

		return "\n".join(lines)


if __name__ == "__main__":
	file = FileUtils("data/eng_words.txt")
	text_ = file.get_words_from_file()
	print(file.split_text(file.split_line(text_)))
