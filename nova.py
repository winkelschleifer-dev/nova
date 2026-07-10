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

print("Nova Language interpreter v0.1a")

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
      variables[parts[2]] = {
      "type": parts[1],
      "value": parts[4]
      }
    
  elif keyword == "set":
    if len(parts) != 4 or parts[2] not in ("=", "+=", "-=", "*="):
      print(f"Syntax error (line {lineNum}): expected 'set <name> <operator> <value>'")
      break
    elif parts[1] not in variables:
      print(f"Name error (line {lineNum}): variable '{parts[1]}' is not defined")
      break
  elif keyword == "say":
    output = line[len("say"):].strip()
    print(output)
  