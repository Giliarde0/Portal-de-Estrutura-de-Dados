print()
print("A estrutura List pode ser usada para varias coisas que estão nos exemplos abaixo:")
print()
print("Este exemplo de lista, ao executar demonstra todos os numeros presentes no Colchete.")
a = list(["1","2","3","4","5","6","7","8","9","10"])
print(a)
print()
print()

print("Este exemplo demonstra os nomes que estão dentro da lista")
empresas = list(["apple", "samsung", "nike"])
print(empresas)
print()
print()


print("Este exemplo de lista separa letra por letra da palavra dentro do parenteses.")
b = list("LISTA")
print(b)
print()
print()

print("Esta lista percorre todos os elementos de 1 ao 10.")
c = list(range(1,11))
print(c)
print()
print()

#Alterando um elemento da lista.
print("Podemos alterar qualquer elemento da lista, por qualquer outro escolhido da seguinte forma:")
jogadores = ["neymar","messi","cr7",]
print(jogadores)
print("Depois de alterar o elemento da lista ficara assim:")
jogadores[2] = "luva de pedreiro"
print(jogadores)
print()
print()

print("Também é possivel acessar um elemento da lista ")
nomes = ["gilberto", "Geovana", "Marcos", "Mara"]
print(nomes)
print(nomes[2])
print()

print("Também é possivel acessar os elementos de trás para frente. Segue o exemplo abaixo:")
nomes = ["gilberto", "Geovana", "Marcos", "Mara"]
print(nomes)
print(nomes[-3])

print()
print()

print("É possivel selecionar qualquer elemento da lista, inclusive o ultimo elemento da lista")
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(letras[-1])

print()

#Este exercicio é sobre a função LEN
print("A função LEN ela serve para contar e demonstrar a quantidade de elementos dentro da propria lista:")
print("Azul,", "Vermelho,", "Laranja,", "Amarelo,", "Azul.")
print("Atravez da Função Len, será demonstrado abaixo quantos elementos há dentro da lista:")
cor = ["azul ","vermelho", "laranja", "amarelo", "azul"]
print(len(cor))

print()
print()


print("A função start, step e stop serve para selecionar intervalos e também para alterar \n elementos de uma lista que são especificados, caso não seja especificado ele inciara o retorno atraves de zero. Segue os exemplos abaixo")
print("Elementos da lista: A,B,C,D,E,F,G,H:")
print("Selecionando os primeiros quatro elementos da lista:")
letras = (["A", "B", "C", "D", "E", "F", "G", "H"])
print(letras[0:4])
print("Selecionando os quatro ultimos elementos da lista:")
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(letras[-4:])
print("Selecionando apenas elementos pares:")
letras = (["A", "B", "C", "D", "E", "F", "G", "H"])
print(letras[::2])
print()
print("Selecionando apenas elementos impares:")
letras = (["A", "B", "C", "D", "E", "F", "G", "H"])
print(letras[1::2])
print()
print("Selecionando em ordem inversa:")
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(letras[::-1])
print()
print()

print("Exemplo de alteração de elemento:")
print("Os elementos dentro da lista são: 0,1,2,3,4,5,6,7,8")
lista = [0, 1, 2, 3, 4, 5, 7, 8]
lista[1:4] = ["joão", "pedro"]
print(lista)
print()
print()


#Operador IN
print("Verificação de inclusão de elemento, ou seja, com o operador de inclusão # in # podemos verificar \n"
      "se o elemento está na lista ou não, se estiver o operador retorna # true # e se não,\n"
      "o operador retorna # false # "
      ".Segue o exemplo abaixo:")
print("Estas são as cidades da lista: são paulo, rio de janeiro, minas gerais, brasilia, gramado:")
print()
print("Agora irei pedir para verificar a inclusão da cidade de são paulo")
cidades = ["são paulo", "rio de janeiro", "minas gerais", ",brasilia", "gramado"]
print("são paulo" in cidades)
print()
print()

print("APPEND")
print("A função append serve para inserir um elemento no final da lista. Segue o exemplo abaixo:")
itens = [""]
itens.append("caneta")
print(itens)
itens.append("caneca")
print(itens)
itens.append("controle")
print(itens)
print()
print()

print("INSERT")
print("A função insert serve para inserir um elemento em uma posição especifica da lista. \n"
      " Segue o exemplo abaixo:")
marcas = ["Apple", "Samsung", "Microsoft", "Nike", "Adidas"]
marcas.insert(2, "Hurley")
print(marcas)
print()
print()

