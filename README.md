# algebra
not yet on [PyPi](https://pypi.org/algebra-math-py/0.0.1/)
##  Install with [TestPyPi](https://test.pypi.org/)
```
pip install -i https://test.pypi.org/simple/ algebra-math-py
```
## How to use
### Importing
```python
from algebra.component import term
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
brackets  are fully supported.<br/>
have fun!









