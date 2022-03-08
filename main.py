#Lexcial Analyzer in Python
from my_design import *

#------------------------------
def lexer(file):

  inicode = list()
  #readfile
  with open(file, 'r') as f:
    for line in f:
      for word in line.split():
        inicode.append(word)
  print(inicode)
  
  #Separator any Separator that are together.
  code = list()
  for each in range(len(inicode)):
    for l in inicode[each]:
      if isSeparator(l):
        #split the Separator
        code.append(l)
        inicode[each] = inicode[each].replace(l,'')
        

    code.append(inicode[each])      

  #Code list contains each individual lexeme

  #Dictionary to store each token as key and lexeme as values
  lexer = {
    "Integer": [],
    "Real": [],
    "Keyword": [],
    "Separator": [],
    "Operator": [],
    "Punctuation": [],
    "Identifier": []
  }
  
  #isInteger
  #isReal
  #isKeyword
  #isSeparator 
  #isOperator 
  #isPunctuation
  #isIdentifier

  
  #Classify each in code array
  for lexeme in code:
    if isReal(lexeme):
      lexer["Real"].append(lexeme)
    elif isInteger(lexeme):
      lexer["Integer"].append(lexeme)
    elif isKeyword(lexeme):
      lexer["Keyword"].append(lexeme)
    elif isPunctuation(lexeme):
      lexer["Punctuation"].append(lexeme)
    elif isSeparator(lexeme):
      lexer["Separator"].append(lexeme)
    elif isOperator(lexeme):
      lexer["Operator"].append(lexeme)
    elif isIdentifier(lexeme):
      lexer["Identifier"].append(lexeme)
    else:
      print("Ad-hoc not included")
  
  #print(lexer)
  #Output to a file
  f = open("output_JerryLiu.txt", 'w')

  #setup
  f.write("Token               Lexeme\n")
  f.write("--------------------------\n")

  for token in lexer:
    f.write(token + "-------------" + str(lexer[token]) + '\n')
  
  f.close()
  #print(code)

#lexer(file) 
#Parameter file is a .txt file
lexer('input_soucecode.txt')