# convcalculator
## Made by Trevor Tsue


### Caculates convolution output size
output = ((input - kernel + 2 * pad) // stride) + 1
#### Where
##### input = Input size
##### kernel = Kernel size
##### stride = stride of kernel movement
##### pad = 0-padding

### Use
python convcalc.py 128 3 --stride 1 --pad 1

### Output
Output Size: 64
