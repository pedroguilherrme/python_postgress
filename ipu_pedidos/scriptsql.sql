create table pedidos(
	idpedido serial not null,
	nome_produto varchar(50) not null,
	nome_cliente varchar(50) not null,
	data_pedido date not null,

	constraint pk_pdd_idpedido primary key (idpedido)
	
);

select * from pedidos;




create table produto(
	idproduto serial not null,
	nome varchar(50) not null,
	valor float not null,

	constraint pk_pdt_idproduto primary key (idproduto)
);

select * from produto
insert into produto (nome,valor) values ('Sabonete',2);
insert into produto (nome,valor) values ('Pasta de dente',4);-
insert into produto (nome,valor) values ('Escova de dente',10);
insert into produto (nome,valor) values ('Pente',3);
insert into produto (nome,valor) values ('Desodorante',8);
insert into produto (nome,valor) values ('Shampoo',12);
insert into produto (nome,valor) values ('Perfume',40);
insert into produto (nome,valor) values ('Condicionador',15);
insert into produto (nome,valor) values ('Papel Higiênico',8);
insert into produto (nome,valor) values ('Sabão em pó',5);

create table cliente ( 
	idcliente serial not null,
	nome varchar(50) not null,
	cpf varchar(11) not null,
	genero varchar(1),

	constraint pk_cln_idcliente primary key(idcliente)
);

select * from cliente;
insert into cliente (nome,cpf,genero) values ('Pedro', '12345678910', 'M');--
insert into cliente (nome,cpf,genero) values ('Caio', '12345678911', 'M');
insert into cliente (nome,cpf,genero) values ('Maria', '12345678922', 'F');
insert into cliente (nome,cpf,genero) values ('Cristiano', '12345678933', 'M');
insert into cliente (nome,cpf,genero) values ('Andreza', '12345678944', 'F');
insert into cliente (nome,cpf,genero) values ('João', '12345678955', 'M');

create table funcionario (
	idfuncionario serial not null,
	nome varchar(50) not null,
	cpf char(11) not null,

	constraint pk_fcn_idfuncionario primary key (idfuncionario)
	
);

insert into funcionario (nome,cpf) values ('Joana','11111111111');
insert into funcionario (nome,cpf) values ('Ana','22222222222');

create table vendas (
	idvenda serial not null,
	idfuncionario integer not null,
	valor float not null,
	data_venda date not null,

	constraint pk_vnd_idvenda primary key (idvenda),
	constraint fk_vnd_idfuncionario foreign key (idfuncionario) references funcionario(idfuncionario)
);
alter table vendas alter column data_venda drop not null;
alter table vendas alter column data_venda set default current_date;
alter table vendas add column idproduto integer, add constraint fk_vnd_idproduto foreign key (idproduto) references produto(idproduto);
select * from vendas;
insert into vendas (idfuncionario,valor,data_venda) values (1,111, '2002-10-10');
insert into vendas (idfuncionario,valor) values (2,200);
insert into vendas (idfuncionario,valor,data_venda) values (1,400, '2012-05-10');
insert into vendas (idfuncionario,valor,data_venda) values (2,500, '2018-01-12');
insert into vendas (idfuncionario,valor,data_venda) values (1,300, '2000-12-12');
insert into vendas (idfuncionario,valor) values (2,100);
select * from produto;

update vendas set idproduto = 4 where idvenda = 2;
update vendas set idproduto = 1 where idvenda = 3;
update vendas set idproduto = 2 where idvenda = 4;
update vendas set idproduto = 3 where idvenda = 5;
update vendas set idproduto = 5 where idvenda = 6;
update vendas set idproduto = 6 where idvenda = 7;


select * from cliente;
select * from produto;
select * from funcionario;
select * from pedidos;



---------------------------------------------------------



