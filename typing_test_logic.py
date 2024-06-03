import time


class TypingTestLogic:
	def __init__(self, text_split):
		self.text_split = text_split
		self.start_time = None
		self.end_time = None
		self.mismatches = set()
		self.idx_line = 1

	def process_key_release(self, event, ui, end_callback):
		text = ui.text_widget.get("1.0", "end-1c")

		if text == self.text_split[self.idx_line - 1]:
			ui.update_display_widget(text)
			ui.clear_text_widget()
			self.idx_line += 1

		if text == "" and self.idx_line == 1:
			self.start_time = None
			self.mismatches.clear()
			ui.text_widget.tag_remove("mistake", "1.0", "end")
		elif self.idx_line == len(self.text_split) + 1:
			end_callback()

		idx = len(text) - 1
		if self.idx_line < len(self.text_split) + 1 and 0 <= idx < len(self.text_split[self.idx_line - 1]):
			if text[idx] != self.text_split[self.idx_line - 1][idx]:
				self.mismatches.add(idx)
				ui.text_widget.tag_add("mistake", f"1.{idx}", f"1.{idx + 1}")
			else:
				ui.text_widget.tag_remove("mistake", f"1.{idx}", f"1.{idx + 1}")

	def calculate_results(self):
		self.end_time = time.time()
		elapsed_time = self.end_time - self.start_time

		error_count = len(self.mismatches)
		total_chars = sum(len(line) for line in self.text_split)
		accuracy = ((total_chars - error_count) / total_chars) * 100
		speed = 60 * total_chars / elapsed_time

		return elapsed_time, error_count, total_chars, accuracy, speed
