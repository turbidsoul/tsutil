# -*- coding: utf8 -*-

from random import Random

rand = Random()

block = []

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def gen_empty_sdk():
    """
    产生一个空的数独数组
    """
    _sdk = []
    for x in nums:
        r = []
        for x in nums:
            r.append(0)
        _sdk.append(r)
    return _sdk


def get_row(sdk, row):
    """
    得到此数独的指定行list
    """
    return sdk[row]


def get_col(sdk, col):
    """
    得到此数独的指定列list
    """
    return [[row[col] for row in sdk] for col in range(len(nums))][col]


def get_block(sdk, block=None, row=None, col=None):
    """
    得到此数独的指定区块的list
    """
    if not block:
        block = get_block_num(row, col)

    r = 0
    c = 0
    if block in [1, 4, 7]:
        c = 3
    elif block in [2, 5, 8]:
        c = 6
    elif block in [3, 6, 9]:
        c = 9

    if block in [1, 2, 3]:
        r = 3
    elif block in [4, 5, 6]:
        r = 6
    elif block in [7, 8, 9]:
        r = 9
    return [sdk[row][col] for row in range(9) for col in range(9) if (row >= 3 * (r - 1) and row < 3 * r and col >= 3 * (c - 1) and col < 3 * c)]


def get_block_num(row, col):
    """
    根据行列号，得到区块号
    """
    if row in [1, 2, 3]:
        block_row = [1, 2, 3]
    elif row in [4, 5, 6]:
        block_row = [4, 5, 6]
    elif row in [7, 8, 9]:
        block_row = [7, 8, 9]

    if col in [1, 2, 3]:
        block_col = [1, 4, 7]
    elif col in [4, 5, 6]:
        block_col = [2, 5, 8]
    elif col in [7, 8, 9]:
        block_col = [3, 6, 9]

    return [block for block in nums if block in block_row and block in block_col][0]


def main():
    sdk = gen_empty_sdk()
    for r in range(len(sdk)):
        for c in range(len(sdk[r])):
            col2row = [[row[col] for row in sdk] for col in range(len(sdk[r]))]  # 行列转换
            block = get_block(r + 1, c + 1)
            print "row:", r + 1, "col:", c + 1, "\nchoice:", [x for x in nums if (x not in sdk[r]) and (x not in col2row[c])], '\nrow:', sdk[r], '\nblock:', block
            sdk[r][c] = rand.choice([x for x in nums if (x not in get_row(r)) and (x not in get_col(c)) and (x not in block)])
            print "row after:", sdk[r], '\ncol after:', [[row[col] for row in sdk] for col in range(len(sdk[r]))][c]
        print("---------------------------")
        for row in sdk:
            print row
        print("---------------------------")
    for r in sdk:
        print(r)


if __name__ == '__main__':
    main()
