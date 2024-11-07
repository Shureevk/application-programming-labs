import argparse
import cv2 as cv
from histogram import display_rgb_histogram, make_rgb_histogram
from image import flip_image


def get_input_info() -> tuple:
    """
    Парсинг аргументов командной строки.
    :return: Кортеж с путём к изображению, путём сохранения и осью переворота.
    """
    parser = argparse.ArgumentParser(
        description="Программа для переворота изображения и отображения его RGB гистограммы.")
    parser.add_argument('input_image_path', type=str, help='Путь к входному изображению')
    parser.add_argument('output_image_path', type=str, help='Путь для сохранения перевернутого изображения')
    parser.add_argument('flip_axis', type=int, choices=[0, 1],
                        help='Ось переворота (0 - вертикально, 1 - горизонтально)')
    args = parser.parse_args()
    return args.input_image_path, args.output_image_path, args.flip_axis


def main() -> None:
    input_image_path, output_image_path, flip_axis = get_input_info()

    try:
        image = cv.imread(input_image_path)
        if image is None:
            print(
                f"Ошибка: не удалось загрузить изображение по пути '{input_image_path}'. Проверьте путь и попробуйте снова.")
            return

        print(f"Размеры изображения {input_image_path}: {image.shape}")

        rgb_histogram = make_rgb_histogram(image)
        display_rgb_histogram(rgb_histogram)

        flipped_image = flip_image(image, flip_axis)
        cv.imshow("Original", image)
        cv.waitKey(0)
        cv.imshow("Reflected", flipped_image)
        cv.waitKey(0)

        cv.imwrite(output_image_path, flipped_image)
        print(f"Перевернутое изображение сохранено по пути: {output_image_path}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
