'''
convcalc.py

Given input size, kernel size, stride, and padding
It prints the output size after the convolution is applied
((input - size + 2 * pad) // stride) + 1

Added dilation of convolution (dilation is essentially increasing the size of the kernel)

((input - (size + (size - 1) * (dilation - 1)) + 2 * pad) // stride) + 1
'''

import argparse


parser = argparse.ArgumentParser()
# Required arguments
parser.add_argument('input', metavar='input_size', type=int, help='Image input size')
parser.add_argument('kernel', metavar='kernel_size', type=int, help='Kernel size')

# Optional arguments
parser.add_argument('--stride', type=int, default=1, help='Stride of convolution')
parser.add_argument('--pad', type=int, default=0, help='0-padding')
parser.add_argument('--dilation', type=int, default=1, help='Dilation of convolution')

# Print out
opt = parser.parse_args()
if opt.input <= 0: raise ValueError('Input size {} must be greater than 0'.format(opt.input))
if opt.kernel <= 0: raise ValueError('Kernel size {} must be greater than 0'.format(opt.kernel))
if opt.stride <= 0: raise ValueError('Stride {} must be greater than 0'.format(opt.stride))
if opt.pad < 0: raise ValueError('Padding {} must be non-negative'.format(opt.pad))
if opt.dilation <= 0: raise ValueError('Dilation {} must be greater than 0'.format(opt.dilation))

print(opt)
output_size = ((opt.input - (opt.kernel + (opt.kernel - 1) * (opt.dilation - 1))+ 2 * opt.pad) // opt.stride) + 1
print('Output Size: ' + str(output_size))

