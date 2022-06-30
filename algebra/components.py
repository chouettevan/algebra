import decimal
from fractions import Fraction
from decimal import Decimal, DecimalTuple
from multiprocessing import set_forkserver_preload
from multiprocessing.connection import answer_challenge
exponents_table = {
  '⁴':'4',
  '⁰':'0',
  '¹':'1',
  '²':'2',
  '³':'3',
  '⁵':'5',
  '⁶':'6',
  '⁷':'7',
  '⁸':'8',
  '⁹':'9',
  'ᐟ':'/',
  'ᐨ':'-'
}
numbers_table = {value:key for key,value in exponents_table.items()}
class polynomio():
  def __init__(self,variables):
    self.v = []
    for i,char in enumerate(variables):
      if i != 0:
        self.v.append(' + ')      
      self.v.append(char)      
    self.variables = list(variables)
  def __str__(self):
    var = list(self.v)
    var = list(map(lambda v:str(v) or '1',var))
    return ''.join(var)
  def __iter__(self):
    return iter(self.variables)
  def __len__(self):
    return len(self.variables)
  def simplify(self):
    return sum(self.variables)
  
  def plot(self,**var):
    answer = 0
    for member in self:
      if type(member) == term:
        answer += member.plot(**var)
      elif type(member) in [int,float,Decimal]:
        answer += member 
    return answer    
    
  def __add__(self,other):
    if type(other) in [int,float,Decimal]:
      check = False
      answer = list(self.variables)
      for i,t in enumerate(answer):
        if type(t) in [int,float,Decimal]:
          answer[i] += other 
          check = True
          break
      if not check:
        answer.append(other)
      return polynomio(answer)  
    if type(other) == polynomio:
      answer = list(self.variables)
      answer.extend(other.variables)
      return polynomio(answer).simplify()  
    else:
      answer = list(self.variables)
      _ = 0
      for i,char in enumerate(answer):
        if type(other) == term and char.compatible(other):
          answer[i] = other + char
          if answer[i].coefficiente == 0:
            del answer[i]  
          _ = 1
          break
        elif type(other) == int and type(char) == int:
          answer[i] += other
          if answer[i].coefficiente == 0:
            del answer[i]  
          _ = 1
          break
      if _ == 0:
        answer.append(other)    
      return polynomio(answer)
  def __sub__(self,other):
    second = -other
    return self + second 
  def __neg__(self):
    return self*-1  
  def __truediv__(self,other):
    return self * other**-1
  def __radd__(self,other):
    return self + other 
  def __rmul__(self,other):
    return self * other 
  def __rsub__(self,other):
    return -1*(self - other)
  def __getitem__(self,items):
    return self.variables[items]
  def __rtruediv__(self,other):
    return (self/other)**-1
  def __pow__(self,other):
    answer = 1
    for i in range(other):
      answer *= self
    answer.variables = list(filter(bool,answer.variables))  
    return answer  
  def __mul__(self,other):
    if type(other) != polynomio:
      var = []
      for i in self:
        var.append(other * i) 
      return polynomio(var).simplify()
    else:
      answer = self*other[0]
      for i in other[1:]:
        answer += self*i
      return answer.simplify()
      
      
      
