#!/usr/bin/env python3
# author: joez

import sys
import random
import argparse


def parse_args():
    p = argparse.ArgumentParser(
        description='A Schulte Table generator', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('-v', '--version', action='version',
                   version='%(prog)s 0.1.0')
    p.add_argument('-r', '--rows', help='table rows', type=int, default=4)
    p.add_argument('-c', '--cols', help='table columns', type=int, default=4)
    p.add_argument('-n', '--nums', help='number of tables',
                   type=int, default=5)

    return p.parse_args()


def main():
    args = parse_args()
    grids = [gen_grid(rows=args.rows, cols=args.cols)
             for i in range(args.nums)]
    print_grids(grids)
    save_grids(grids)


def save_grids(grids, file="schulte-table.xlsx"):
    try:
        import xlsxwriter
        import os
    except ImportError:
        return

    if os.path.exists(file):
        os.unlink(file)
    book = xlsxwriter.Workbook(file)
    head = "秒表计时，按顺序手指口念，熟练后可以尝试倒数"
    stat = "第{}次:____秒"
    center = {'align': 'center', 'valign': 'vcenter'}
    fmt_grid = book.add_format({'font_size': 50, 'border': 1, **center})
    fmt_head = book.add_format({'font_size': 16, **center})
    fmt_stat = book.add_format({'font_size': 20, **center})
    for n, grid in enumerate(grids):
        rows, cols = (0, 0)
        try:
            rows = len(grid)
            cols = len(grid[0])
        except IndexError:
            pass
        if rows < 1 or cols < 1:
            continue
        sheet = book.add_worksheet('{:d}'.format(n+1))
        grid_r, grid_c = (1, 0)
        for i, row in enumerate(grid):
            sheet.write_row(grid_r+i, grid_c, row, fmt_grid)
            sheet.set_row(grid_r+i, 80)
        sheet.set_column(grid_c, grid_c+cols-1, 16)
        sheet.merge_range(grid_r-1, grid_c, grid_r-1,
                          grid_c+cols, head, fmt_head)
        sheet.set_row(grid_r-1, 30)
        sheet.set_column(grid_c+cols, grid_c+cols, 20, fmt_stat)
        for i in range(3):
            sheet.write(grid_r+i, grid_c+cols, stat.format(i+1))
    book.close()


def gen_grid(rows=4, cols=4):
    '''
    Generate a Schulte Table with given cols and rows
    The result is a 2D array (list of rows)
    '''
    nums = list(range(1, cols * rows + 1))
    random.shuffle(nums)
    grid = [None] * rows
    for i in range(0, len(grid)):
        grid[i], nums = nums[:cols], nums[cols:]
    return grid


def print_grids(grids):
    for grid in grids:
        print("")
        for row in grid:
            print(*row)


if __name__ == "__main__":
    main()
