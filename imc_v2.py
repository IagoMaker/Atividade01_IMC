#Programa que calcula o inidice de massa corporal - Versão 2
#Programa conforme sugerido na aula de programacao, com melhorias adicionais

while True:
   
    condicao = int(input("\n### MENU DE OPCOES ###\n1 - Para calcular IMC\n2 - Para sair\nDIGITE A SUA OPCAO: "))
    
    if condicao == 1:
       
        fAltura = float(input("\nDigite a sua altura: "))
        fPeso = float(input("Digite o seu peso: "))
       
        fImc = fPeso/(fAltura**2)
        print("IMC: %.2f" % fImc)
        print("DE ACORDO COM O ICM: ")
        
        if fImc < 17:
            print("=> Muito abaixo do peso")
        elif fImc >= 17.0 and fImc < 18.5:
            print("=> Abaixo do peso normal")
        elif fImc >= 18.5 and fImc < 25.0:
            print("=> Peso dentro do normal")
        elif fImc >= 25.0 and fImc <= 30.0:
            print("=> Acima do peso normal")
        elif fImc > 30.0:
            print("=> Muito acima do peso")
    
    if condicao == 2:
        print("\nSaindo do programa...\n")
        break