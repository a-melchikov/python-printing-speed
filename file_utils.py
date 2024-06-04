import os
import random
from logging import getLogger

logger = getLogger(__name__)


class FileUtils:
	"""
	Класс для работы с файлами.
	"""

	def __init__(self, filename: str) -> None:
		self.filename: str = filename
		logger.info(f"Создан экземпляр {__class__.__name__} с файлом: {self.filename}")

	@property
	def filename(self) -> str:
		return self.__filename

	@filename.setter
	def filename(self, name: str) -> None:
		if not isinstance(name, str):
			logger.error("Имя файла должно быть типа str")
		if not os.path.isfile(name):
			logger.error(f"Файл '{name}' не найден")
		self.__filename = name
		logger.info(f"Установлено имя файла: {self.__filename}")

	def get_text(self, count_word: int = 10, max_len_line: int = 45) -> str:
		"""
		Получение текста из файла.

		Args:
			count_word (int): Количество слов. По умолчанию 10.
			max_len_line (int): Максимальная длина строки. По умолчанию 45.

		Returns:
			str: Текст из файла.
		"""
		logger.info(f"Получение текста с параметрами count_word={count_word}, max_len_line={max_len_line}")
		words = self.get_words_from_file(count_word)
		text = self.split_line(words, max_len_line)
		logger.info(f"Полученный текст: {text}")
		return text

	@staticmethod
	def split_text(text) -> list[str]:
		"""
		Разбиение текста на строки.

		Args:
			text (str): Текст.

		Returns:
			list[str]: Список строк.
		"""
		logger.info("Разбиение текста на строки")
		text_split = [x + " " for x in text.split('\n')]
		text_split[-1] = text_split[-1][:-1]
		logger.info(f"Результат разбиения текста: {text_split}")
		return text_split

	def get_words_from_file(self, count_word: int = 20) -> str:
		"""
		Получение случайных слов из файла.

		Args:
			count_word (int): Количество слов. По умолчанию 20.

		Returns:
			str: Слова из файла.
		"""
		logger.info(f"Получение {count_word} случайных слов из файла")
		with open(self.filename, "r", encoding="utf-8") as f:
			lines = f.readlines()
		words = " ".join(map(str.strip, random.choices(lines, k=count_word)))
		logger.info(f"Полученные слова: {words}")
		return words

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
		logger.info(f"Разбиение текста на строки с максимальной длиной {max_len}")
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

		result = "\n".join(lines)
		logger.info(f"Результат разбиения на строки: {result}")
		return result


if __name__ == "__main__":
	file = FileUtils("data/eng_words.txt")
	text_ = file.get_words_from_file()
	split_text = file.split_text(file.split_line(text_))
