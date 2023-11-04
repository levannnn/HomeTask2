import os

def list_file_create(txt):
    dict_file = {}
    list_file = os.listdir("txt")
    for i in list_file:
        with open(txt + '\\' + i, 'r', encoding='utf-8') as f:
            file_1 = f.readlines()
            dict_file[i] = len(file_1)
    return dict_file


list_file_create('txt')


# Запись в файл
def file_res(txt):
    list_tuple = list(list_file_create(txt).items())
    list_sorted = [i[0] for i in sorted(list_tuple, key=lambda items: items[1])]
    os.remove('write.txt')
    for name_file in list_sorted:
        with open('write.txt', 'a', encoding='utf-8') as f_1:
            with open(txt + '\\' + name_file, 'r', encoding='utf-8') as f:
                text_file = f.readlines()
            f_1.write(name_file + '\n')
            f_1.write(str(len(text_file)) + '\n')
            f_1.writelines(text_file)
            f_1.write('\n')

    return


file_res('txt')