# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла

def file_info(file_way: str):
    *_, file_name = file_way.split('/')
    *_, file_tape = file_name.split('.') 
    return (file_way, file_name, file_tape)



way_file = '/Users/timuribatulin/Downloads/images.png'
print(file_info(way_file))


