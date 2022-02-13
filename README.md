# algebra

##  Install with [PyPi](https://pypi.org/)
```
pip install algebra.py
```
## How to use
### Importing
```python
from algebra.components import term
```
### Initializing
Note: to see the output shown in the comments you need to run `print()` or `str()` at the answer
```python
term1 = term('2x')# 2x
#exponent in terms
term2 = term('2x²')# 2x²
term3 = term('2x2')# also works
#supports multiple variables
term4 = term('2x2y3')# 2x²y³
# suports negative coefficients
term5 = term('-2x3')# -2x³
```
### Supported Operations 
sum 
---
substraction is supported the same way
```python
sum1 = term('2x') + term('3x')# 5x
sum2 = term('2x') + term('2y')# 2x + 2y
# support for integer sum
sum3 = term('3x') + 4 # 3x + 4
```
 multiplication
 ---
```python
mul1 = term('2x') * 4# 8x
mul2 = term('2x') * term('3x')# 6x²
mul3 = term('2x') * term('3y')# 6xy
mul4 = term('2xy') * term('3yz')# 6xy²z
```
division
---
```python
div1  = term('4x')/2 # 2x
div2 = term('4x')/term('2x')# 2
div3 = term('4x2')/term('4x')# x
div4 = term('4x')/term('4x2')# not supported yet
div5 = term('4x2')/term('4x2')# not supported yet
```

Exponentiation
---
```python
exp1 = term('2x')**2 # supported
exp2 = term('2x')**-1 #not supported
exp2 = term('2x')**term('2x')# not supported
exp3 = term('2x')**2.5# not supported
```
polynoms
---
example
```python
pol1 = term('2x') + term('3y') # 2x + 3y
pol2 = term('2x') - 2 # 2x - 2
# sum
pol4 = pol1 + pol2 #  4x + 3y - 2
# multiplication
pol5 = pol1 * pol2 #  supported
# exponentiation
pol6 = pol5**2 # supported
pol7 = pol5**2.5 # not supported
pol8 = pol6**pol5 # not supported
```
polynoms support sum, substraction, multiplication and exponents as terms do.
division is not supported

have fun!









