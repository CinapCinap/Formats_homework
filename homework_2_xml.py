import xml.etree.ElementTree as ET


def open_file_xml(file_name):
    parser = ET.XMLParser(encoding = 'utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    return items

def get_all_words(items, min_word_length):
    words_dict = {}
    for item in items:
        words = item.find('description').text.lower().split()
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
    items = open_file_xml('newsafr.xml')
    words_dict = get_all_words(items, 6)
    print_top_words(words_dict, 6, 10)

main()
