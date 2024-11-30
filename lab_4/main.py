import argparse


import Data_Frame as d_fr


def get_input_info() -> str:
    """
    Parsing the arguments of command line
    :return: Name of csv-file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_csv', type=str, help='name dir')
    args = parser.parse_args()
    csv_file_path = args.path_to_csv
    return csv_file_path


def main() -> None:

    try:
        csv_file_path = get_input_info()

        dataframe = d_fr.create_dataframe(csv_file_path)
        print("Initial DataFrame:")
        print(dataframe.head())

        d_fr.add_image_dimensions(dataframe)
        print("\nDataFrame with Image Dimensions:")
        print(dataframe[["Height", "Width", "Depth"]].head())

        print("\nStatistical Information:")
        d_fr.display_statistical(dataframe)

        filtered_df = d_fr.filter_dataframe(dataframe, max_height=1000, max_width=1000)
        print("\nFiltered DataFrame (Images < 1000x1000):")
        print(filtered_df[["Height", "Width"]].head())

        d_fr.add_image_area(dataframe)

        sorted_df = d_fr.sort_dataframe(dataframe)
        print("\nSorted DataFrame by Area:")
        print(sorted_df.head()[["relative_path", "Area"]])

        d_fr.create_area_histogram(dataframe)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()