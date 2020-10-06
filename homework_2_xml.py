def open_file_xml(file_name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding = 'utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    return items

def get_all_words(items):
    words_dict = {}
    for item in items:
        words = item.find('description').text.lower().split()
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
    items = open_file_xml('newsafr.xml')
    words_dict = get_all_words(items)
    print_top_10(words_dict)

main()