print("INDEX")
print("O metodo index é usada para obter a posição de um elemento em uma lista. Segue o exemplo abaixo:")
esportes = ["Futebol", "Vôlei", "Basquete", "Natação" ]
print(esportes.index("Vôlei"))
print()
print()

print("REMOVE")
print("É possivel remover um elemento de uma lista usando o metodo remove. Segue o exemplo abaixo:")
restaurantes = ["paris6", "copacabana palace", "hannover", "a casa do porco"]
restaurantes.remove("a casa do porco")
print(restaurantes)
print()
print()

print("POP")
print("O metodo pop ele também pode ser utilizado para remover elementos da lista através da posição\n"
      "do elemento, assim ele retorna o item escolhido para ser removido da lisa. Segue o exemplo abaixo:")
print("Esta é a lista dos objetos: Balde,", "Sapato,", "Cadeira,", "Vaso,", "Mesa.")
objetos = ["Balde", "Sapato", "Cadeira", "Vaso", "Mesa"]
print(objetos.pop(1))
print(objetos)
print(objetos.pop(2))
print(objetos)
print()
print()

print("COUNT")
print("O metodo coutn é utilizado para contar  a quantidade de vezes que um elemento aparece em uma lista. \n"
      " Segue o exemplo a seguir:")
numeros = ["1","1","2","2","2","3","4"]
print(numeros.count("1"))
print(numeros.count("2"))
print(numeros.count("3"))
print(numeros.count("4"))
print()
print()

print("REVERSE")
print("O método reverse não recebe nenhum parâmetro e modifica automaticamente a lista. \n"
      "Segue abaixo um exemplo:")
data = ["21", "14", "27", "28", "31", "07"]
print(data)
data.reverse()
print(data)
print()
print()

print("SORT")
print("O metodo sort utiliza um padrão opicional reverse que indica se a lista deve ser ordenada \n "
"de forma crescente (False) \n" "ou decrescente (True). \n"
"Por padrão o valor desse parâmetro é False (ordenação crescente). A seguir um exemplo abaixo:")
nome = ["Gilberto", "Jõao", "Mario", "Daniel", "Pedro"]
nome.sort()
print(nome)
nome.reverse()
print(nome)
print()
print()

print("Outro exemplo de reordenação de lista. A seguir um exemplo:")
idades = [5, 25, 11, 21, 12, 56]
idades.sort()
print(idades)
idades.sort(reverse = True)
print(idades)
print()
print()

print("SORTED")
print("O metodo sorted é usado para obter uma copia ordenada de uma lista sem auterar"
      " a lista original. A seguir um exemplo:")
x = [5, 25, 11, 21, 12, 56]
print(sorted(x))
print(x)
print(sorted(x)[::1])
print()
print()

print("COPY")
print("O metodo copy ele retorna uma copia da lista. A seguir um exemplo:")
l = [10]
w = l.copy()
w.append(20)
o = w.copy()
o.append(30)
print(l)
print(w)
print(o)
print()
print()

print("+")
print("Utilizando o operador # + # é possivel concatenar uma lista, e de acordo com a \n"
"ordenada concatenação uma nova lista pode ser criado:")
geovana = ["15 anos", "1,62", "Namorada"]
marcos = ["48 anos", "1,72", "Sogro"]
mara = ["45", "1,64", "Sogra"]
print(geovana + marcos + mara)
print(mara + marcos + geovana)
print(marcos + mara + geovana)
print()
print()

print("MIN")
print("A função Min retorna o menor valor em uma lista")
num = [12, 14, 21, 17, 7]
print(min(num))
print()
print()

print("MAX")
print("A função max retorna o maior valor de uma lista. Segue o exemplo abaixo:")
m = [1.2, 2.4, 3.7, 7, 10]
print(max(m))
print()
print()

print("SUM")
print("A função sum retorna a soma de todos os valores dentro de uma lista. Segue o exemplo abaixo:")
soma = [1,2,3,4,5,6,7,8,9,10]
print(sum(soma))
print()
print()

#TUPLAS
print("TUPLAS")
print()
print("Tuplas são listas imutaveis, uma vez criadas, não podem ser alteradas, podendo"
" conter dados heterogeneos, e homogeneos\n de dados implicitos e explicitos. Segue o exemplo a seguir: ")
print("Tupla Implicita:")
cadastro = ("Jose", 2000, 2022, 9.5)
print(cadastro)
type(cadastro)
print()
print("Tupla Explicita:")
cadastro = tuple(["Jose", 2000, 2022, 9.5])
print(cadastro)
type(cadastro)
print()
print()

