def  perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
# Had to follow ALX checkmarks to use this code for here, remember it can be made cleaner than this
            if num2 != 0 :
                return num1/num2
            elif num2 == 0:
                return "Error"
            else: 
                return "Well done"
            