class term():
  letterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  def __init__(self,txt):
    for i in txt:
      if i in self.letterlist:
        s = i 
        break
    index = txt.index(s)
    try:
      self.coefficiente = float(txt[:index])
    except ValueError:
      self.coefficiente = 1
    l = []
    for  i in self.letterlist:
      if i in txt:
        l.append(txt.index(i))
    l.sort()     
    self.variables = []
    if len(l) == 1:
      self.variables.append(variable(txt[l[0]:]))
    else:
      for a,b in zip(l[:-1],l[1:]):
        if txt[a:b]:
          self.variables.append(variable(txt[a:b]))
      self.variables.append(variable(txt[b:]))     
      self.variables.sort(key=lambda i:i.letra) 
    if self.coefficiente == int(self.coefficiente):
      self.coefficiente = int(self.coefficiente)  
    self.variables = [var for var in self.variables if var.exponente != 0]  
  def compatible(self,other):
    if type(other) == term:
      if self.variables == other.variables:
        return True
    return False

  def __add__(self,other):
    if other:
      if self.compatible(other):
        s = ''.join([str(i) for i in self.variables])
        return term(f'{ self.coefficiente + other.coefficiente }{s}')
      else:
        return polynomio([self,other])
    else:
      return self    
  def mulcomp(self,other):
    if [i.letra for i in self.variables] == [i.letra for i in other.variables]:
      return True
    return False   
  def __mul__(self,other):
    if other and self:
      if type(other) == term:
        if self.mulcomp(other):
          varses = []
          for v,v2 in zip(self.variables,other.variables):  
            varses.append(v*v2)  
        else:
          varses = []
          v2 = 0
          others = [i.letra for i in other.variables]
          selfs = [i.letra for i in self.variables]
          for v in self.variables:
            if v.letra in others:
              for i in other.variables:
                v2 = 0
                if v.letra == i.letra:
                  varses.append(v*i)       
          for o in other.variables:
            if o.letra not in selfs:
              varses.append(o)
          for s in self.variables:
            if s.letra not in others:
              varses.append(s)
        sa = ''.join([str(i) for i in varses])
        return term(f'{self.coefficiente*other.coefficiente}{sa}')
      elif type(other) in [int,float,Decimal]:
        s = "".join([str(i) for i in self.variables])
        return term(f'{self.coefficiente*other}{s}')
    else:
      return 0   
  def __pow__(self,other):
    if other == 0:
      return 1
    answer = term(str(self))
    answer.coefficiente = answer.coefficiente**other
    if answer.coefficiente == int(answer.coefficiente):
      answer.coefficiente = int(answer.coefficiente)
    for variable in answer.variables:
      variable.exponente *= other
    return answer  

  def plot(self,**var):
    answer = 1
    for variable in self.variables:
      answer *= variable.plot(**var)
    answer *= self.coefficiente 
    return answer 


  def __str__(self):
    s = ''.join([str(i) for i in self.variables])
    coff = self.coefficiente if self.coefficiente != 1 else ''
    return f'{coff}{s}'
  def __abs__(self):
    if self.coefficiente < 0 :
      return -self
    else:
      return self  
  def __bool__(self):
    return bool(self.coefficiente)
  def __sub__(self,other):
    return self + -other
  def __neg__(self):
    return self * -1
  def __truediv__(self,other):
    if self.compatible(other):
      answer = self.coefficiente/other.coefficiente
      if answer == int(answer):
        return int(answer)
      return answer  
    return self * other**-1
  def __radd__(self,other):
    return self + other 
  def __rmul__(self,other):
    return self * other 
  def __rsub__(self,other):
    return -1*(self - other)
  def __rtruediv__(self,other):
    return (self/other)**-1
  def __eq__(self,o):
    try:
      if self.coefficiente == o.coefficiente:
        if self.compatible(o):
          return True 
      return False     
    except:
      return False

class variable():
  def __init__(self,txt):
    self.letra = txt[0]
    try:  
      self.exponente = int(txt[1:])
    except ValueError:
      exp = ''
      for i in txt[1:]:
        try:
          exp += exponents_table[i]
        except KeyError:
          pass
      try:
        self.exponente = int(exp) 
      except ValueError:
        try:
          self.exponente = Decimal(txt[1:])
        except decimal.InvalidOperation:
          self.exponente = 1 
  def __str__(self):
    exp = ''
    if type(self.exponente) in [Decimal,float]:
      exps = Decimal(str(self.exponente))
      txt = str(Fraction(exps))
      new_txt = ''
      for i in txt:
        new_txt += numbers_table[i]
      return f'{self.letra}{new_txt}'  
    if self.exponente != 1:
      for i in str(self.exponente):
        exp += numbers_table[i] 
    return f'{self.letra}{exp}' 
  def plot(self,**var):
    if self.letra in var.keys():
      return var[self.letra]**self.exponente
    elif "univ" in var.keys():
      return var["univ"]**self.exponente  
    else:
      return 1

  def __mul__(self,other):
    if self.letra == other.letra:
      return variable(f'{self.letra}{self.exponente + other.exponente}')
  def __eq__(self,o):
    if self.letra == o.letra:
      if self.exponente == o.exponente:
        return True
    return False 
if __name__ == '__main__':
  import unittest
  from test.comp import Algebra_tests
  Algebra_tests.term = term
  unittest.main()



                
