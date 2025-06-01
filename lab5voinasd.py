print("Ягодяк Павел Сергеевич АИСа-020303-о24")
import re
from collections import Counter

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def preprocess_text(text):
    # Удаляем знаки препинания и переводим текст в нижний регистр
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    return words

def build_frequency(words):
    return Counter(words)

def search_words(frequency, query):
    # Находим слова, содержащие запрос
    matching_words = {word: freq for word, freq in frequency.items() if query in word}
    # Сортируем по частоте и берем первые 20
    sorted_words = sorted(matching_words.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:20]

def main():
    file_path = 'voina_i_mir.txt'  # Путь к файлу с текстом
    text = load_text(file_path)
    words = preprocess_text(text)
    frequency = build_frequency(words)

    while True:
        query = input("Введите запрос (не менее 3 символов): ")
        if len(query) < 3:
            print("Запрос должен содержать не менее 3 символов.")
            continue
        
        results = search_words(frequency, query)
        print("Найденные слова:")
        for word, freq in results:
            print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
