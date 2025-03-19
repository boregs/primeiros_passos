while True: 
    boas_vindas = input("Bem vindo ao PetPele's, aqui você encontra os gatinhos mais lindos para a adoção! Deseja vê-los? ")
    gatos = ["Pele", "Elza", "Dom", "Cisca", "Ze", "Flokis"]
    ficha_gatos = {
        "Pele": ["idade:" "12", "sexo:" "Macho", "Personalidade:" "Docil, Carinhoso, Amigavel"],
        "Elza": ["idade:" "14", "sexo:" "Fêmea", "Personalidade:" "Brava, Carinhosa, Não tão amigavel"],
        "Dom": ["idade:" "5", "sexo:" "Macho", "Personalidade:" "Quieto, Anti-social"],
        "Cisca": ["idade:" "7", "sexo:" "Fêmea", "Personalidade:" "Aventureira, Amigavel, Caçadora"],
        "Ze": ["idade:" "16", "sexo:" "Macho", "Personalidade:" "Quieto, Calmo, Amigavel"],
        "Flokis": ["idade:" "8", "sexo:" "Fêmea", "Personalidade:" "Amigavel, Brava, Mia Bastante"],
    }
    if boas_vindas.lower() == "sim":
        for item in gatos:
            print(item)
    else: print("Que pena! Espero que mude de ideia!")
    while True: 
        escolha_do_car = input("Escolha um dos gatos para continuar: ")
        gato_escolhido = (escolha_do_car)
        if escolha_do_car in gatos:
            print(f"Você escolheu o(a) {gato_escolhido}! Aqui está sua ficha.")
            for item in ficha_gatos[gato_escolhido]:
                print(item)
        else: print("Infelizmente esse gato não está no nosso sistema.")
        while True:
            adotar_gato = input(f"Você deseja adotar {gato_escolhido}? ")
            if adotar_gato.lower() == "sim":
                print(f"Parabéns! Adoção aceita! Agradecemos seu apoio!")
                break
            else: adotar_gato_nao = input("Você deseja voltar ao inicio? ")
            if adotar_gato_nao.lower() == "sim":
                break
            else: saida_do_usuario = input("Que pena! Deseja sair? ")
            if saida_do_usuario.lower() == "sim":
                break
        break
    continue     
    
    
        
        