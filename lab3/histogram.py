import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def make_rgb_histogram(image: np.ndarray) -> tuple:
    """
    Рассчитывает гистограмму RGB для изображения.
    :param image: Входное изображение в формате NumPy массива.
    :return: Кортеж с гистограммами для красного, зеленого и синего каналов.
    """
    red_h = cv.calcHist([image], [2], None, [256], [0, 256])
    green_h = cv.calcHist([image], [1], None, [256], [0, 256])
    blue_h = cv.calcHist([image], [0], None, [256], [0, 256])
    return red_h, green_h, blue_h


def display_rgb_histogram(hist: tuple) -> None:
    """
    Отображает гистограмму RGB.
    :param hist: Кортеж с гистограммами для красного, зеленого и синего каналов.
    """
    plt.figure(figsize=(10, 5))
    plt.title('Гистограмма RGB')
    plt.xlabel('Диапазон пикселей')
    plt.ylabel('Количество пикселей')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    red_h, green_h, blue_h = hist
    plt.plot(red_h, color='red', label='Красный канал')
    plt.plot(green_h, color='green', label='Зеленый канал')
    plt.plot(blue_h, color='blue', label='Синий канал')
    plt.legend()
    plt.show()
