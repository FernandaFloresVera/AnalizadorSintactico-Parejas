from lark import Transformer, Token, Tree

class MyTransformer(Transformer):
    def __init__(self):
        self.token_counts = {} 
        #se inicializa un diccionario vacio
        # llamado tokens_counts 
        # para almaDcenar los tokens

    def add_token(self, token_type, token_value): #agrerar un token al diccionario token_counts
        if token_type not in self.token_counts:
            self.token_counts[token_type] = 0
        self.token_counts[token_type] += 1
        #token_type es el tipo de token, como una cadena de caracteres
        #token_value es el valor del token
        #si el tipo de token no esta presente en el diccionario se inicializa con un recuento de 0
        #luego se incrementa el recuento para ese tipo de token



    def start(self, items):
        for item in items:
            self._process_item(item)
            #metodo de entrada para la transformaciin
            #recibe una lista de elementos 'items' y los procesa uno x uno llamando al metodo 'process_item"
        


    def _process_item(self, item):
        if isinstance(item, Token):
            self.add_token(item.type, item)
        elif isinstance(item, Tree):
            for child in item.children:
                self._process_item(child)
                
    #procesa un elemento individual
    #si el elemento es un token (token)se agrega al diccionario de recuento usando el metodo token
    #si el elemento es un arbol (tree) se procesan recursivamenre todos sus hijos llamando de nuevo a _process_item

    def get_token_counts(self):
        return self.token_counts
    
    #devuelve un diccionario token_counts que contiene el recuneto de tokens 
    #Este código define la clase MyTransformer que puede ser utilizada para contar los tokens presentes en un análisis sintáctico.pu