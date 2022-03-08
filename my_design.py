
#isNumber
def isInteger(token):
  if "." not in token:
    try:
      token = int(token)
      return True
    except:
      return False
  else:
    return False


#isReal
def isReal(token):
  if "." in token:
    return True
  else:
    return False 

#isBoolean
def isBool(token):
  return token == "true" or token == "false"

#isString
def isString(token):
  return token[0] == '"' and token[len(token)-1] == '"'


#isKeyword checks for c++ keywords
def isKeyword(token):
  key = ["include", "iostream", "using namespace std", "main", "int", "double", "float", "switch", "do", "return", "for", "while"]
  if token.lower() in key:
    return True
  else:
    return False
  
#Separator
def isSeparator(token):
  sep = ["#","{", "}", ",", "(", ")" ,">>","<<", ";"]
  if token in sep:
    return True
  else:
    return False 

#Operator
def isOperator(token):
  operator = ["<", ">", "<=", ">=", "*", "+", "-", "/", "=", "-=", "*=", "+=", "/=", "++", "--", "==" ," "]
  if token in operator:
    return True
  else:
    return False 

#puncuation
def isPunctuation(token):
  if token == ";":
    return True
  else:
    return False

#isIdentifier
def isIdentifier(token):
  if token[0] != '"':
    return True
  else:
    return False


