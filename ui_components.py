from tkinter import Text, DISABLED, NORMAL


class UIComponents:
	def __init__(self, root, font, on_key_press=None, on_key_release=None):
		self.root = root
		self.font = font
		self.on_key_press = on_key_press
		self.on_key_release = on_key_release

	def create_text_widget(self):
		text_widget = Text(self.root, height=1, font=self.font)
		text_widget.pack(expand=True)
		if self.on_key_press:
			text_widget.bind("<KeyPress>", self.on_key_press)
		if self.on_key_release:
			text_widget.bind("<KeyRelease>", self.on_key_release)
		return text_widget

	def create_display_widget(self, text):
		display_widget = Text(self.root, wrap="word", font=self.font)
		display_widget.insert("1.0", text)
		display_widget.configure(state=DISABLED)
		display_widget.pack(anchor="nw", pady=10)
		return display_widget

	@staticmethod
	def update_display_widget(display_widget):
		display_widget.configure(state=NORMAL)
		display_widget.delete("1.0", "2.0")
		display_widget.configure(state=DISABLED)

	@staticmethod
	def clear_widget(widget):
		widget.delete("1.0", "end")
