import numpy as np
import tensorflow as tf

from scipy.misc import imread, imresize, imsave

from pic_omis import config

# 参考自https://github.com/igormq/ctc_tensorflow_example/blob/master/utils.py
def sparse_tuple_from(sequences, dtype=np.int32):

    indices = []
    values = []

    for n, seq in enumerate(sequences):
        indices.extend(zip([n]*len(seq), [i for i in range(len(seq))]))
        values.extend(seq)

    indices = np.asarray(indices, dtype=np.int64)
    values = np.asarray(values, dtype=dtype)
    shape = np.asarray([len(sequences), np.asarray(indices).max(0)[1]+1], dtype=np.int64)

    return indices, values, shape

# 将图像大小调整为模型需要输入的大小
def resize_image(image, input_width):

    im_arr = imread(image, mode='L')
    r, c = np.shape(im_arr)
    if c > input_width:
        c = input_width
        ratio = float(input_width) / c
        final_arr = imresize(im_arr, (int(32 * ratio), input_width))
    else:
        final_arr = np.zeros((32, input_width))
        ratio = 32.0 / r
        im_arr_resized = imresize(im_arr, (32, int(c * ratio)))
        final_arr[:, 0:min(input_width,np.shape(im_arr_resized)[1])] = im_arr_resized[:, 0:input_width]
    return final_arr, c

def label_to_array(label):
    try:
        return [config.CHAR_VECTOR.index(x) for x in label]
    except Exception as ex:
        print(label)
        raise ex

# 根据输入的ground_truth返回单词字符串
def ground_truth_to_word(ground_truth):

    try:
        return ''.join([config.CHAR_VECTOR[i] for i in ground_truth if i != -1])
    except Exception as ex:
        print(ground_truth)
        print(ex)
        input()

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
