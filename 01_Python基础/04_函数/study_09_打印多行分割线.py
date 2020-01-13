def print_line(char, times):
    """打印单行分割线

    :param char: 分割线使用的分割字幅
    :param times: 分割线的长度
    """
    print(char * times)


def print_lines(char, times, row):
    """打印多行分割线

    :param char: 分割线字幅
    :param times: 分割线每行的字幅数
    :param row: 分割线的行数
    :return:
    """
    row1 = 1
    while row1 <= row:
        print_line(char, times)
        row1 += 1


print_lines("-", 20, 5)
