file_dir = "files/"

def generate_standard_archives(file_name):
    edges = open(file_dir+"graph_edge.net", "w")       #arquivo onde serao guardados as linhas
    vertex = open(file_dir+"graph_vertex.net", "w")    #arquvo onde serao guardados os vertices
    arq = open(file_dir + file_name, "r")      #arquivo de leitura

    arq.readline()                             #primeira leitura: uma linha que indica a leitura de vertices

    while True:
        itens = arq.readline().split("\"")        #separa a linha em 3 itens : numero, nome e qtd de artigos
        if(len(itens) == 1):            #para na leitura que indica edges
            break
        else:
            vertex.write(itens[0].replace(" ", "/")+itens[1]+itens[2].replace(" ", "/")) #escreve cada separando com o "/
    while True:
        line = line = arq.readline()
        itens = line.split(" ")
        if (len(itens) == 1):           #para na leitura que indica triangle
            break
        else:
            edges.write(line.replace(" ", "/"))
    arq.close()
    vertex.close()
    edges.close()

menu = 1
while (menu != 0):
    vertex_file = str(input("Digite o nome do arquivo do dataset: "))
    generate_standard_archives(vertex_file)
    menu = eval(input("Digite 0 para sair: "))
    if menu == 0:
        exit(0)
