from arithmetic_operations import perform_operation

def test_perform_operation():
    # Test addition
    assert perform_operation(2, 3, 'add') == 5, "Addition failed"

    # Test subtraction
    assert perform_operation(5, 3, 'subtract') == 2, "Subtraction failed"

    # Test multiplication
    assert perform_operation(4, 3, 'multiply') == 12, "Multiplication failed"

    # Test division
    assert perform_operation(10, 2, 'divide') == 5, "Division failed"

    # Test division by zero
    result = perform_operation(5, 0, 'divide')
    assert result == "Error: Division by zero", "Division by zero not handled correctly"

    # Test invalid operation
    result = perform_operation(5, 5, 'mod')
    assert result == "Error: Invalid operation", "Invalid operation not handled correctly"

    print("All tests passed.")

if __name__ == "__main__":
    test_perform_operation()
