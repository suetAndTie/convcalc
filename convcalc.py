'''
convcalc.py

Given input size, kernel size, stride, and padding
It prints the output size after the convolution is applied
((input - size + 2 * pad) // stride) + 1
'''

import argparse


parser = argparse.ArgumentParser()
# Required arguments
parser.add_argument('input', metavar='input_size', type=int, help='Image input size')
parser.add_argument('kernel', metavar='kernel_size', type=int, help='Kernel size')

# Optional arguments
parser.add_argument('--stride', type=int, default=1, help='Stride of convolution')
parser.add_argument('--pad', type=int, default=0, help='0-padding')

# Print out
opt = parser.parse_args()
print(opt)
output_size = ((opt.input - opt.kernel + 2 * opt.pad) // opt.stride) + 1
print('Output Size: ' + str(output_size))

