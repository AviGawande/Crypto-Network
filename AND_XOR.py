def apply_operations(input_string, operation):
    result = ""
    for char in input_string:
        result += chr(ord(char) ^ operation)
    return result

input_string = "Hello World"
operation = 127

result_and = apply_operations(input_string, operation)
result_or = apply_operations(input_string, operation)

print(f"Original String: {input_string}")
print(f" Result of AND operation with 127: {result_and}")
print(f"Result of OR operation with 127: {result_or}")
