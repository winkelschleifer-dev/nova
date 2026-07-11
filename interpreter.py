print("----    ----   --------   ---    ---     ------  ")
print("*****   ****  **********  ***    ***    ********   ")
print("------  ---- ----    ---- ---    ---   ----------  ")
print("************ ***      *** ***    ***  ****    **** ")
print("------------ ---      --- ---    ---  ------------ ")
print("****  ****** ****    ****  ********   ************ ")
print("----   -----  ----------    ------    ----    ---- ")
print("****    ****   ********      ****     ****    **** ")

for _ in range(0, 5):
	print()

print("Nova Language interpreter v0.0.2a")

for _ in range(0, 5):
	print()





fileName = input("<NOVA> Please type in the file name (without .nova extension): ")

file = open(fileName + ".nova")
  
variables = {}



data = file.read()
lines = data.splitlines()

lineNum = 0
for raw_line in lines:
  line = raw_line.strip()
  lineNum += 1
  
  if not line or line.startswith("$"):
    continue
  
  parts = line.split(maxsplit=4)
  keyword = parts[0]
  if keyword == "make":
    if len(parts) != 5 or parts[3] != "=":
      print(f"Syntax error (line {lineNum}): expected 'make <type> <name> = <value>'")
      break
    else:
      if parts[1] == "text":
        variables[parts[2]] = {
        "type": parts[1],
        "value": str(parts[4])
        }
      elif parts[1] == "int":
        variables[parts[2]] = {
        "type": parts[1],
        "value": int(parts[4])
        }
      elif parts[1] == "float":
        variables[parts[2]] = {
        "type": parts[1],
        "value": float(parts[4])
        }
      elif parts[1] == "bool":
        variables[parts[2]] = {
        "type": parts[1],
        "value": bool(parts[4])
        }
    
  elif keyword == "set":
    if len(parts) != 4 or parts[2] not in ("=", "+=", "-=", "*="):
      print(f"Syntax error (line {lineNum}): expected 'set <name> <operator> <value>'")
      break
    elif parts[1] not in variables:
      print(f"Name error (line {lineNum}): variable '{parts[1]}' is not defined")
      break
    else:
      if parts[2] == "=":
        variables[parts[1]]["value"] = parts[3]
      elif parts[2] == "+=":
        if variables[parts[2]]["type"] == "text":
          variables[parts[2]]["value"] += parts[3]
        elif variables[parts[2]]["type"] == "int":
          variables[parts[2]]["value"] += int(parts[3])
        elif variables[parts[2]]["type"] == "float":
          variables[parts[2]]["value"] += float(parts[3])
        else:
          print(f"Value error (line {lineNum}): cannot add to boolean")
      elif parts[2] == "-=":
        if variables[parts[2]]["type"] == "text":
          print(f"Value error (line {lineNum}): cannot substract from text")
        elif variables[parts[2]]["type"] == "int":
          variables[parts[2]]["value"] -= int(parts[3])
        elif variables[parts[2]]["type"] == "float":
          variables[parts[2]]["value"] -= float(parts[3])
        else:
          print(f"Value error (line {lineNum}): cannot substract from boolean")
      else:
        if variables[parts[2]]["type"] == "text":
          print(f"Value error (line {lineNum}): cannot multiply text")
        elif variables[parts[2]]["type"] == "int":
          variables[parts[2]]["value"] *= int(parts[3])
        elif variables[parts[2]]["type"] == "float":
          variables[parts[2]]["value"] *= float(parts[3])
        else:
          print(f"Value error (line {lineNum}): cannot multiply boolean")


  elif keyword == "say":
    output = line[len("say"):].strip()
    print(output)