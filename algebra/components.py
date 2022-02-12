exponents_table = {
  '⁴':4,
  '⁰':0,
  '¹':1,
  '²':2,
  '³':3,
  '⁵':5,
  '⁶':6,
  '⁷':7,
  '⁸':8,
  '⁹':9,
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
    return ''.join([str(i) for i in self.v])
  def __iter__(self):
    return iter(self.variables)
  def __len__(self):
    return len(self.variables)
  def simplify(self):
    return sum(self.variables)
  def __add__(self,other):
    if type(other) == polynomio:
      answer = self.variables
      answer.extend(other.variables)
      return polynomio(answer).simplify()  
    else:
      answer = self.variables
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
  endedInit = False
  def __init__(self,txt):
    for i in txt:
      if i in self.letterlist:
        s = i 
        break
    index = txt.index(s)
    try:
      self.coefficiente = int(txt[:index])
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
    self.endedInit = True 
  def compatible(self,other):
    if type(other) == term:
      if self.variables == other.variables:
        return True
    return False
  def __setattr__(self,name,value):
    if not self.endedInit:
      self.__dict__[name] = value

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
      elif type(other) == int:
        s = "".join([str(i) for i in self.variables])
        return term(f'{self.coefficiente*other}{s}')
    else:
      return 0   
  def __pow__(self,other):
    answer = self
    answer.coefficiente = answer.coefficiente**other
    for variable in answer.variables:
      variable.exponente *= other
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
          exp += str(exponents_table[i])
        except KeyError:
          pass
      try:
        self.exponente = int(exp) 
      except ValueError:
        self.exponente = 1     
  def __str__(self):
    exp = ''
    if self.exponente != 1:
      for i in str(self.exponente):
        exp += numbers_table[int(i)] 
    return f'{self.letra}{exp}' 
  def __mul__(self,other):
    if self.letra == other.letra:
      return variable(f'{self.letra}{self.exponente + other.exponente}')
  def __eq__(self,o):
    if self.letra == o.letra:
      if self.exponente == o.exponente:
        return True
    return False 


                
