import argparse

from annotation import annotation_make
from download import download_image
from iterator import ImageIterator


def arg_parser() -> argparse.Namespace:
    """
    Функция, которая позволяет ввести ключевое слово, указать путь к директории,
    задать количество изображений и указать путь к файлу для аннотирования.
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='Ключевое слово для поиска фотографий')
    parser.add_argument('-d','--dir_name', type=str, help='Путь к директории')
    parser.add_argument('-v','--num_images', type=int, help='Количество изображений для скачивания')
    parser.add_argument('-f', '--annotation_file', type=str, help='Путь к файлу для аннотации')
    arg = parser.parse_args()
    return arg

def main() -> None:
    try:
        args = arg_parser()
        download_image(args.dir_name, args.keyword, args.num_images)
        annotation_make(args.dir_name, args.annotation_file)
        iterator = ImageIterator(args.annotation_file)
        for img in iterator:
            print(img)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()