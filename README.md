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

Note:Do not use j as a variable.it is being used for complex number handling
```python
term1 = term('2x')# 2x
#exponent in terms
term2 = term('2x²')# 2x²
term3 = term('2x2')# also works
#supports multiple variables
term4 = term('2x2y3')# 2x²y³
# suports negative coefficients
term5 = term('-2x3')# -2x³
#supports complex exponents and coefficients
term6 = term('2x2+2j')# 2x²⁺²ⁱ
term7 = term('3+1jx3')# (3+1j)x³
```
Accesssing properties
```python
t1 = term('2x3+2jy4+3j') # 2x³⁺²ⁱy⁴⁺³ⁱ
# coefficient
t1.coefficiente # 2
# variables
t1.variables # list of the variables,in alphabetic order
t1.variables[0].letra # x
t1.variables[0].exponente # (3+2j)
```
## Supported Operations 
sum 
---
substraction is supported the same way
```python
sum1 = term('2x') + term('3x')# 5x
sum2 = term('2x') + term('2y')# 2x + 2y
# supports integer,float or decimal sums
sum3 = term('3x') + 4 # 3x + 4
# supports complex sums
sum4 = term('3x2+1j') + term('3x3+2j') # 3x²⁺¹ⁱ + 3x³⁺²ⁱ
#supports sums with complex numbers
sum5 = term('3x2+1j') + 5-2j # 3x²⁺¹ⁱ + (5-2j)
```
 multiplication
 ---
```python
mul1 = term('2x') * 4# 8x
mul2 = term('2x') * term('3x')# 6x²
mul3 = term('2x') * term('3y')# 6xy
mul4 = term('2xy') * term('3yz')# 6xy²z
mul5 = term('3x1+3j') * term('3x')# 9x²⁺³ⁱ
mul6 = term('3x1+3j') * (2+1j) # (6+3j)x¹⁺³ⁱ
mul7 = term('3x1+3j') * term('3x2+4j')#9x³⁺⁷ⁱ
```
division
---
```python
div1  = term('4x')/2 # 2x
div2 = term('4x')/term('2x')# 2
div3 = term('4x2')/term('4x')# x
div4 = term('4x')/term('4x2')# xᐨ¹
div5 = term('4x2')/term('4x2')# 1
```

Exponentiation
---
```python
exp1 = term('2x')**2 #4x²
exp2 = term('2x')**-1 # 0.5xᐨ¹
exp2 = term('2x')**term('2x')# not supported
exp3 = term('2x')**2.5 # 5.656854249492381x⁵ᐟ²
```
polynoms
---
example
```python
pol1 = term('2x') + term('3y') # 2x + 3y
pol2 = term('2x') - 2 # 2x - 2
# polynom properties
pol2.variables # list of terms
pol2.variables[0] # 2x
pol2.variables[1] # -2
# sum
pol4 = pol1 + pol2 #  4x + 3y - 2
# multiplication
pol5 = pol1 * pol2 # 4x² + 6xy + -4x + -6y'
# exponentiation
pol6 = pol1**2 # 4x² + 12xy + 9y²
pol7 = pol1**2.5 # non-integer powers are not yet supported
pol8 = pol1**pol2 # not supported
div1  = pol1/2 # x + 1.5y
div2 = pol1/term('2x')# 1 + 1.5xᐨ¹y
div3 = pol1/pol2 # not supported
```
substituting numbers to the variables
---
```python
term1 = term('2y')
pol1 = term('2x') + term('3y')
term1.plot(y=2) # 4
pol1.plot(x=2,y=3)# 13
# univ sets every variable which does not has a value to its value
pol1.plot(univ=5) # 25 (x=5,y=5)
pol1.plot(x=2,univ=4) # 16 (only replaces y,x is set to 2)
```
accessing properties on terms
```python
t1 = term('2x²y')
t1.coefficiente # acceses the coefficient (2)
t1.variables # accesses the list of variables (returns [x²,y])
t1.variables[0].letra # x
t1.variables[0].exponente # 2
```
accessing properties on polynoms
```python
t1 = term('2x²y')
t2 = 2
p1 = t1 + t2 # 2x²y + 2
p1.variables # [term(2x²y),2]
for i in p1:
    print(i) 
    #  iterating a polynom iterates over the list of terms
    #  it contains 
# term() objects cannot be iterated over
```
polynoms support sum, substraction, multiplication and exponents as terms do.


have fun!