print("Declaração implicita:")
print()
t1 = ("p")
t2 = ("p",)
print(type(t1), type(t2))
t3 = ("j", "k", "l")
print(t3)
print()

print("Declaração explicita:")
t1 = tuple([2019])
print(t1)
t2 = tuple("GG2107")
print(t2)
# Strings também podem ser tuplas de caracteres
print()
print()

print("Erro em tupla ao modificar:")
bairro = ("Av Alziro Zarur", "Jasiel do Prado Ferreira", "Paulinho Oscar")
#bairro[1] = "Danilo de Freitas"
print("Ao tentar modificar uma tupla, essa mensagem de erro igual \n "
"a essa apareçe: TypeError: 'tuple' object does not support itemassignment")
print()
print()

print("SELEÇÃO DE ELEMENTOS NAS TUPLAS")
print("Nas tuplas também é possivel utilizar funções de listas, exceto metodos que removam \n"
",adicionem, modifiquem e  operações. Um exemplo abaixo de seleção de elemento na tupla logo abaixo:")
num = ("1", "2", "3", "4", "5", "6", "7", "8")
print(num[2])
print()
print()

print("Outro exemplo de seleção nas tuplas de um numero até o outro:")
num = ("A", "B", "C", "D", "E", "F", "G", "H")
print(num[1:4])
print()
print()

print("VERIFICAÇÃO DE ELEMENTOS NAS TUPLAS")
print("Exemplo de verficação de elemento na tupla:")
nomes = ("Geovana", "Gilberto", "Leonora", "Lucila")
print("Geovana" in nomes)
print("Gilberto" in nomes)
print("Daniel" in nomes)
print()
print()

print("Concatenando Tuplas:")
x1 = (1, 2)
x2 = (3, 4)
x3 = (5, 6)
print(x1 + x2 + x3)
print(x3 + x2 + x1)
print(x2 + x3 + x1)
print()
print()

print("Localizando um elemento na Tuplas:")
princesas = ( "Rapunzel", "Geovana", "Branca de Neve", "Cinderela")
print(princesas.index("Geovana"))
print()

print("Evitanto um erro em localização de elemento em Tupla:")
princesas = ( "Rapunzel", "Geovana", "Branca de Neve", "Cinderela")
if "Elsa" in princesas:
    print(princesas.index("Elsa"))
else:
    print("Elsa não está na tupla.")
print()
print()

print("Imprimindo todos os elementos em uma tupla de princesas, linha por linha:")
princesas = ( "Rapunzel", "Geovana", "Branca de Neve", "Cinderela")
for princ in princesas:
    print(princ)
print()
print()


print("DICIONARIOS")
print("Dicionários são estruturas de chave-valor, ou seja, os valores ou seja dados que \n"
" estão sempre associados a uma chave")
dicionario = {
1.2: True ,
123: "Um Dois Três","cat": "dog",
("X", "Y"): (2, 3, 5)
}
print()

print("Acessando um valor dentro de um dicionario")
print(dicionario)

dicionario = {
"Nome": "Ash Ketchum",
"Idade": 10,
"Profissão": "Treinador Pokémon"
}
print(dicionario["Nome"])
print(dicionario["Idade"])
print(dicionario["Profissão"])
print()

print("Metodo Get. O método get é outra forma para obter valores de um dicionário \n "
"Ele recebe como parâmetro a chave associada ao valor desejado, veja o exemplo abaixo:")
dicionario = {
"Nome": "Jõao",
"Idade": 10,
"Profissão": "Tecnico de TI"
}
print(dicionario.get("Nome"))
print(dicionario.get("Cidade"))
print()

print("Verificando o tamanho de um dicionario com Len. O tamanho de um dicionário também pode ser \n"
"verificado através da função len. Veja no exemplo abaixo:")
dicionario = {
"Nome": "Gilberto",
"Idade": 18,
"Profissão": "Treinador Pokémon"}
print(len(dicionario))
print()

print("Removendo o valor de um dicionario utilizando o metodo POP ")
dicionario = {
"Nome": "Ash Ketchum",
"Idade": 12,
"Profissão": "Treinador Pokémon",
"Cidade": "Pallet"}
profissao = dicionario.pop ("Profissão")
print(profissao)
print(dicionario)
print()

print("Removendo um valor de um dicionario com a declaração Del. \n "
"A função del pode ser utilizado para deletar um valor de um dicionario!")
dicionario = {
"Nome": "Geovana",
"Idade": 15,
"Apelido": "Geo",
"Cidade": "São Paulo"}
del dicionario["Apelido"]
print(dicionario)
