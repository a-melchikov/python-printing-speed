import datetime
from logging import getLogger

logger = getLogger(__name__)


class HistoryManager:
	def __init__(self, file_path="data/history.txt"):
		self.file_path = file_path
		logger.info(f"Создан экземпляр {__class__.__name__} данные сохраняются в: {self.file_path}")

	def save_result(self, count_word, error_count, total_chars, accuracy, elapsed_time, speed):
		logger.info(f"Сохранение результата в файл: {self.file_path}")
		with open(self.file_path, "a", encoding="utf-8") as f:
			f.write(f"{count_word} {error_count}/{total_chars} {accuracy:.2f} {elapsed_time:.2f} {speed:.2f} "
					f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
			logger.info(
				f"В файл {self.file_path} успешно сохранены данные: {count_word} {error_count}/{total_chars} "
				f"{accuracy:.2f} {elapsed_time:.2f} {speed:.2f} "
				f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

	def get_history(self):
		logger.info(f"Получение истории тестов из файла: {self.file_path}")
		with open(self.file_path, "r", encoding="utf-8") as f:
			lines = f.readlines()
			lines.reverse()
			res = [line.split() for line in lines]
			logger.info(f"История тестов была успешно получена (последние 5 тестов): {res[:5]}")
			return res
