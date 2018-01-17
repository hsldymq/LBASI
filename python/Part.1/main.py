import token
import interpreter

def main():
    while True:
        try:
            text = input('calc:> ')
        except EOFError:
            break

        if not text:
            continue
        intp = interpreter.Interpreter(text)
        result = intp.express()

        print(result)

if __name__ == '__main__':
    main()

