'''
convcalc.py

Given input size, kernel size, stride, and padding
It prints the output size after the convolution is applied
((input - size + 2 * pad) // stride) + 1
'''

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--input', type=int, required=True, help='Input size')
parser.add_argument('--size', type=int, required=True, help='Kernel Size')
parser.add_argument('--stride', type=int, default=1, help='Stride of convolution')
parser.add_argument('--pad', type=int, default=0, help='0-padding')

opt = parser.parse_args()
print(opt)
output_size = ((opt.input - opt.size + 2 * opt.pad) // opt.stride) + 1
print('Output Size: ' + str(output_size))

