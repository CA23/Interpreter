class Tokenizer:

    def __init__(self, type, value):
        self.type = type
        self.value = value
    


    def __str__(self):
        
        #defining the __str__ method to return what would technically be expected from the
        #__repr__ method

        return 'Tokenizer({type}, {value})'.format(type = self.type, value = self.value)

class Interpret:

    def __init__(self, text):

        self.text = text
        self.position = 0
        self.current = None

    def error(self):
            raise Exception('Error parsing line')

    def get_next(self):
            #Tokenizer/Lexical analyzer

        text = self.text

        if self.position > len(text) - 1:
            return Tokenizer(None, None)

        #setting the final token to None at the end of text

        ch_current = text[self.position]

        #checking to see if the character is a digit or an operator

        if ch_current.isdigit():
            #create a token as an instance of Tokenizer with its type and value
            token  = Tokenizer('INTEGER', int(ch_current))
            self.position = self.position + 1
            return token

        if ch_current == '+':
            token = Tokenizer('PLUS', ch_current)
            self.position  = self.position + 1
            return token

        self.error()

    def process(self, token_type):
                # check if the current token type is the same as the passed token type 
                #if yes, set current token to next token otherwise raise error

        if self.current.type == token_type:
            self.current = self.get_next()
        else:
            self.error()

    def evaluate(self):
        self.current = self.get_next()
        #assign the current to left
        left = self.current
        self.process('INTEGER')
        #recall that process checks for a type and if it matches, sets
        #current token to next token
        #so, now current token is the next token/char in the text input
        operation = self.current
        #now we have a digit as a left token, operator as a right
        self.process('PLUS')
        #checks if the current is an operator, sets the next token as current
        right = self.current
        self.process('INTEGER')
        #now after this process the current is set to None, left is a digit, operation is the middle token and right
        #is another digit.

        result  = left.value + right.value
        #evaluate and assign to result
        return result

    

