import sys

def run_piyucesh_line(line, variables):
    line = line.strip()

    if line.startswith("print "):
        to_print = line[6:].strip()
        if to_print.startswith('"') and to_print.endswith('"'):
            print(to_print[1:-1])
        else:
            parts = to_print.split(" + ")
            result = ""
            for part in parts:
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):
                    result += part[1:-1]
                else:
                    result += str(variables.get(part, f"<undefined:{part}>"))
            print(result)

    elif line.startswith("ask "):
        parts = line.split(" into ")
        question = parts[0][4:].strip()[1:-1]
        var_name = parts[1].strip()
        variables[var_name] = input(question + ": ")

def run_piyucesh_file(filename):
    variables = {}
    with open(filename, "r") as f:
        for line in f:
            run_piyucesh_line(line, variables)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: piyucesh <filename.piy>")
    else:
        run_piyucesh_file(sys.argv[1])
