import json


# Load stock data from JSON file
def carregarDadosEstoque():
    try:
        with open('stock_data.json') as file:
            stockData = json.load(file)
    except FileNotFoundError:
        stockData = {}
    return stockData


def carregarDadosVendidos():
    try:
        with open('sales_report.json') as file:
            salesData = json.load(file)
    except FileNotFoundError:
        salesData = {}
    return salesData


# Save stock data to JSON file
def saveStockData(stockData):
    with open('stock_data.json', 'w') as file:
        json.dump(stockData, file)


def saveSoldData(stockData):
    with open('sales_report.json', 'w') as file:
        json.dump(stockData, file)


def mostrarRelatorioVendas(stock_data):
    print("Produtos vendidos:")
    for nome, produto in stock_data.items():
        print(
            f"Nome: {nome}, Preço vendido: {produto['preco']}, Quantidade vendida: {produto['quantidade']}")


# Create a new product in the stock
def criarProduto(stockData, soldData):

    while True:
        nome = input("Digite o nome do produto: ")
        if nome.strip() == "":
            print("O nome do produto não pode ser vazio. Tente novamente.")
        if nome in stockData:
            print("O produto já está em estoque.")
        else:
            break

    while True:
        try:
            tipo = input("Tipo do produto: ")
            if tipo.strip() == "":
                print("O tipo do produto não pode ser vazio. Tente novamente.")
            else:
                break
        except ValueError:
            print("Input inválido. Insira um valor válido.")

    while True:
        try:
            preco = float(input("Preço do produto: "))
            if (preco < 0):
                print("Preço não pode ser menor do que zero!")
            else:
                break
        except ValueError:
            print("Input inválido. Digite um número válido para o preço.")

    while True:
        try:
            quantidade = int(input("Quantidade do produto: "))
            if quantidade < 0:
                print("Quantidade tem que ser maior do que zero. Tente novamente")
            else:
                break
        except ValueError:
            print("Input inválido. Insira um valor válido.")

    stockData[nome] = {'preco': preco, 'tipo': tipo, 'quantidade': quantidade}
    saveStockData(stockData)
    soldData[nome] = {'preco': 0, 'quantidade': 0}
    saveSoldData(soldData)
    print(f"Produto '{nome}' adicionado ao estoque.")

# Update an existing product in the stock


def atualizarProduto(stockData):
    while True:
        nome = input("Digite o nome do produto a ser atualizado: ")
        if nome.strip() == "":
            print("O nome do produto não pode ser vazio. Tente novamente.")
        else:
            break

    if nome in stockData:

        while True:
            try:
                preco = float(input("Preço do produto atualizado: "))
                if (preco < 0):
                    print("Preço não pode ser menor do que zero!")
                else:
                    break
            except:
                print("Input inválido. Insira um valor válido.")

        while True:
            try:
                tipo = input("Tipo do produto atualizado: ")
                if tipo.strip() == "":
                    print("O tipo do produto não pode ser vazio. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Input inválido. Insira um valor válido.")

        while True:
            try:
                quantidade = int(input("Quantidade do produto atualizado: "))
                if quantidade < 0:
                    print("Quantidade tem que ser maior do que zero. Tente novamente")
                else:
                    break
            except ValueError:
                print("Input inválido. Insira um valor válido.")
        stockData[nome]['preco'] = preco
        stockData[nome]['tipo'] = tipo
        stockData[nome]['quantidade'] = quantidade
        saveStockData(stockData)

        print(f"Produto '{nome}' atualizado no estoque.")
    else:
        print(f"Produto '{nome}' não encontrado.")


# Delete a product from the stock


def deletarProduto(stockData, soldData):
    while True:
        nome = input("Digite o nome do produto a ser deletado: ")
        if nome.strip() == "":
            print("O nome do produto não pode ser vazio. Tente novamente.")
        else:
            break
    if nome in stockData:
        del stockData[nome]
        saveStockData(stockData)
        # del soldData[nome]
        # saveSoldData(soldData)
        print(f"Produto '{nome}' deletado do estoque.")
    else:
        print(f"Produto '{nome}' não encontrado.")

# Display the current stock data


def mostrarEstoque(stockData):
    print("Estoque atual:")
    for nome, produto in stockData.items():
        print(
            f"Nome: {nome}, Preco: {produto['preco']}, Quantidade: {produto['quantidade']}")

# Main program loop


# Sell a product from the stock
def venderProduto(stockData, soldData):
    nomeProduto = input("Digite o nome do produto a ser vendido: ")

    if nomeProduto in stockData:
        quantidadeDisponivel = stockData[nomeProduto].get('quantidade', 0)
        if quantidadeDisponivel > 0:
            while True:
                try:
                    quantidadeVendida = int(
                        input("Digite a quantidade a ser vendida: "))
                    if quantidadeVendida <= 0 or quantidadeVendida > quantidadeDisponivel:
                        print(
                            "Quantidade inválida. Digite um valor entre 1 e ", quantidadeDisponivel)
                    else:
                        break
                except ValueError:
                    print(
                        "Input inválido. Digite um número válido para a quantidade.")

            # Update stock data
            stockData[nomeProduto]['quantidade'] -= quantidadeVendida
            saveStockData(stockData)

            # Calculate total price sold
            precoUnidade = stockData[nomeProduto].get('preco', 0)
            precoVendidoTotal = precoUnidade * quantidadeVendida

            soldData[nomeProduto]['quantidade'] += quantidadeVendida
            soldData[nomeProduto]['preco'] += precoVendidoTotal

            saveSoldData(soldData)

            print(
                f"Foram vendido {quantidadeVendida} unidades de {nomeProduto} por um total de R${precoVendidoTotal:.2f}")
            print("Estoque atualizado.")
        else:
            print("O produto está fora de estoque.")
    else:
        print("Produto não encontrado.")

# Main program loop


def main():
    stockData = carregarDadosEstoque()
    soldData = carregarDadosVendidos()

    while True:
        print("\nSistema de estoque: ")
        print("1. Criar um produto")
        print("2. Atualizar um produto")
        print("3. Deletar um produto")
        print("4. Mostrar estoque")
        print("5. Vender um produto")
        print("6. Relatório de vendas")
        print("7. Exit")

        escolha = input("Escolha alguma ação (1-7): ")

        if escolha == '1':
            criarProduto(stockData, soldData)
        elif escolha == '2':
            atualizarProduto(stockData, soldData)
        elif escolha == '3':
            deletarProduto(stockData, soldData)
        elif escolha == '4':
            mostrarEstoque(stockData)
        elif escolha == '5':
            venderProduto(stockData, soldData)
        elif escolha == '6':
            mostrarRelatorioVendas(soldData)
        elif escolha == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
