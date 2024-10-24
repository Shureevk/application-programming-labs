import csv


class ImageIterator:
    def __init__(self, annotation_path: str) -> None:
        """Эта функция извлекает абсолютный путь к файлу из строки и добавляет его в список.
        :param annotation_path: путь к файлу с аннотацией
        """
        self.image_paths = []
        self.current_index = 0

        with open(annotation_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Пропускаем заголовок
            for row in csv_reader:
                abs_path = row[1]  # Предполагаем, что путь к изображению находится во втором столбце
                self.image_paths.append(abs_path)


    def __iter__(self) -> 'ImageIterator':
        """
        :return: возврат текущего экземпляра класса
        """
        return self


    def __next__(self) -> str:
        """
        Эта функция получает следующий элемент из списка абсолютных путей к изображениям.
        :return: путь к текущему изображению
        """
        if self.current_index < len(self.image_paths):
            image_path = self.image_paths[self.current_index]
            self.current_index += 1
            return image_path
        else:
            raise StopIteration