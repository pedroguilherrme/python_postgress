# Pedidos
import pedidos;
from datetime import datetime;

todos_pedidos = pedidos.todos_pedidos()

for pedido in todos_pedidos:
    data_formatada = pedido[3].strftime("%d/%m/%Y %H:%M:%S")
    print('Id:', pedido[0],'\nNome do Produto:' , pedido[1], '\nNome do Cliente:',pedido[2], '\nData :', data_formatada )  
    print("| ==========================================")


# Clientes
import cliente;

todos_clientes = cliente.todos_clientes()

for clientes in todos_clientes:
    print('Id:' , clientes[0], '\nNome do Cliente:', clientes [1], '\nCPF:', clientes[2], '\nGênero:', clientes[3])
    print("| ==========================================")

# Funcionarios

import funcionario

todos_funcionarios = funcionario.todos_funcionarios()
for funcionarios in todos_funcionarios:
    print('\nId:',funcionarios[0], '\nNome:' , funcionarios[1],'\nCPF:' , funcionarios[2])
    print("| ==========================================")


# Produtos
import produto

todos_produtos = produto.todos_produtos()
for produtos in todos_produtos:
    print('Id:',produtos[0], '\nNome:', produtos[1], '\nValor:', produtos[2])
    print("| ==========================================")

# Vendas 

import vendas
from datetime import datetime

todas_vendas = vendas.todas_vendas()
for venda in todas_vendas:
    data_formatada = venda[4].strftime("%d/%m/%Y")
    print('Id:',venda[0], '\nNome do vendedor:', venda[1],'\nValor:',venda[3],'\nData da venda:', data_formatada, '\nNome  do produto:', venda[2])
    print("| ==========================================")


