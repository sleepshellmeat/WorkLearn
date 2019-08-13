import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import qrcode

def qr_matrix(data):
    qr = qrcode.QRCode(version=1, box_size=1, border=1)
    qr.add_data(data)
    return np.asarray(qr.get_matrix(), dtype = int)

def _rle(matrix):
    # find run start and ends
    d = np.diff(matrix)
    row, start_pos = np.where(d > 0)
    _, end_pos = np.where(d < 0)
    # find run lengths
    run_lengths = end_pos - start_pos
    # split runs from different rows into separate arrays
    split_on = np.cumsum(np.bincount(row - 1))[:-1]
    return np.split(run_lengths, split_on)

def run_length_encode(matrix):
    rle_row = _rle(matrix)
    rle_col = _rle(matrix.T)
    return rle_row, rle_col

def nonogram_qr(data):
    qr = qr_matrix(data)
    row_rle, col_rle = run_length_encode(qr)
    shape = np.array(qr.shape) - 2
    return shape, row_rle, col_rle

def draw_nonogram(shape, row_rle, col_rle):
    r, c = shape
    f = open('qr.griddler', "w")

    f.write('MK Version 3.0')
    f.write('\n')
    f.write('\n')

    f.write(str(r)+' '+str(c))
    f.write('\n')
    f.write('\n')

    q=np.zeros((r,c),dtype=int)
    for qq in q:
        f.write(str(qq)[1:-1].replace("0", "?"))
        f.write('\n')
    f.write('\n')

    for col in col_rle:
        f.writelines(str(col[::-1])[1:-1])
        f.write('\n')

    f.write('\n')
    for row in row_rle:
        f.writelines(str(row[::-1])[1:-1])
        f.write('\n')

    fig, ax = plt.subplots(figsize=(10, 10))
    plt.axis('off')
    plt.axis('equal')
    # draw the grid for the nonogram:
    for i in range(r + 1):
        ax.plot([0, c], [-i, -i], 'k-')
    for j in range(c + 1):
        ax.plot([j, j], [0, -r], 'k-')

    # draw the numbers onto the grid
    for i, row in enumerate(row_rle):
        for idx, val in enumerate(row[::-1]):

            ax.annotate(xy=(-idx - 0.5, -i - 0.5), s=val, ha='center', va='center')
    for j, col in enumerate(col_rle):
        for idx, val in enumerate(col[::-1]):
            ax.annotate(xy=(j + 0.5, idx + 0.5), s=val, ha='center', va='center')

    # adjust x and y limits
    lim_left = max([len(x) for x in row_rle + col_rle]) + 1
    lim_right = max(r, c) + 1
    ax.set_xlim(-lim_left, lim_right)
    ax.set_ylim(-lim_right, lim_left)
    return ax

name=input('请输入二维码内容（比如我爱你？）：')
ax = draw_nonogram(*nonogram_qr(name))
print('制作完成，图片名字叫做：打印吧.jpg')

savefig("打印吧.jpg")