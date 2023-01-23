def date_to_hour(date):
    result = 0
    for i, v in enumerate(date):
        v = int(v)
        if i == 0:
            result += v * 24
        elif i == 1:
            result += v * 730
        elif i == 2:
            result += v * 8760
    return result


class Pessoa:
    def __init__(self):
        self.livro = None

    def multa_check(self):
        if self.livro:
            prazo_horas = date_to_hour(self.livro.prazo.split("/"))
            dia_horas = date_to_hour(self.livro.dia.split("/"))

            if prazo_horas - dia_horas >= 730:
                self.livro.preco = int(self.livro.preco + (self.livro.preco * 0.01))
                print("Multa aplicada: ")
                print(round(self.livro.preco - (self.livro.preco * 0.01)), "->", self.livro.preco, "\n")
                return
            print("Multa nao aplicada \n")
        else:
            print("Sem livro registrado \n")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.clientes = []

    def adicionar_livro(self, livro):
        if livro is Livro and livro:
            self.livros.append(livro)

    def ordenar_livros(self):
        datas_horas = []
        datas = []
        for livro in self.livros:
            datas_horas.append(date_to_hour(livro.data_lancamento.split("/")))
            datas.append(livro.data_lancamento)

        for i in range(len(datas_horas)):
            for j in range(len(datas_horas)):
                if datas_horas[i] > datas_horas[j]:
                    auxiliar = datas_horas[i]
                    datas_horas[i] = datas_horas[j]
                    datas_horas[j] = auxiliar

                    auxiliar = datas[i]
                    datas[i] = datas[j]
                    datas[j] = auxiliar

        for data in datas:
            print(data)
        print("\n")

    def livro_autor(self):
        autores = {}

        for livro in self.livros:
            if livro.autor not in autores:
                autores[livro.autor] = [livro.nome]
            else:
                autores[livro.autor].append(livro.nome)

        for key in autores:
            print(key + ":")
            for livro in autores[key]:
                print(livro)
            print("\n")

    def multas(self):
        for i, cliente in enumerate(self.clientes):
            print("Cliente", i)
            cliente.multa_check()

    def alugar_livro(self, livro, cliente):
        self.clientes[cliente].livro = livro


class Livro:
    def __init__(self, nome, autor, data_lancamento, preco, prazo, dia):
        self.nome = nome
        self.autor = autor
        self.data_lancamento = data_lancamento
        self.preco = preco
        self.prazo = prazo
        self.dia = dia


def main():
    pessoa1 = Pessoa()
    pessoa2 = Pessoa()
    pessoa3 = Pessoa()

    biblioteca = Biblioteca()

    livro1 = Livro("LivroNome", "Gustavo", "12/8/2024", 100, "10/3/2023", "10/3/2022")
    livro2 = Livro("rodrigo", "gisele", "22/1/2023", 20, "1/1/2023", "2/1/2023")
    livro3 = Livro("pedro", "gisele", "22/1/2023", 20, "1/1/2023", "2/1/2023")

    biblioteca.livros.append(livro1)
    biblioteca.livros.append(livro2)
    biblioteca.livros.append(livro3)

    biblioteca.clientes.append(pessoa1)
    biblioteca.clientes.append(pessoa2)
    biblioteca.clientes.append(pessoa3)

    biblioteca.alugar_livro(biblioteca.livros[0], 0)
    biblioteca.alugar_livro(biblioteca.livros[1], 1)

    # a)
    biblioteca.multas()

    # b)
    biblioteca.ordenar_livros()

    # c)
    biblioteca.livro_autor()

    return 0


if __name__ == '__main__':
    main()
