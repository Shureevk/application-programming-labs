import csv
import os
import os.path as op

def annotation_make(dir_name:str, annotation_file: str) -> None:
    """
    Функция генерирует аннотацию, создавая CSV-файл,
    в который записываются заголовки ('relative path', 'Absolute path'),
    а также заносятся относительные и абсолютные пути.
    :param dir_name: директория с изображениями
    :param annotation_file:csv файл для аннотации
    :return: None
    """
    with open(annotation_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute path", "relative path"])
        image_list = os.listdir(dir_name)
        for image_name in image_list:
            absolute_path = op.abspath(op.join(dir_name, image_name))
            relative_path = op.relpath(op.join(dir_name, image_name), start=".")
            writer.writerow([absolute_path, relative_path])