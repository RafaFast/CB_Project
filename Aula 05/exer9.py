"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando 
o seu preço normal e condição de pagamento: 
À vista dinheiro/cheque  -   10% de desconto
À vista no cartão        -   5% de desconto
Até 2x no cartão         -   Sem reajuste
3x ou mais no cartão     -   20% de juros
"""

valor = int(input("\nValor: R$"))
met_pag = input("\nÀ vista [V] ou parcelado [P]: ").upper()

if met_pag in ["V", "P"]:
    if met_pag == "V":
        mei_pag = input("\nCartão [C], Dinheiro [D] ou Cheque [P]: ").upper()
        if mei_pag in ["C", "D", "P"]:
            if mei_pag == "C":
                print(f"\nPagar: R${int(valor * 0.95)},00 \n")
            else:
                print(f"\nPagar: R${int(valor * 0.9)},00 \n")
        else:
            print("\nDigite um valor válido \n")
    else:
        parc = int(input("\nQuantidade de parcelas: "))
        if parc == 2:
            print(f"\nPagar por mês: R${int(valor / parc)},00 \n")
        elif parc >= 3:
            print(f"\nPagar por mês: R${int((valor * 1.2) / parc)},00 \n")
else:
    print("\nDigite um valor válido\n")

