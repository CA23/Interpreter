import Calc
from Calc import Interpret
from Calc import Tokenizer
def main():
    while True:
        try:
            text = raw_input('Calculate > ')
        except EOFError:
            #EOFError is raised when raw_input() ends without reading any data
            #For instance a Ctrl + D ends current read which could rasie an EOF
            break
        if not text:
            #if no text is entered
            continue
        expression = Interpret(text)
        result = expression.evaluate()
        print result


if __name__ == "__main__":
    main()
