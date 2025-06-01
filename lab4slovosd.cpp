#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <chrono>
#include <locale>

using namespace std;

// Функция для разбора слова и формирования ассоциативного массива числа вхождений каждой буквы
unordered_map<string, int> strtomap_utf8(const string& src) {
    unordered_map<string, int> dst;
    size_t i = 0;
    while (i < src.size()) {
        size_t utf8_size = 1;
        if ((src[i] & 0x80) == 0) {
            utf8_size = 1; // 1 байт
        } else if ((src[i] & 0xE0) == 0xC0) {
            utf8_size = 2; // 2 байта
        } else if ((src[i] & 0xF0) == 0xE0) {
            utf8_size = 3; // 3 байта
        } else if ((src[i] & 0xF8) == 0xF0) {
            utf8_size = 4; // 4 байта
        }
        dst[src.substr(i, utf8_size)]++;
        i += utf8_size;
    }
    return dst;
}

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");

    cout << "Ягодяк Павел Сергеевич АИСа-020303-о24" << endl;

    string word;
    cout << "Введите слово (в нижнем регистре): ";
    cin >> word;

    cout << "Слово: " << word << ", размер слова: " << word.size() << endl;

    auto begin = chrono::steady_clock::now(); 

    auto word_map = strtomap_utf8(word);

    ifstream in("nouns.txt");
    if (!in.is_open()) {
        cout << "Не удалось открыть файл nouns.txt" << endl;
        return -1;
    }

    vector<string> lines;
    string line;

    while (getline(in, line)) {
        if (line.size() <= word.size()) {
            auto line_map = strtomap_utf8(line);
            bool found = true;
            for (const auto& p : line_map) {
                if (p.second > word_map[p.first]) {
                    found = false;
                    break;
                }
            }
            if (found) {
                lines.push_back(line);
            }
        }
    }

    // Сортируем массив строк по убыванию длины
    sort(lines.begin(), lines.end(), [](const string& s1, const string& s2) {
        return s1.length() > s2.length();
    });

    cout << "Найденные слова из словаря:" << endl;
    for (const auto& l : lines) {
        cout << l << endl;
    }

    auto end = chrono::steady_clock::now(); 
    auto duration_ms = chrono::duration_cast<chrono::milliseconds>(end - begin).count(); 
    cout << "Время выполнения (мс): " << duration_ms << " миллисекунд" << endl;

    return 0;
}
