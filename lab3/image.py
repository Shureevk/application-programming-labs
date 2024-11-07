import cv2 as cv
import numpy as np


def flip_image(image: np.ndarray, axis: int) -> np.ndarray:
    """
    Переворачивает изображение по заданной оси.
    :param image: Входное изображение в формате NumPy массива.
    :param axis: Ось переворота (0 — вертикально, 1 — горизонтально).
    :return: Перевернутое изображение.
    """
    if axis not in (0, 1):
        raise ValueError("Ось переворота должна быть 0 (вертикально) или 1 (горизонтально).")
    return cv.flip(image, axis)
