import requests

responce = requests.get("https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/")

with open("../data/eng_words.txt", "w", encoding="utf-8") as f:
	f.write("\n".join(
		word for word in responce.text[responce.text.find('abandon'):responce.text.find('zone')].split("<br />") if
		len(word) > 1))
