ascii_list = []

É_Inteira = input("Deseja imprimir toda tabela ASCII? (s/n) \n")
if É_Inteira == "s" or É_Inteira == "S":
    for i in range(32, 127):
        ascii_list.append(chr(i))
if É_Inteira == "n" or É_Inteira == "N":
    print("Para imprimir a tabela ASCII em um intervalo especifico, você deve especificar onde dará inicio a impressão e onde ela acabará.")
    Inicio = input("Insira em que posição (32 a 127) da tabela a impressão deve ser iniciada: ")
    Fim = input("Insira em que posição (32 a 127) da tabela a impressão deve ser encerrada: ")
    try:
        for i in range(int(Inicio), int(Fim)):
            ascii_list.append(chr(i))
    except:
        raise ValueError("Os argumentos devem ser números inteiros entre 32 e 127.")

print(ascii_list)