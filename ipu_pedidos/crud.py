import streamlit as st;
import Pages.Cliente.Create as PageCriarCliente
import Pages.Cliente.Consultar as ConsultarCliente
import Pages.Cliente.Delete as DeletarCliente
import Pages.Cliente.Edit as EditarCliente
import Pages.Produto.Delete as DeletarProduto
import Pages.Produto.Consultar as ConsultarProduto
import Pages.Produto.Create as IncluirProduto
import Pages.Produto.Edit as EditarProduto
import Pages.Funcionario.Consultar as ConsultarFuncionario
import Pages.Funcionario.Edit as EditarFuncionario
import Pages.Funcionario.Delete as DeletarFuncionario
import Pages.Funcionario.Create as IncluirFuncionario
import Pages.Pedido.Consultar as ConsultarPedido
import Pages.Pedido.Create as CriarPedido
import Pages.Pedido.Delete as ExcluirPedido
import Pages.Pedido.Edit as EditarPedido
import Pages.Vendas.Consultar as ConsultarVendas
import Pages.Vendas.Create as IncluirVenda
import Pages.Vendas.Delete as ExcluirVenda
import Pages.Vendas.Edit as EditarVenda
st.sidebar.title('Menu')
page_section = st.sidebar.selectbox('Selecione uma seção:', ['Nenhum','Cliente', 'Produto', 'Funcionario', 'Pedido', 'Vendas'])
if page_section == 'Cliente':
    Page_cliente = st.sidebar.selectbox('Ação desejada', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

    if Page_cliente == 'Incluir':
        PageCriarCliente.Create()

    elif Page_cliente == 'Consultar':
        ConsultarCliente.Consultar()

    elif Page_cliente == 'Excluir':
        DeletarCliente.Delete()

    elif Page_cliente == 'Alterar':
        EditarCliente.Editar()

elif page_section == 'Produto':
    page_produto = st.sidebar.selectbox('Produto', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

    if page_produto == 'Excluir':
        DeletarProduto.Delete()
    
    elif page_produto == 'Consultar':
        ConsultarProduto.Consultar()
    
    elif page_produto == 'Incluir':
        IncluirProduto.Create()
    elif page_produto == 'Alterar':
        EditarProduto.Editar()

elif page_section == 'Funcionario':
    page_funcionario = st.sidebar.selectbox('Funcionario',['Incluir','Alterar','Excluir','Consultar'])
    
    if page_funcionario == 'Consultar':
        ConsultarFuncionario.Consultar()
    
    elif page_funcionario == 'Alterar':
        EditarFuncionario.Editar()

    elif page_funcionario == 'Excluir':
        DeletarFuncionario.Delete()

    elif page_funcionario == 'Incluir':
        IncluirFuncionario.Create()

elif page_section == 'Pedido':
    page_pedido = st.sidebar.selectbox('Pedido',['Incluir','Alterar','Excluir','Consultar'])

    if page_pedido == 'Consultar':
        ConsultarPedido.Consultar()
    
    elif page_pedido == 'Incluir':
        CriarPedido.Create()
    
    elif page_pedido == 'Excluir':
        ExcluirPedido.Delete()
    
    elif page_pedido == 'Alterar':
        EditarPedido.Editar()

elif page_section == 'Vendas':
    page_vendas = st.sidebar.selectbox('Vendas',['Incluir','Alterar','Excluir','Consultar'])
    
    if page_vendas == 'Consultar':
        ConsultarVendas.Consultar()

    elif page_vendas == 'Incluir':
        IncluirVenda.create_vendas()

    elif page_vendas == 'Excluir':
        ExcluirVenda.Delete()
    
    elif page_vendas == 'Alterar':
        EditarVenda.Editar()