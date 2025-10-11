import sys

def run_piyucesh_line(line, variables):
    line = line.strip()

    if line.startswith("print "):
        to_print = line[6:].strip()
        if to_print.startswith('"') and to_print.endswith('"'):
            print(to_print[1:-1])
        elif to_print.startswith('+'):
            # Print variable with + prefix (e.g., "print +sum")
            var_name = to_print[1:].strip()
            print(variables.get(var_name, f"<undefined:{var_name}>"))
        else:
            # Handle both " + " and " +" (without space after +) for variables
            parts = []
            if " +" in to_print:
                # Split on " +" to handle cases like "text" +variable
                temp_parts = to_print.split(" +")
                for i, part in enumerate(temp_parts):
                    if i == 0:
                        parts.append(part.strip())
                    else:
                        # This part starts with the variable name after +
                        parts.append("+" + part.strip())
            else:
                # Handle traditional " + " splitting
                parts = to_print.split(" + ")
            
            result = ""
            for part in parts:
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):
                    result += part[1:-1]
                elif part.startswith('+'):
                    # Handle +variable syntax
                    var_name = part[1:].strip()
                    result += str(variables.get(var_name, f"<undefined:{var_name}>"))
                else:
                    result += str(variables.get(part, f"<undefined:{part}>"))
            print(result)

    elif line.startswith("ask "):
        parts = line.split(" in ")
        question = parts[0][4:].strip()
        var_name = parts[1].strip()
        variables[var_name] = input(question + ": ")

    elif " plus " in line and " in " in line:
        # Handle syntax: "5 plus 4 in sum" or "num1 plus num2 in sum"
        parts = line.split(" in ")
        operation_part = parts[0].strip()
        var_name = parts[1].strip()
        
        # Split by "plus" to get operands
        operands = operation_part.split(" plus ")
        if len(operands) == 2:
            left = operands[0].strip()
            right = operands[1].strip()
            
            # Convert to numbers, handling both literals and variables
            try:
                left_val = float(variables.get(left, left))
                right_val = float(variables.get(right, right))
                result = left_val + right_val
                # Store as int if it's a whole number, otherwise as float
                variables[var_name] = int(result) if result.is_integer() else result
            except ValueError:
                print(f"Error: Cannot perform addition with '{left}' and '{right}'")

    elif " minus " in line and " in " in line:
        # Handle syntax: "10 minus 4 in sum" or "num1 minus num2 in sum"
        parts = line.split(" in ")
        operation_part = parts[0].strip()
        var_name = parts[1].strip()
        
        # Split by "minus" to get operands
        operands = operation_part.split(" minus ")
        if len(operands) == 2:
            left = operands[0].strip()
            right = operands[1].strip()
            
            # Convert to numbers, handling both literals and variables
            try:
                left_val = float(variables.get(left, left))
                right_val = float(variables.get(right, right))
                result = left_val - right_val
                # Store as int if it's a whole number, otherwise as float
                variables[var_name] = int(result) if result.is_integer() else result
            except ValueError:
                print(f"Error: Cannot perform subtraction with '{left}' and '{right}'")

    elif " into " in line and " in " in line:
        # Handle syntax: "5 into 4 in product" or "num1 into num2 in product"
        parts = line.split(" in ")
        operation_part = parts[0].strip()
        var_name = parts[1].strip()
        
        # Split by "into" to get operands
        operands = operation_part.split(" into ")
        if len(operands) == 2:
            left = operands[0].strip()
            right = operands[1].strip()
            
            # Convert to numbers, handling both literals and variables
            try:
                left_val = float(variables.get(left, left))
                right_val = float(variables.get(right, right))
                result = left_val * right_val
                # Store as int if it's a whole number, otherwise as float
                variables[var_name] = int(result) if result.is_integer() else result
            except ValueError:
                print(f"Error: Cannot perform multiplication with '{left}' and '{right}'")

    elif " by " in line and " in " in line:
        # Handle syntax: "20 by 4 in quotient" or "num1 by num2 in quotient"
        parts = line.split(" in ")
        operation_part = parts[0].strip()
        var_name = parts[1].strip()
        
        # Split by "by" to get operands
        operands = operation_part.split(" by ")
        if len(operands) == 2:
            left = operands[0].strip()
            right = operands[1].strip()
            
            # Convert to numbers, handling both literals and variables
            try:
                left_val = float(variables.get(left, left))
                right_val = float(variables.get(right, right))
                
                # Check for division by zero
                if right_val == 0:
                    print("Error: Division by zero")
                else:
                    result = left_val / right_val
                    # Store as int if it's a whole number, otherwise as float
                    variables[var_name] = int(result) if result.is_integer() else result
            except ValueError:
                print(f"Error: Cannot perform division with '{left}' and '{right}'")

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
