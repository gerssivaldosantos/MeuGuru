def busca(setor,matriz):
        """Recebe o nome de um setor junto a uma matriz
        que armazena os dados de funcionários e busca 
        os funcionários que pertecem a este setor
        : str, list -> list
        """
        retorno_busca = []
        for linha in range(len(matriz)):
            if matriz[linha][2] == setor:
                item = [matriz[linha][0],matriz[linha][1],matriz[linha][3]]
                retorno_busca.append(item)
        return retorno_busca