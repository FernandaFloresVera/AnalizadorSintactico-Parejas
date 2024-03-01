from lark import Lark
from transformador import MyTransformer

def load_grammar():
    with open("grammar.lark", "r") as file:
        return file.read()
    
#esta funcion carga la gramatica desde un archivo llamado grammar.lark
#y devuelve su contenido en una cdena de texto
#utiliza un bloque with open para abirir el archivo y asegurarse de que se cierre correctamente despues 
#de leer su contenido

def procesar_entrada(entrada):
    try:
        grammar = load_grammar()
        lexer_parser = Lark(grammar, parser='lalr')
        tree = lexer_parser.parse(entrada) 
        #print(tree.pretty()) imprime el arbol creado por la linea anterior (tambien usado para el debug, IGNORAR)
        transformer = MyTransformer()
        transformer.transform(tree)
        return transformer.get_token_counts()
    except Exception as e:
        print(e)
        raise e
    
    #toma una cadena entrada como argumento
    #intenta procesar la entrada segun la gramatica definida
    #primero carga la gramatica usando la funcion load grammar
    #luego crea un objeto 'lark' con la gramatica cargadad y especifica que se debe utilizr el analizador lalr
    #utiliza el el metodo parse del obj lark para generar un arbol sintactico a partir de la entrada
    #crea una instancia de mytransformer para transformar ek arbol sintactico
    #llama al metodo transfor de mytransformer para procesar el arbol sintactico y contar los tokens
    #devuelve el recuento de los tokens obtenido llamando al metodo get_token_counts de MyTransformer
    
    