import os
import nltk
from collections import Counter

nltk.download('brown')
nltk.download('punkt')


def write_to_file(filename, most_common):
	with open(filename, 'w') as file:
		for word in most_common:
			file.write(f"{word}\n")


brown_data = nltk.corpus.brown.words()
filtered_words_en = [word for word in brown_data if word.isalpha() and len(word) > 2]
lower_case_words_en = [word.lower() for word in filtered_words_en]
brown_fdist_en = Counter(lower_case_words_en)

os.makedirs('../data/eng', exist_ok=True)
word_counts = [100, 250, 500, 1000, 2500, 5000]
for count in word_counts:
	most_common = [x[0] for x in brown_fdist_en.most_common(count)]
	filename = f"../data/eng/eng{count}.txt"
	write_to_file(filename, most_common)

with open('russian_text.txt', 'r', encoding='utf-8') as file:
	russian_text = file.read()

tokens_ru = nltk.word_tokenize(russian_text, language='russian')
filtered_words_ru = [word for word in tokens_ru if word.isalpha() and len(word) > 2]
lower_case_words_ru = [word.lower() for word in filtered_words_ru]
brown_fdist_ru = Counter(lower_case_words_ru)

os.makedirs('../data/rus', exist_ok=True)
for count in word_counts:
	most_common = [x[0] for x in brown_fdist_ru.most_common(count)]
	filename = f"../data/rus/rus{count}.txt"
	write_to_file(filename, most_common)

print("Файлы успешно созданы и заполнены данными в каталогах 'data/eng' и 'data/rus'.")
