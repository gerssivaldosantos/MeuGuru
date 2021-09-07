
class SistemaLivros:
    def __init__(self, dados):
        print("""        
 __  __ _       _           ____  _ _     _ _       _                 
|  \/  (_)     | |         |  _ \(_) |   | (_)     | |                
| \  / |_ _ __ | |__   __ _| |_) |_| |__ | |_  ___ | |_ ___  ___ __ _ 
| |\/| | | '_ \| '_ \ / _` |  _ <| | '_ \| | |/ _ \| __/ _ \/ __/ _` |
| |  | | | | | | | | | (_| | |_) | | |_) | | | (_) | ||  __/ (_| (_| |
|_|  |_|_|_| |_|_| |_|\__,_|____/|_|_.__/|_|_|\___/ \__\___|\___\__,_|
                                                                      
                                                                      
 """)
        self.dados = dados
        self.handler()

    def handler(self):

        self.listar_livros()

    def listar_livros(self):
        for dado in self.dados:
            titulo = dado["titulo"]
            autor = dado["autor"]
            print(f"Título: {titulo}\nAutor: {autor}\n\n")
    


SistemaLivros([
    {
    "titulo":"Ansiedade, O mal do século",
    "autor":"Augusto Cury"
    },
    {
    "titulo":"As seis lições",
    "autor":"Ludwig Von Mises"
    }
    
    ])