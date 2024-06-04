from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
from logging import getLogger

logger = getLogger(__name__)


class UIComponents:
	def __init__(self, root, font, on_key_press=None, on_key_release=None):
		self.root = root
		self.font = font
		self.on_key_press = on_key_press
		self.on_key_release = on_key_release

		style = ThemedStyle(root)
		style.set_theme("clearlooks")
		# equilux
		# radiance
		# yaru
		# plastik
		# clearlooks

		self.center_window(800, 600)
		logger.info(f"Создан экземпляр {__class__.__name__} выбрана тема: {style.current_theme}")

	def center_window(self, width, height):
		logger.info(f"Создание центрального окна приложения с параметрами {width}x{height}")
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		logger.info(f"Разрешение экрана пользователя {screen_width}x{screen_height}")
		x = (screen_width / 2) - (width / 2)
		y = (screen_height / 2) - (height / 2)
		self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
		logger.info(f"Центральное окно успешно создано с параметрами ({width}x{height}+{int(x)}+{int(y)})")

	def create_text_widget(self):
		logger.info("Создание текстового виджета")
		frame = ttk.Frame(self.root, padding=10)
		frame.pack(expand=True, fill="both")

		text_widget = Text(frame, height=1, font=self.font, wrap="word", relief=GROOVE, bg="#e6e6e6", fg="#333333")
		text_widget.pack(expand=True, fill="both", padx=5, pady=5)
		if self.on_key_press:
			text_widget.bind("<KeyPress>", self.on_key_press)
		if self.on_key_release:
			text_widget.bind("<KeyRelease>", self.on_key_release)
		logger.debug(f"Создан текстовый виджет Text: {text_widget.pack_info()}")
		return text_widget

	def create_display_widget(self, text):
		logger.info(f"Создание отображающего виджета с текстом: {text}")
		frame = ttk.Frame(self.root, padding=10)
		frame.pack(expand=True, fill="both")

		display_widget = Text(frame, wrap="word", font=self.font, relief=FLAT, bg="#f0f0f0", fg="#333333")
		display_widget.insert("1.0", text)
		display_widget.configure(state=DISABLED)
		display_widget.pack(expand=True, fill="both", padx=5, pady=5)
		logger.debug(f"Создан отображающий виджет Text: {display_widget.pack_info()}")
		return display_widget

	@staticmethod
	def update_display_widget(display_widget, text):
		logger.info(f"Обновление отображающего виджета текстом: {text}")
		display_widget.configure(state=NORMAL)
		display_widget.delete("1.0", END)
		display_widget.insert("1.0", text)
		display_widget.configure(state=DISABLED)
		logger.info(f"Данные в отображающем виджете успешно обновлены")

	@staticmethod
	def clear_widget(widget):
		logger.debug(f"Очистка виджета {widget}")
		widget.delete("1.0", "end")
		logger.debug(f"Очистка виджета {widget} прошла успешно")


if __name__ == "__main__":
	root = Tk()
	ui = UIComponents(root, ("Helvetica", 18, "bold"))
	root.mainloop()
