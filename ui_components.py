from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle


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

	def center_window(self, width, height):
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		x = (screen_width / 2) - (width / 2)
		y = (screen_height / 2) - (height / 2)
		self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

	def create_text_widget(self):
		frame = ttk.Frame(self.root, padding=10)
		frame.pack(expand=True, fill="both")

		text_widget = Text(frame, height=1, font=self.font, wrap="word", relief=GROOVE, bg="#e6e6e6", fg="#333333")
		text_widget.pack(expand=True, fill="both", padx=5, pady=5)
		if self.on_key_press:
			text_widget.bind("<KeyPress>", self.on_key_press)
		if self.on_key_release:
			text_widget.bind("<KeyRelease>", self.on_key_release)

		return text_widget

	def create_display_widget(self, text):
		frame = ttk.Frame(self.root, padding=10)
		frame.pack(expand=True, fill="both")

		display_widget = Text(frame, wrap="word", font=self.font, relief=FLAT, bg="#f0f0f0", fg="#333333")
		display_widget.insert("1.0", text)
		display_widget.configure(state=DISABLED)
		display_widget.pack(expand=True, fill="both", padx=5, pady=5)

		return display_widget

	@staticmethod
	def update_display_widget(display_widget):
		display_widget.configure(state=NORMAL)
		display_widget.delete("1.0", "2.0")
		display_widget.configure(state=DISABLED)

	@staticmethod
	def clear_widget(widget):
		widget.delete("1.0", "end")


if __name__ == "__main__":
	root = Tk()
	ui = UIComponents(root, ("Helvetica", 18, "bold"))
	root.mainloop()
