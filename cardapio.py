lista = [
    "\nHot-dog: [100]",
    "\nx-bauru: [101]",
    "\nx-salada: [102]",
    "\nx-bacon: [103]",
    "\nx-burguer: [104]",
    "\nsuco de laranja: [105]",
    "\nrefrigerante: [106]",
]

print("\nCardápio:")
for item in lista:
    print(item)

total = 0

while True:
    codigo_pedido = int(input("\nDigite o código do pedido (ou 0 para finalizar): "))
    if codigo_pedido == 0:
        break
    
    quantidade = int(input("Digite a quantidade: "))

    preco = 0
    if codigo_pedido == 100:
        preco = 1.20 * quantidade
    elif codigo_pedido == 101:
        preco = 1.30 * quantidade
    elif codigo_pedido == 102:
        preco = 1.50 * quantidade
    elif codigo_pedido == 103:
        preco = 1.20 * quantidade
    elif codigo_pedido == 104:
        preco = 17.00 * quantidade
    elif codigo_pedido == 105:
        preco = 9.50 * quantidade
    elif codigo_pedido == 106:
        preco = 6.00 * quantidade
    else:
        print("Código inválido!")
        continue  # volta pro início do loop sem somar nada
    
    total += preco
    print(f"Item adicionado! Subtotal até agora: R${total:.2f}")

print(f"\nTotal do pedido: R${total:.2f}")
