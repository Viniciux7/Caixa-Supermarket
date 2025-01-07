class Caixa:
    def _init_(self):
        self.produtos = {}
        self.carrinho = {}
        self.total = 0

    def menu(self):
        while True:
            print('Bem-vindo à Caixa!')
            print('1. Cadastrar produto')
            print('2. Adicionar ao carrinho')
            print('3. Remover do carrinho')
            print('4. Ver carrinho')
            print('5. Pagar')
            print('6. Sair')

            try:
              escolha = int(input('Escolha: '))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            if escolha == 1:
                self.cadastrar_produtos()
            elif escolha == 2:
                self.add_carrinho()
            elif escolha == 3:
                self.exibir_carrinho()
            elif escolha == 4:
              self.ver_carrinho()
            elif escolha == 5:
                self.pagamento()
            elif escolha == 6:
                self.sair()
                break
            else:
                print('Escolha inválida.')

    def cadastrar_produtos(self):  
          
        self.codigo = int(input('Digite o código do Produto: '))

        if self.codigo in self.produtos or self.codigo < 100:
          print('Código já cadastrado ou é menor que 3 dígitos, cadastre outro.')
          self.codigo = int(input('Digite o código do Produto: '))


        self.nome = input('Nome do Produto: ')
        self.preco = float(input('Preço do Produto: '))
        self.quantidade = int(input('Quantidade do Produto: '))
        self.produtos[self.codigo] = {'nome': self.nome, 'preco': self.preco, 'quantidade': self.quantidade}
        print('Produto cadastrado com sucesso.')


    def add_carrinho(self):
        codigo_add = int(input('Digite o código do produto no qual deseja adicionar ao carrinho: '))

        if codigo_add not in self.produtos:
            print('Produto não encontrado.')
            codigo_add = int(input('Digite o código do produto no qual deseja adicionar ao carrinho: '))

        quantidade_add = int(input('Digite a quantidade no qual deseja adicionar ao carrinho: '))

        if quantidade_add > self.produtos[codigo_add]['quantidade']:
            print('Quantidade insuficiente no estoque.')
            return

        if codigo_add in self.carrinho:
            self.carrinho[codigo_add]['quantidade'] += quantidade_add
        else:
            self.carrinho[codigo_add] = {
                'nome': self.produtos[codigo_add]['nome'],
                'preco': self.produtos[codigo_add]['preco'],
                'quantidade': quantidade_add
            }

        self.produtos[codigo_add]['quantidade'] -= quantidade_add
        print(f"Foi adicionado {quantidade_add} unidade(s) de {self.produtos[codigo_add]['nome']} ao carrinho.")

    def remover_carrinho(self):
        codigo_remover = int(input('Digite o código do produto no qual deseja remover do carrinho: '))

        if codigo_remover not in self.carrinho:
            print('Produto não está no carrinho.')
            return

        quantidade_remover = int(input('Digite a quantidade no qual deseja remover do carrinho: '))

        if quantidade_remover > self.carrinho[codigo_remover]['quantidade']:
            print(f"Erro! Remova uma quantidade menor ou igual a {self.carrinho[codigo_remover]['quantidade']}.")
            return

        self.carrinho[codigo_remover]['quantidade'] -= quantidade_remover

        if self.carrinho[codigo_remover]['quantidade'] == 0:
            del self.carrinho[codigo_remover]

        self.produtos[codigo_remover]['quantidade'] += quantidade_remover
        print(f"Foi removido {quantidade_remover} unidade(s) de {self.produtos[codigo_remover]['nome']} do carrinho.")

    def exibir_carrinho(self):
        if not self.carrinho:
            print('O carrinho está vazio.')
            return

        print('Itens no carrinho:')
        for codigo, item in self.carrinho.items():
            print(f"Código: {codigo} | Nome: {item['nome']} | Quantidade: {item['quantidade']} | Preço: R${item['preco']:.2f}")

    def pagamento(self):
        self.total = sum(item['quantidade'] * item['preco'] for item in self.carrinho.values())
        print(f'Total: R${self.total:.2f}.\n Como deseja pagar?')
        print('1 - Cartão de Crédito')
        print('2 - Cartão de Débito')
        print('3 - Dinheiro')

        try:
            self.escolha_pag = int(input('Escolha a opção no qual deseja pagar: '))
        except ValueError:
            print("Por favor, digite um número válido.")
            return

        if self.escolha_pag == 1:
            print('Cartão de Débito.')
            print(f'Valor: {self.total}')
            input('Digite a senha do seu Cartão de Débito: ')
            print('Compra aprovada.')
        elif self.escolha_pag == 2:
            print('Cartão de Crédito.')
            print('Deseja pagar a vista ou parcelado:')
            self.escolha_p = int(input('1- A vista \n2- Parcelado'))

            if self.escolha_p == 1:
                print(f'Valor: {self.total}')
                input('Digite a senha do cartão: ')
                print('Compra aprovada.')

            elif self.escolha_p == 2:
                print(f'Valor: {self.total}')
                for i in range(1, 11):
                    self.parcelas = self.total / i
                    print(f'{i}x = {self.parcelas: .2f}')

                self.parcela = int(input('Deseja dividir em quantas parcelas? '))
                self.valor = float(self.total / self.parcela)
                print(f'Você escolheu {self.parcela} parcela(s) no valor de R$ {self.valor: .2f}.')
            else:
                print('Opção inválida.')
                return

        elif self.escolha_pag == 3:
            print('Dinheiro.')
            print(f'Valor: {self.total}')
            self.dinheiro = float(input('Valor pago?'))

            if self.dinheiro < self.total:
                print("Valor insuficiente. Operação cancelada.")
                return

            self.troco = self.dinheiro - self.total
            print(f'Devolva {self.troco: .2f}.')
        
        self.carrinho.clear()  
        self.total = 0  
        print('Compra finalizada com sucesso!')


    def sair(self):
        print("Encerrando o programa. Obrigado!")
        exit()

if __name__ == "_main_":
  caixa = Caixa()
  caixa.menu()