sala1c1 = [100, [], "Pulp Fiction"]
sala2c1 = [150, [], "Kill Bill"]
sala3c1 = [200, [], "Django"]
sala1c2 = [100, [], "Deuce Bigalow: American Gigalow"]
sala2c2 = [4000,[1,2,3], "Balas e Bolinhos"]
sala3c2 = [20,[2,7,8,19],"Hungover"]


cinema1 = [sala1c1, sala2c1, sala3c1]
cinema2 = [sala1c2,sala2c2,sala3c2]

def listar(cinema):
    for sala in cinema:
        print(sala[2])

def disponivel(cinema,filme,lugar):
    for sala in cinema:
        if filme==sala[2]:
            if lugar < 0 or lugar > sala[0]:
                print("N/E")

            elif lugar in sala[1]:
                print ("Indisponivel")
            else:
                print ("disponivel")
             

def vendebilhete(cinema,filme,lugar):
    UploadedCinema=cinema
    for sala in UploadedCinema:
        if sala[2]==filme:
            if lugar not in sala[1]:
                sala[1].append(lugar)
            else: print ("lugar ocupado")

                
    return UploadedCinema

vendebilhete(cinema2,"Hungover",15)


def listarDisponibilidades(Cinema):
    print("Filmes em exposição:")
    for sala in Cinema:
        x= sala[0] - len(sala[1]) 
        
        print(sala[2] + ", com "+str(x)+" disponiveis.")
    return  

listarDisponibilidades(cinema1)  
        



def inserirSala( cinema, sala, lotação, filme ):
    salanova=[lotação,[],filme]
    nomesala=str(sala)
    
    
    if salanova not in cinema:
        cinema.append(salanova)
    print("Sala nova adicionada")
    print(f"{nomesala}: com lotação de "+str(salanova[0])+" lugares. Filme em exibição: "+salanova[2],flush=True)
    

    return 
inserirSala(cinema1,sala1c1, 100, "Barbie")

MENU=-1
print("""Bom dia! Obrigado por escolher o nosso Cinema, aqui estão os próximos passos: 
      (1) Listar todos os filmes em exibição;
      (2) Verificar a disponibilidade da sala e do lugar;
      (3) Comprar bilhete, somente após verificar a disponibilidade;
      (4) Listar os lugares restantes em cada sala;
      (5) Adiciona uma sala ao cinema;
      (6) Fechar o MENU.""")

while MENU !=6:
    MENU=int(input("Escolhe a tua opção."))

    if MENU==1:
        listar(cinema1)

    elif MENU ==2:
        filmeM=input("Escolhe o filme que queres ver")
        lugarM=int(input("Escolhe um lugar da sala"))
        print(filmeM,lugarM)

        disponivel(cinema1,filmeM,lugarM)


    elif MENU ==3:
        vendebilhete(cinema1,input("Escolhe o filme que queres ver"), input("Insira o lugar3"))

    
    elif MENU ==4:
        listarDisponibilidades(cinema1)

    elif MENU ==5:
        inserirSala(cinema1,input("Qual o nome da nova sala?"),int(input("Qual a lotação da sala?")),input(("Qual o filme em exibição?")))
    
print("Obrigado")


