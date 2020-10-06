import json


def open_file_json(file_name):
    with open(file_name, encoding = 'utf-8') as file:
        data = json.load(file)
    return data

def get_all_words(data, min_word_length):
    news_list = data["rss"]["channel"]["items"]
    words_dict = {}
    for item in news_list:
        words = item["description"].lower().split()
        for word in words:
            if len(word) > min_word_length:
                words_dict[word] = words_dict.get(word, 0) + 1        
    words_dict = list(words_dict.items())
    words_dict.sort(key=lambda i: i[1], reverse=True)    
    return words_dict

def print_top_words(words_list, min_word_length, word_count):
    print(f'Топ {word_count} самых часто встречающихся в новостях '
          f'слов длиннее {min_word_length} символов:\n')
    for word, count in words_list[:word_count]:
        print(f'"{word}" - {count} упоминаний')    
    return words_list[:word_count]

def main():
    data = open_file_json('newsafr.json')
    words_dict = get_all_words(data, 6)
    print_top_words(words_dict, 6, 10)

main()
