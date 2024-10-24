import os

from icrawler.builtin import BingImageCrawler


def download_image(dir_name: str,keyw: str,val: int) -> None:
    """
    Функция осуществляет загрузку изображения с использованием BingImageCrawler,
    предварительно создавая директорию (если это необходимо) и очищая её (если требуется).
    :param dir_name: директория, в которую мы сохраняем изображения
    :param keyw: ключевое слово
    :param val: кол-во изображений для скачивания
    :return: None
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    google_crawler = BingImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': dir_name,"backend": "FileSystem"})
    google_crawler.crawl(keyword=keyw, max_num=val)