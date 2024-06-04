import time
from logging import getLogger

logger = getLogger(__name__)


class TypingTestLogic:
	def __init__(self, text_split):
		self.text_split = text_split
		self.start_time = None
		self.end_time = None
		self.mismatches = set()
		self.idx_line = 1
		logger.info(f"Создан экземпляр {__class__.__name__} c текстом {text_split}")

	def process_key_release(self, event, ui, end_callback):
		logger.info("Обработка нажатой клавиши")
		text = ui.text_widget.get("1.0", "end-1c")
		logger.debug(f"Введена строка {text}")

		if text == self.text_split[self.idx_line - 1]:
			logger.info(f"Введенная строка равна первой строке: {text}")
			self.idx_line += 1
			logger.debug(f"Индекс строки увеличен {self.idx_line}")
			ui.clear_text_widget()
			ui.update_display_widget("\n".join(self.text_split[self.idx_line - 1:]))
		else:
			logger.debug(f"Введенная строка {text} != {self.text_split[self.idx_line - 1]}")

		if text == "" and self.idx_line == 1:
			logger.debug(f"Сброс времени и ошибок {self.start_time}, {self.mismatches}")
			self.start_time = None
			self.mismatches.clear()
			ui.text_widget.tag_remove("mistake", "1.0", "end")
			logger.debug(f"Время: {self.start_time}, Ошибки: {self.mismatches}")
		elif self.idx_line == len(self.text_split) + 1:
			logger.info("Все строки были успешно введены")
			end_callback()

		idx = len(text) - 1
		if self.idx_line < len(self.text_split) + 1 and 0 <= idx < len(self.text_split[self.idx_line - 1]):
			if text[idx] != self.text_split[self.idx_line - 1][idx]:
				logger.info(
					f"Допущена ошибка по индексу {idx} ожидался символ {self.text_split[self.idx_line - 1][idx]} был введен {text[idx]}")
				self.mismatches.add(idx)
				ui.text_widget.tag_add("mistake", f"1.{idx}", f"1.{idx + 1}")
			else:
				logger.debug(f"Ошибки по индексу {idx} не обнаружено")
				ui.text_widget.tag_remove("mistake", f"1.{idx}", f"1.{idx + 1}")

	def calculate_results(self):
		logger.info("Вычисление результата")
		self.end_time = time.time()
		elapsed_time = self.end_time - self.start_time

		error_count = len(self.mismatches)
		total_chars = sum(len(line) for line in self.text_split)
		accuracy = ((total_chars - error_count) / total_chars) * 100
		speed = 60 * total_chars / elapsed_time
		logger.info(f"Результат был успешно вычислен время: {elapsed_time} сек, ошибки/символы: {error_count}/{total_chars} "
					f"аккуратность: {accuracy}%, скорость: {speed} сим/мин")

		return elapsed_time, error_count, total_chars, accuracy, speed
