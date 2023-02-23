import re

def regular_expression(list):
  for string in list:
    #Integer
    if re.match("^[0-9]+$",string):
      text = "An integer."
      print("{} matches the pattern: {}".format(string,text))
    #Float    
    elif re.match("^[0-9]+\.[0-9]+$",string):
      text = "A float consists of 1 or more digits before and after decimal point."
      print("{} matches the pattern: {}".format(string,text))
    elif re.match("^[0-9]+\.[0-9][0-9]$",string):
      text = "A float with exactly 2 digits after the decimal point"
      print("{} matches the pattern: {}".format(string,text))

    elif re.match("^[0-9]+\.[0-9]+[f]$",string):
      text = "A float ending with a letter f"
      print("{} matches the pattern: {}".format(string,text))

    elif re.match("[0-9]+[0-9]+[0-9]+[a-zA-Z]+[a-zA-Z]+", string):
      text = "Exactly 3 digits, followed by at least 2 letters (capital or lowercase doesn’t matter)"
      print("{} matches the pattern: {}".format(string, text))

    elif re.match("^[A-Z]+[a-z]+[0-9]+", string):
      text = " Capital letters ( 1 or more), followed by lowercase letters (1 or more),followed by digits (0 or more) "
      print("{} matches the pattern: {}".format(string, text))

                
         
    else:
      print("{} does not match any available pattern.".format(string))
                
list= ['22.11', '23', '66.7f','123abcde', 'Case44', 'Happy', '78', '66.7', 'yes123', 'Book111']
regular_expression(list)


def removePartOfString(string):
  index = re.search(r"\d+",string)
  string = string[0:index.start()]+string[index.end():]
  print("Found integer {} starting at position {} and ending at position {}. The rest of the string is: {}".format( index.group(), index.start(), index.end(), string ))

removePartOfString("22 street")
removePartOfString("90years")
  