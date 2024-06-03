from tkinter import *
from tkinter.ttk import Treeview
from ui_components import UIComponents


class TypingTestUI:
	def __init__(self, root, text, on_key_press, on_key_release):
		self.root = root
		self.text = text
		self.font = ("Helvetica", 22, "bold")
		self.ui_components = UIComponents(self.root, self.font, on_key_press, on_key_release)
		self.text_widget = self.ui_components.create_text_widget()
		self.text_widget.tag_configure("mistake", underline=True, foreground="red")
		self.display_widget = self.ui_components.create_display_widget(self.text)

	def update_display_widget(self, text):
		UIComponents.update_display_widget(self.display_widget, text)

	def clear_text_widget(self):
		UIComponents.clear_widget(self.text_widget)

	def show_result(self, result_text):
		for widget in self.root.winfo_children():
			widget.destroy()
		result_label = Label(self.root, text=result_text, font=self.font)
		result_label.pack(expand=True)

	def show_history_window(self, history_manager):
		history_window = Toplevel(self.root)
		history_window.title("История тестов")
		history_window.geometry("900x400")

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

		history_data = history_manager.get_history()
		for idx, data in enumerate(history_data, start=1):
			tree.insert("", "end", text=str(idx), values=data)

		tree.pack(expand=True, fill="both")
