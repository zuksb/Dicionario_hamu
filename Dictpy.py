def criar_dict():
    with open('dicionario.txt', 'a', encoding='utf-8') as dicionario:
        pass
    return "Dicionário criado com sucesso"

def procurar(palavra_pesquisada):
    with open("dicionario.txt", "r", encoding="utf-8") as dicionario:
        for linha in dicionario:
            linha_limpa = linha.strip()
            if not linha_limpa:
                continue
            partes = linha_limpa.split(":")
            palavra_hamu = partes[0]
            palavra_portugues = partes[1]

            if palavra_pesquisada.lower() == palavra_hamu.lower():
                return f"Palavra '{palavra_pesquisada}' encontrada! Tradução: {palavra_portugues}"
            
            if palavra_pesquisada.lower() == palavra_portugues.lower():
                return f"Palavra '{palavra_pesquisada}' encontrada! Tradução: {palavra_hamu}"
                
        return f"Palavra '{palavra_pesquisada}' não encontrada no dicionário"
    
def adicionar(): 
    palavra_hamu = input("Digite a palavra em HAMU: ").strip()
    palavra_portugues = input("Digite a tradução em PORTUGUÊS: ").strip()
    
    with open("dicionario.txt", "a", encoding="utf-8") as dicionario:
        dicionario.write(f"{palavra_hamu}:{palavra_portugues}\n")
        print("Palavra adicionada com sucesso!")
while True:
    pergunta = input("Voce deseja criar um dicionario, escrever no dicionario, procurar no dicionario ou sair?").strip().lower()
    if pergunta == "criar":
        criar_dict(input("Digite o conteúdo do dicionário: "))
    elif pergunta == "escrever":    
        adicionar()
    elif pergunta == "procurar":
        palavra_pesquisada = input("Digite a palavra que deseja procurar: ").strip()
        resultado = procurar(palavra_pesquisada)
        print(resultado)    
    elif pergunta == "sair":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha 'criar', 'escrever', 'procurar' ou 'sair'.")