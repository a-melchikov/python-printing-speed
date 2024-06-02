import random


def get_words_from_file(filename: str, count_word: int = 20) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return " ".join(map(str.strip, random.choices(lines, k=count_word)))
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return ""
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""


def split_line(text: str, max_len: int = 45) -> str:
    words = text.split()
    current_line = []
    lines = []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) > max_len:
            lines.append(" ".join(current_line))
            current_line = [word]
        else:
            current_line.append(word)

    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)


if __name__ == "__main__":
    text = get_words_from_file("eng_words.txt", 40)
    print(split_line(text, 20).split('\n'))
