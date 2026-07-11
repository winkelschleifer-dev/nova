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

variables = {}

try:
    with open(fileName + ".nova") as file:
        data = file.read()

except FileNotFoundError:
    print("File error: file does not exist")
    exit()


lines = data.splitlines()

lineNum = 0

for raw_line in lines:
    line = raw_line.strip()
    lineNum += 1

    if not line or line.startswith("$"):
        continue

    parts = line.split(maxsplit=4)
    keyword = parts[0]


    # MAKE

    if keyword == "make":

        if len(parts) != 5 or parts[3] != "=":
            print(
                f"Syntax error (line {lineNum}): expected 'make <type> <name> = <value>'"
            )
            break


        var_type = parts[1]
        var_name = parts[2]
        value = parts[4]


        if var_type == "text":
            variables[var_name] = {
                "type": "text",
                "value": value
            }


        elif var_type == "int":
            try:
                variables[var_name] = {
                    "type": "int",
                    "value": int(value)
                }
            except ValueError:
                print(f"Value error (line {lineNum}): expected integer")
                break


        elif var_type == "float":
            try:
                variables[var_name] = {
                    "type": "float",
                    "value": float(value)
                }
            except ValueError:
                print(f"Value error (line {lineNum}): expected float")
                break


        elif var_type == "bool":

            if value == "true":
                bool_value = True

            elif value == "false":
                bool_value = False

            else:
                print(
                    f"Value error (line {lineNum}): expected true or false"
                )
                break


            variables[var_name] = {
                "type": "bool",
                "value": bool_value
            }


        else:
            print(
                f"Type error (line {lineNum}): unknown type '{var_type}'"
            )
            break



    # SET

    elif keyword == "set":

        if len(parts) != 4 or parts[2] not in ("=", "+=", "-=", "*="):
            print(
                f"Syntax error (line {lineNum}): expected 'set <name> <operator> <value>'"
            )
            break


        var_name = parts[1]
        operator = parts[2]
        value = parts[3]


        if var_name not in variables:
            print(
                f"Name error (line {lineNum}): variable '{var_name}' is not defined"
            )
            break


        var = variables[var_name]


        if operator == "=":

            if var["type"] == "int":
                var["value"] = int(value)

            elif var["type"] == "float":
                var["value"] = float(value)

            elif var["type"] == "bool":
                if value == "true":
                    var["value"] = True
                elif value == "false":
                    var["value"] = False
                else:
                    print(
                        f"Value error (line {lineNum}): expected true or false"
                    )
                    break

            else:
                var["value"] = value



        elif operator == "+=":

            if var["type"] == "text":
                var["value"] += value

            elif var["type"] == "int":
                var["value"] += int(value)

            elif var["type"] == "float":
                var["value"] += float(value)

            else:
                print(
                    f"Value error (line {lineNum}): cannot add to boolean"
                )
                break



        elif operator == "-=":

            if var["type"] == "int":
                var["value"] -= int(value)

            elif var["type"] == "float":
                var["value"] -= float(value)

            else:
                print(
                    f"Value error (line {lineNum}): cannot subtract from this type"
                )
                break



        elif operator == "*=":

            if var["type"] == "int":
                var["value"] *= int(value)

            elif var["type"] == "float":
                var["value"] *= float(value)

            else:
                print(
                    f"Value error (line {lineNum}): cannot multiply this type"
                )
                break



    # SAY

    elif keyword == "say":

        output = line[len("say"):].strip()

        if output in variables:
            print(variables[output]["value"])

        else:
            print(output)



input()