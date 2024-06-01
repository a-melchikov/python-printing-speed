import random


def get_words_from_file(filename, count_word):
	with open(filename, "r", encoding="utf-8") as f:
		return " ".join((map(str.strip, random.choices(f.readlines(), k=count_word))))


if __name__ == "__main__":
	print(get_words_from_file("eng_words.txt", 30))