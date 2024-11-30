import os
import cv2

import matplotlib.pyplot as plt
import pandas as pd


def create_dataframe(annotation_file: str) -> pd.DataFrame:
    """
    Создание DataFrame
    :param annotation_file: путь для файла аннотации
    :return: DataFrame
    """
    if not os.path.exists(annotation_file):
        raise FileNotFoundError(f"Файл аннотации не найден: {annotation_file}")
    df = pd.read_csv(annotation_file)
    df.columns = ['absolute_path', 'relative_path']
    return df


def add_image_dimensions(df: pd.DataFrame) -> None:
    """
    Добавление столбцов: длина, ширина, глубина
    :param df: Original DataFrame
    :return: None
    """
    heights, widths, depths = [], [], []

    for rel_path in df["relative_path"]:
        if not os.path.exists(rel_path):
            raise FileNotFoundError(f"Файл изображения не найден: {rel_path}")
        image = cv2.imread(rel_path)
        if image is None:
            raise ValueError(f"Не удалось открыть изображение: {rel_path}")
        h, w, d = image.shape
        heights.append(h)
        widths.append(w)
        depths.append(d)

    df["Height"] = heights
    df["Width"] = widths
    df["Depth"] = depths


def display_statistical(df: pd.DataFrame) -> None:
    """
    Создание статистики
    :param df: DataFrame to statistic
    :return: Statistical information of columns: height, width, depth
    """
    stats = df[['Height', 'Width', 'Depth']].describe()
    print(stats)

def filter_dataframe(df: pd.DataFrame, max_height: float, max_width: float) -> pd.DataFrame:
    """
    Фильрация DataFrame
    :param df: Origin DataFrame
    :param max_height: max height
    :param max_width: max width
    :return: filtered DataFrame
    """
    filter_df=df[(df["Height"] < max_height) & (df["Width"] < max_width)]
    return filter_df


def add_image_area(df: pd.DataFrame) -> None:
    """
    Добавлние колонки площадь
    :param df: Origin DataFrame
    :return: None
    """
    df["Area"] = df["Height"] * df["Width"]


def sort_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортировка DataFrame
    :param df: Origin DataFrame
    :return: Sorted DataFrame
    """
    return df.sort_values(by="Area")


def create_area_histogram(df: pd.DataFrame) -> None:
    """
    Создание гистограммы
    :param df: DataFrame
    :return: None
    """
    plt.figure(figsize=(10, 5))
    plt.hist(df['Area'], bins=20, color='blue', edgecolor='black')
    plt.title('Area distribution')
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
