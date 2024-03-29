"""checkerboard_creator.py

TODO: add other calibration pattern like https://github.com/opencv/opencv/blob/master/doc/pattern_tools/gen_pattern.py
    TODO: make_circles_pattern
    TODO: make_acircles_pattern
origin: https://github.com/ProximaB/Camera-Calibration-Pattern-Generator

usage: checkerboard_creator.py [-h] -r ROWS_GRID_NUM -c COLUMNS_GRID_NUM
                              [-s BLOCK_SIZE_MM] [-o OUTPUT_FILE_NAME]
                              [-d OUTPUT_PATH] [-b BASE_COLOR]

optional arguments:
  -h, --help            show this help message and exit
  -r ROWS_GRID_NUM, --rows-grid-num ROWS_GRID_NUM
                        Number of grid for width.
  -c COLUMNS_GRID_NUM, --columns-grid-num COLUMNS_GRID_NUM
                        Number of grid for height.
  -s BLOCK_SIZE_PX, --block-size-px BLOCK_SIZE_PX
                        Size of block element in px.
  -o OUTPUT_FILE_NAME, --output-file-name OUTPUT_FILE_NAME
                        Name of output pdf file.
  -d OUTPUT_PATH, --output-path OUTPUT_PATH
                        Path where save the checkerboard. e.g. -d C:/. | -d
                        ./checkerboards
  -b BASE_COLOR, --base-color BASE_COLOR
                        Color of rectangle, background will be set to its
                        inverted color. (rrr,ggg,bbb)
examples:
    python checkerboard_creator.py -r 2 -c 2
    python checkerboard_creator.py -r 2 -c 2 -s 30 -o 2x2
    python checkerboard_creator.py -r 10 -c 8 -d ./results -o A4_20px
    python checkerboard_creator.py -r 7 -c 8 -s 30 -o A4 -d results -b (20,30,80)

    # Example
    # create a checkerboard pattern in file chessboard.svg with 9 rows, 6 columns and a square size of 25mm
        python checkerboard_creator.py -r 6 -c 9 -s 25 -d ./calibre_file -o 6_9_25
    # create a checkerboard pattern in file chessboard.svg with 5 rows, 7 columns and a square size of 20mm
        python checkerboard_creator.py -r 5 -c 7 -s 20 -d ./calibre_file -o 5x7_20
"""

import numpy as np
import argparse
import os
from PIL import Image
from datetime import datetime

def argument_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-r", "--rows-grid-num", required=True, type=int,
                    help="Number of grid for height.")
    ap.add_argument("-c", "--columns-grid-num", required=True, type=int,
                    help="Number of grid for width.")
    ap.add_argument("-s", "--block-size-px", required=False, type=int, default=30,
                    help="Size of block element in px.")
    ap.add_argument("-o", "--output-file-name", required=False, type=str, default="Checkerboard_" + f"{datetime.now():%Y%m%d_%H%M%S}",
                    help="Name of output pdf file.")
    ap.add_argument("-d", "--output-path", required=False, type=str, default=".",
                    help="Path where save the checkerboard. e.g. -d C:/. | -d ./checkerboards")                   
    ap.add_argument("-b", "--base-color", required=False, type=str, default="(255,255,255)",
                    help="Color of rectangle, background will be set to its inverted color. (rrr,ggg,bbb)")
    return vars(ap.parse_args())

def generate_checkerboard(rows_num, columns_num, block_size, output_name, output_path, base_color):
    block_size = block_size * 4
    image_width = block_size * columns_num
    image_height = block_size * rows_num
    inv_color = tuple(255 - val for val in base_color),

    checker_board = np.zeros((image_height, image_width, 3), np.uint8)

    color_row = 0
    color_column = 0

    for i in range(0, image_height, block_size):
            color_row = not color_row
            color_column = color_row

            for j in range(0, image_width, block_size):
                checker_board[i:i+block_size, j:j +
                            block_size] = base_color if color_column else inv_color
                color_column = not color_column
    return checker_board

def save_img_to_pdf(file_name, img, saveTo):
    if not os.path.exists(saveTo):
        os.makedirs(saveTo)
    img = Image.fromarray(img)

    try:
        img.save(saveTo + "/" + file_name + ".pdf", resolution=100.0, save_all = True)
    except Exception as ex:
        print("Error while saving file.")
        print(ex)
        return False
    else: return True

# Yujie 20200205
def save_img_to_png(file_name, img, saveTo):
    if not os.path.exists(saveTo):
        os.makedirs(saveTo)
    img = Image.fromarray(img)

    img.save(saveTo + "/" + file_name + ".png", resolution=100.0, save_all = True)

def main():
    args = argument_parser()

    rows_num = args['rows_grid_num']
    columns_num = args['columns_grid_num']
    grid_size = args['block_size_px']
    output_name = args['output_file_name']
    base_color = tuple(map(int, args['base_color'][1:-1].split(',')))
    output_path = args['output_path']

    print('Generating checkerboard...')
    checker_board = generate_checkerboard(rows_num, columns_num,
                          grid_size, output_name, output_path, base_color)

    success = save_img_to_pdf(output_name, checker_board, output_path)
    # Yujie 20200205
    if success:
        save_img_to_png(output_name, checker_board, output_path)

    print(f'File {output_name}.pdf has saved to: {os.path.abspath(output_path)}') if success else print('Something goes wrong...')

if __name__ == '__main__':
    main()
else:
    pass
