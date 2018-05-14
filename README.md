# convcalculator
## Made by Trevor Tsue


### Caculates convolution output size
output = ((input - size + 2 * pad) // stride) + 1
#### Where
##### input = Input size
##### size = Kernel size
##### stride = stride
##### pad = 0-padding

### Use
python convcalc.py --input 128 --size 3 --stride 1 --pad 1

### Output
Output Size: 64
