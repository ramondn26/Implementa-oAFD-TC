# Instruções de uso

    Para fornecer os dados que serão usados na criação do AFD, a seguinte sintaxe deve ser seguida:
    - Os estados usados nos testes foram do formato "q(n)" onde n >= 0 (seguindo o padrão do material da disciplina LFA);
    - O alfabeto é fornecido símbolo a símbolo separado por espaços;
    - O número (inteiro) de transições que será o critério de parada para a repetição de leitura das transições;
    - Definição do estado inicial;
    - Definição dos estados finais, separando-os por espaço caso seja mais de um estado de aceitação;
    - Cadeia que será testada no autômato fornecido.


# Exemplo de uso
Informe os estados separados por espaço: q0 q1 q2
Informe o alfabeto separado por espaço: a b
Informe o número de transições: 4
Informe as transições: 
q0 b q0
q0 a q1
q1 a q1
q1 b q2
Informe o estado inicial: q0
Informe os estados de aceitação separados por espaço: q2
Informe uma cadeia para testar (ou 'sair' para finalizar): bbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaab
Aceita