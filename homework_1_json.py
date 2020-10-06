def open_file_json(file_name):
    import json
    with open(file_name, encoding = 'utf-8') as file:
        data = json.load(file)
    return data

def get_all_words(data):
    news_list = data["rss"]["channel"]["items"]
    words_dict = {}
    for item in news_list:
        words = item["description"].lower().split()
        for i in range(len(words)):
            if len(words[i]) > 6:
                words_dict[words[i]] = words_dict.get(words[i], 0) + 1            
    words_dict = list(words_dict.items())
    words_dict.sort(key=lambda i: i[1], reverse=True)    
    return words_dict

def print_top_10(words_list):
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n')
    for i in range(0, 10):
        print(f'"{words_list[i][0]}" - {words_list[i][1]} упоминаний')  
    return

def main():
    data = open_file_json('newsafr.json')
    words_dict = get_all_words(data)
    print_top_10(words_dict)

main()
