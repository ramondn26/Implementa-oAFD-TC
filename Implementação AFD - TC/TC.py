# Implementação de AFD 
# Aluno: Ramon Damasceno Nascimento
# Matrícula: 202220180

#-------------------------------------------------------------------------------------------------------

# Construtor da classe
# Neste código, o AFD é criado a partir das informações fornecidas pelo usuário.

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estadoInicial, estadosAceitacao):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes  
        self.estadoInicial = estadoInicial
        self.estadosAceitacao = set(estadosAceitacao)

    def verificacao(self, cadeia):
        estado_atual = self.estadoInicial
        for simbolo in cadeia:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                return False
        return estado_atual in self.estadosAceitacao

# Os dados são solicitados ao usuários em formatos padronizados
def entradaDados():
    estados = input("Informe os estados separados por espaço: ").split()
    alfabeto = input("Informe o alfabeto separado por espaço: ").split()
    quantTansicoes = int(input("Informe o número de transições: "))
    
    print("Informe as transições: ")
    transicoes = {}
    for _ in range(quantTansicoes):
        origem, simbolo, destino = input().split()
        transicoes[(origem, simbolo)] = destino

    estadoInicial = input("Informe o estado inicial: ")
    estadosAceitacao = input("Informe os estados de aceitação separados por espaço: ").split()

    return estados, alfabeto, transicoes, estadoInicial, estadosAceitacao

def main():
    estados, alfabeto, transicoes, estadoInicial, estadosAceitacao = entradaDados()
    afd = AFD(estados, alfabeto, transicoes, estadoInicial, estadosAceitacao)
    
    while True:
        cadeia = input("Informe uma cadeia para testar (ou 'sair' para finalizar): ")
        if cadeia.lower() == 'sair':
            break
        resultado = afd.verificacao(cadeia)
        print("Aceita" if resultado else "Rejeitada")

if __name__ == "__main__":
    main()
