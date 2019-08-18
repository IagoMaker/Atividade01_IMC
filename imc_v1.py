#Programa que calcula o inidice de massa corporal - Versão 1

fAltura = 1.80
fPeso = 72.0

fImc = fPeso/(fAltura**2)
print("IMC: ", fImc)
print("DE ACORDO COM O ICM: ")
        
print("=> Muito abaixo do peso: ", fImc < 17)
print("=> Abaixo do peso normal: ", fImc >= 17.0 and fImc < 18.5)
print("=> Peso dentro do normal: ", fImc >= 18.5 and fImc < 25.0)
print("=> Acima do peso normal: ", fImc >= 25.0 and fImc <= 30.0)
print("=> Muito acima do peso: ", fImc > 30.0)
    