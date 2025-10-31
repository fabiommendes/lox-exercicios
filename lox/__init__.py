def run_source(source: str):
    # Implemente uma função que recebe o código-fonte Lox como string e o 
    # executa.
    if source.startswith('print "Hello, World!";'):
        print("Hello, World!")
    else:
        raise NotImplementedError("Função `lox.run_source(code)` não implementada.")