########################################################################

import os
import numpy as np

PATH = 'D:/githubcode/mfwtest01.github.io/python编程从入门到实践'

########################################################################


def read_txt(txt_path, mode='r+', encoding='utf-8'):
    with open(txt_path, mode, encoding=encoding) as file:
        text = file.read()

        # # Take both "space" and "\n" as spliting characters.
        # # For English volcabularies.
        # characters = text.split()

        # For Chinese characters.
        characters = list(text)

    return characters


def read_txt_np(txt_path, dtype=str, delimiter=' ', encoding='utf-8'):
    # The delimiter is None by default, and None means ' '.
    # The encoding is 'bytes' by default.
    return np.loadtxt(txt_path,
                      dtype=dtype,
                      delimiter=delimiter,
                      encoding=encoding).reshape(-1, 5)


def write_txt(data, txt_path, mode=None, replace=False):
    if '%' in mode:
        # c      : character
        # d or i : signed decimal integer
        # e or E : scientific notation with e or E.
        # f      : decimal floating point (e.g. '%.2f')
        # g, G   : use the shorter of e,E or f
        # o      : signed octal
        # s      : string of characters
        # u      : unsigned decimal integer
        # x,X    : unsigned hexadecimal integer
        if os.path.exists(txt_path) and replace:
            previous = np.loadtxt(txt_path,
                                  dtype=str,
                                  delimiter=' ',
                                  encoding='utf-8')
            data = np.vstack([previous, data])
            np.savetxt(txt_path, data, fmt=mode)

        else:
            np.savetxt(txt_path, data, fmt=mode)    # fmt = '%s'

    else:
        file = open(txt_path, mode)
        # Can write multiple strings contained in a list.
        file.writelines(data)
        # Can only write a string.
        file.write(data)
        file.close()


def horizontal2vertical(txt_path, col, right2left=False):
    # Read a selected txt file.
    characters = read_txt(txt_path, encoding='utf-8')
    # Determine how many extra characters should be added.
    space = ['  ' for i in range(col - len(characters) % col)]
    # Add the space to the existing characters.
    characters.extend(space)
    # Reshape and transpose the characters.
    paragraph = np.array(characters).reshape(col, -1).T

    if right2left:
        # Convert the column sequence.
        paragraph = paragraph[:, ::-1]

    # Write the transformed paragraph back to the file.
    file = open(txt_path, 'w', encoding='utf-8')
    # Write the paragraph to a file line by line.
    for line in paragraph:
        # Change a list of words back to a string.
        string = ''.join(str(i) for i in line)
        # Mind to change lines.
        file.writelines(string + '\n')

    file.close()
    return paragraph


########################################################################


if __name__ == '__main__':
    # characters = read_txt(os.path.join(PATH, 'test.txt'), encoding='utf-8')
    # print(len(characters))
    # print((characters))

    horizontal2vertical(os.path.join(PATH, 'test.txt'), 10, right2left=False)

    # np.savetxt('vertical.txt', characters, encoding='utf-8')

    # arr = read_txt_np('/Users/kcl/Desktop/Logo_iPY2txt/TRG_10.txt')
    # print(arr[:, :4].astype(np.float))
    # arr = np.random.randint(0, 5, 20).reshape(5, 4)
    # write_txt(arr, 'test.txt', mode='%s')
