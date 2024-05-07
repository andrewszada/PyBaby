import os 
resp = ''
carrinho_total = 0
while resp != '0':
  os.system("cls")
  print("############################################")
  print("######       Projeto SIG-Escola       ######")
  print("############################################")
  print("#####      1 - Módulo Cliente          #####")
  print("#####      2 - Módulo Vendedor        #####")
  print("#####      3 - Módulo Produto/Vendas         #####")
  print("#####      4 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  resp = input("##### Escolha sua opção: ")

  if resp == "1":
    os.system("cls")
    print(" ")
    print("_______________________________________")
    print("_______           Módulo Cliente          _______")
    print("_______________________________________")
    print("____  1 - Cadastrar Cliente              _____")
    print("_____ 2 - Exibir Dados do Cliente       _____")
    print("_____ 3 - Alterar Dados do Cliente       _____")
    print("_____ 4 - Excluir Cliente               _____")
    resp2 = input("##### Escolha sua opção: ")
    if resp2 == ("1"):
      os.system("cls")
      nome = input("Qual seria o seu nome completo? ")
      endereço = input("Qual o seu endereço completo? ")
      telefone = input("Qual o seu número de telefone? ")
      produtos = input("Qual seria os tipos de produto que seria de seu interesse? (Temos as opções de roupas, fraldas e brinquedos) ")
      metodo_de_pagamento = input("Qual seria o metodo de pagamento desejado? ")
    elif resp2 == ("2"):
      os.system("cls")
      print(nome)
      print(endereço)
      print(telefone)
      print(produtos)
      print(metodo_de_pagamento)
      n_bugar = input(" ")
    elif resp2 == ("3"):
      os.system("cls")
      nome = input("Edite seu nome ")
      endereço = input("Edite seu endereço ")
      telefone = input("Edite seu telefone ")
      produtos = input("Edite sua preferência de produtos")
      metodo_de_pagamento = input("Edite seu método de pagamento ")

  if resp == ("2"):
    os.system("cls")
    print(" ")
    print("_______________________________________")
    print("_______           Módulo Vendedor          _______")
    print("_______________________________________")
    print("____   1 - Informações do Vendedor             _____")
    print("_____  2 - Informações do CEO      _____")
    print("_____  3 - Gestão de Estoque      _____")
    
    
    if resp2 == ("1"):
      print("ANDRÉ BABY IMPORTS ")
      print("Vendedor Premium")
      print("5000+ vendas ")
      mensagem = input("Tenha um bom dia!")
    elif resp2 == ("2"):
      print("Com mestrado em administração e gestão de negócios")  
      print("André Leandro de Medeiros Araújo atua no mercado de produtos infantis a 10 anos")
      print("Com seus 33 anos, busca a cada ano satisfazer e contribuir a todas mamães e papais")
      print("(Eu já fui pai e tenho convicção em como esses produtos são caros, quero ajudar eles), disse André. ")
      bugger = input(" ")


  elif resp == '3':
    os.system("cls")
    print(" ")
    print("_______________________________________")
    print("_______           Módulo Produtos          _______")
    print("_______________________________________")
    print("____  1 - Comprar Carrinhos Para Bebê             _____")
    print("_____ 2 - Comprar Brinquedos para Bebê     _____")
    print("_____ 3 - Comprar Roupas Para Bebê      _____")
    print("_____ 4 - Mostrar Carrinho Total              _____")
    
    
    
    
    produto = input("Temos produtos dos mais variados para sua criança: CARRINHO(1), BRINQUEDOS (2), ROUPAS (3) ")
    if produto == ("1"):
      os.system("cls")
      print("POSSUIMOS CARRINHOS DE 2 MARCAS PRINCIPAIS")
      print("TEMOS DA GRACO, MARCA CUSTO BENEFÍCIO")
      print("MODELOS NA FAIXA DOS R$ 500 e R$2.500" )
      print("TEMOS O MODELO Graco Premier Modes Lux Stroller, Midtown™ Collection (1) custando R$2.200")
      print("TEMOS O MODELO Extend™ LX R129 (2) custando R$566")
      print("TEMOS O MODELO FastAction™ Fold Sport Click Connect™ Travel System (3) custando R$1700")
      escolha_graco_bugaboo = input("Se interessou por algum modelo de Graco? (S/N)")
      if escolha_graco_bugaboo == ("S"):
        os.system("cls")
        escolha_graco_2 = input("Qual dos modelos você deseja adicionar no seu carrinho")
        if escolha_graco_2 == ("1"):
          os.system("cls")
          carrinho_total += 2.200
          aviso = input("Parabéns, você adicionou Graco Premier Modes Lux Stroller, Midtown™ Collection ao seu carrinho! ")
        elif escolha_graco_2 == ("2"):
          os.system("cls")
          carrinho_total += 566
          aviso = input("Parabéns, você adicionou o Extend™ LX R129 ao seu carrinho!")      
        elif escolha_graco_2 == ("3"):
          os.system("cls")
          carrinho_total += 1700
          aviso = input("Parabéns você adicionou FastAction™ Fold Sport Click Connect™ Travel System ao seu carrinho! ")
      if escolha_graco_bugaboo == ("N"):
        os.system("cls")
        print ("BUGABOO, UMA MARCA PREMIUM, DE ALTA QUALIDADE")
        print("NOSSOS MODELOS SE ENCONTRAM NA FAIXA DE R$2000 e R$10.000 ")
        escolha_bugaboo = input("Ficou interessado? (S/N)")
        if escolha_bugaboo == ("S"):
          os.system("cls")
          print("TEMOS O Bugaboo Butterfly Ultra-Compact Stroller(1) CUSTANDO R$2.320")
          print("TEMOS O Bugaboo Donkey5 Mono Complete Stroller(2) CUSTANDO R$7.196")
          print ("TEMOS Bugaboo Fox 5 Complete Full-Size Stroller(3) CUSTANDO R$5.667")
          escolha_bugaboo_2 = input("Se interessou por algum modelo?")
          if escolha_bugaboo_2 == ("1"):
            carrinho_total += 2.320
            aviso = input("Parabéns você adicionou o Bugaboo Butterfly Ultra-Compact Stroller ao seu carrinho! ")
          elif escolha_bugaboo_2 == ("2"):
            carrinho_total += 7.196
            aviso = input("Parabéns você adicinou o  Bugaboo Donkey5 Mono Complete Stroller ao seu carrinho!")
          elif escolha_bugaboo_2 == ("3"):
            carrinho_total += 5.667
            aviso = input("Parabéns você adicionou o Bugaboo Fox 5 Complete Full-Size Stroller ao seu carrinho!")

    elif produto == ("2"):
      produtos_brinquedo = input("POSSUIMOS BRINQUEDOS DA MARCA FISHER-PRICE (1), BABY EINSTEIN (2) E VTECH(3) ")
      if produtos_brinquedo == ("1"):
        print("FISHER-PRICE É UMA MARCA CONHECIDA E IDEAL PARA SEU BEBÊ")
        print("TEMOS TAPETES COM ATIVIDADES, BRINQUEDOS MUSICAIS E MUITOS OUTROS")
        print("NOSSOS MODELOS VARIAM DE R$30 a R$150")
        pergunta_fisherprice = input("Ficou interessado? (S/N)")
        if pergunta_fisherprice == ("S"):
          print("TEMOS O MODELO Fisher-Price Soothing Motions Bassinet(1) custando R$464")
          print ("TEMOS O MODELO Fisher-Price Rainforest Jumperoo(2) CUSTANDO R$438")
          print ("TEMOS O MODELO Fisher-Price Little People Big Animal Zoo(3) CUSTANDO R$190")
          modelo_fisherprice = input("Se interessou por qual dos modelos? ")
          if modelo_fisherprice == ("1"):
            carrinho_total += 464
            aviso = input("Parabéns você adicionou Fisher-Price Soothing Motions Bassinet ao seu carrinho! ")
          elif modelo_fisherprice == ("2"):
            carrinho_total += 438
            aviso = input("Parabéns você adicionou o Fisher-Price Rainforest Jumperoo ao seu carrinho ")
          elif modelo_fisherprice == ("3"):
            carrinho_total += 190
            aviso = input("Parabéns você adicionou Fisher-Price Little People Big Animal Zoo ao seu carrinho")
      elif produtos_brinquedo == ("2"):
        print("BABY EINSTEIN É UMA MARCA IDEAL PARA VOCÊ QUE QUER ESTIMULAR O ESTÍMULO A APRENDIZADO DE SEU BEBÊ")
        print("OFERECEMOS BRINQUEDOS MUSICAIS QUE PROPÕE ATIVIDADES E EDUCATIVOS PARA O BEBÊ")
        print("NOSSOS PREÇOS VARIAM DE R$50 A R$150")
        pergunta_babyeinstein = input("Ficou interessado? (S/N)")
        if pergunta_babyeinstein == ("S"):
          print("TEMOS O MODELO Baby Einstein Take Along Tunes Musical Toy(1) CUSTANDO R$46")
          print ("TEMOS O MODELO Baby Einstein Sea Dreams Soother(2) CUSTANDO R$206")
          print("TEMOS O MODELO Baby Einstein Glow & Discover Light Bar(3) CUSTANDO R$92")
          modelo_babyeinstein = input("Se interessou por qual modelo?")
          if modelo_babyeinstein == ("1"):
            carrinho_total += 46
            aviso = input("PARABÉNS VOCÊ ADICIONOU Baby Einstein Take Along Tunes Musical Toy AO SEU CARRINHO")
          elif modelo_babyeinstein == ("2"):
            carrinho_total += 206
            aviso = input("PARABÉNS VOCÊ ADICIONOU Baby Einstein Sea Dreams Soother AO SEU CARRINHO ")
          elif modelo_babyeinstein == ("3"):
            carrinho_total += 92
            aviso = input("PARABÉNS VOCÊ ADICIONOU Baby Einstein Glow & Discover Light Bar AO SEU CARRINHO")
          
      elif produtos_brinquedo == ("3"):
        print("MARCA ESPECIALIZADA EM BRINQUEDOS ELETRÔNICOS, A VTECH É MAIS VOLTADA PARA BRINQUEDOS QUE ESTIMULEM O DESENVOLVIMENTO DA CRIANÇA")
        print("POR ESSA MARCA, É OFERECIDO BRINQUEDOS MUSICAIS COM ATIVIDADES")
        print("NOSSOS PREÇOS VARIAM DE R$50 A R$200")
        pergunta_vtech = input("Ficou interessado? (S/N)")
        if pergunta_vtech == ("S"):
          print("TEMOS O MODELO VTech Kidizoom Smartwatch DX3(1) CUSTANDO R$309")
          print("TEMOS O MODELO VTech Sit-to-Stand Learning Walker(2) CUSTANDO R$180")
          print("TEMOS O MODELO VTech Go! Go! Smart Ultimate RC Speedway(3) CUSTANDO R$257")
          modelos_vtech = input("SE INTERESSOU POR QUAL DESSES MODELOS?")  
          if modelos_vtech == ("1"):
            carrinho_total += 309
            print("PARABÉNS VOCÊ ADICIONOU VTech Kidizoom Smartwatch DX3 AO SEU CARRINHO ")
          elif modelos_vtech == ("2"):
            carrinho_total += 180
            print("PARABÉNS VOCê ADICIONOU VTech Sit-to-Stand Learning Walker AO SEU CARRINHO")
          elif modelos_vtech == ("3"):
            carrinho_total += 257
            print("PARABÉNS VOCÊ ADICIONOU O VTech Go! Go! Smart Ultimate RC Speedway AO SEU CARRINHO ")
    elif produto == ("3"):
      produtos_roupas = input("POSSUIMOS MARCAS DE ROUPAS DAS SEGUINTES MARCAS: Carter's (1), Lilica Ripilica (2), Puket (3)")
      if produtos_roupas == ("1"):
        print("A CARTER'S É UMA MARCA QUE FOCA TOTALMENTE NO CONFORTO COM UM PREÇO JUSTO!")
        print("NOSSO MODELOS VARIAM ENTRE A R$39,90 A R$89,90")
        escolha_carter = input("FICOU INTERESSADO NESSA MARCA? (S/N )")
        if escolha_carter == ("S"):
          print("TEMOS UM BODY DE MANGA CURTA(1), FEITO 100% DE ALGODÃO E FÁCIL DE VESTIR, CUSTANDO R$39,90")
          print("TEMOS UM MACACÃO DE MALHA(2), FEITO PARA DIAS FRIOS QUE PREZAM PELO SEU CONFORTO, CUSTANDO R$79,90")    
          print("E POSSUIMOS UM CONJUNTO PARA USAR NO BEBÊ NO SEU DIA A DIA(CAMISETA E CALÇA), CUSTANDO R$89,90")
          modelos_carter = input("FICOU INTERESSADO EM QUAL DOS NOSSOS MODELOS?")
          if modelos_carter == ("1"):
            carrinho_total += 39,90
            aviso = input("PARABÉNS VOCÊ ADICIONOU UM BODY DE MANGA CURTA AO SEU CARRINHO!")
          elif modelos_carter == ("2"):
            carrinho_total += 79,90
            aviso = input("PARABÉNS VOCÊ ADICIONOU UM MACACÃO DE MALHA AO SEU CARRINHO!")
          elif modelos_carter == ("3"):
            carrinho_total += 89,90
            aviso = input("PARABÉNS VOCÊ ADICIONOU UM CONJUNTO DE DUAS PEÇAS INFANTIL AO SEU CARRINHO")
      elif produtos_roupas == ("2"):
        print("A LILICA RIPILICA É UMA ÓTIMA PARA VOCÊ QUER QUE SUA MENINA TENHA ESTILO E CONFORTO!")
        print("NOSSOS MODELOS VARIAM ENTRE R$139,90 A R$199,90")
        escolha_lilica = input("FICOU INTERESSADO NESSA MARCA? (S/N)")
        if escolha_lilica == ("S"):
          print("TEMOS VESTIDOS ESTAMPADOS DE DIVERSAS CORES E DESIGN MODERNO, NOSSO PREÇO MÉDIO É R$139,90")
          print("TEMOS CONJUNTO DE CAMISETA E SAIA, PERFEITO PARA OCASIÕES ESPECIAIS, NOSSO PREÇO MÉDIO É ")
      elif produtos_roupas == ("3"):
        print("A PUKET É UMA MARCA BRASILEIRA CONHECIDA POR SUAS MARCAS INFANTIS COM UM DESIGN ALEGRE")
        print("NOSSOS MODELOS VARIAM ENTRE R$19,90 A R$69,90 ")
        escolha_puket = input("FICOU INTERESSADO NESSA MARCA(S/N)?")
        if escolha_puket == ("S"):
          print("TEMOS UM CONJUNTO DE TRÊS MEIAS COM ESTAMPAS DIVERTIDAS(1) CUSTANDO R$19,90")
          print("TEMOS UM BODY COM ESTAMPAS DIVERTIDAS E DIVERTIDOS(2) CUSTANDO R$49,90")
          print("TEMOS UM CONJUNTO DE PIJAMA(3) PERFEITO PARA QUANDA A SUA CRIANÇA ESTIVER PARA DORMIR, CUSTANDO R$69,90")
          modelos_puket = input("FICOU INTERESSADO EM QUAIS DE NOSSOS MODELOS?")
          if modelos_puket == ("1"):
            carrinho_total += 19,90
            aviso = input("PARABÉNS VOCÊ ADICIONOU UM CONJUNTO DE TRÊS MEIAS AO SEU CARRINHO!")
          if modelos_puket == ("2"):
            carrinho_total += 49,90
            aviso = input("PARABÉNS VOCÊ ADICIONOU UM BODY COM ESTAMPAS DIVERTIDAS AO SEU CARRINHO!")  
          if modelos_puket == ("3"):
            carrinho_total += 69,90
            aviso = input("PARABÉNS VOCÊ ADICIONOU UM CONJUNTO DE PIJAMA AO SEU CARRINHO!")

    if produto == ("4"):
      print("O seu total no seu carrinho é", carrinho_total)
      finalizar_compra = input("DESEJA FINALIZAR A COMPRA?(S/N) ")

    



