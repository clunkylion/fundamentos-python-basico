
    #La función recibirá un string del tipo "(aaa)(b)", con letras y paréntesis. Debes retornar true si los paréntesis están balanceados, 
    #false si no. Balanceados implica número equivalente de cierres y aperturas, pero en el orden correcto. 
    #Ejemplos True: "(aa)(bb)" -> true. "( ( ) )" -> true 
    #Ejemplos False: "(" -> False, ")(" -> False "(()" -> False

def BalanceParenthesis(Str):
    stack = []
    for char in Str:
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            top_element = stack.pop()
            if not Compare(top_element, char):
                return False
    if len(stack) != 0:
        return False
    return True

def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False

if __name__ == "__main__":
    string = str(input("Ingresa un String : "))
    print(BalanceParenthesis(string))
