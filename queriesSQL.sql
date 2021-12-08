/* PARTE 1 */

CREATE DATABASE EuVendedor;
USE EuVendedor;
CREATE TABLE ProdutoVendido (
   	ID_NF INT NOT NULL,
	ID_ITEM INT NOT NULL,
	COD_PROD INT NOT NULL,
	VALOR_UNIT DOUBLE NOT NULL,
	QUANTIDADE INT NOT NULL,
	DESCONTO DECIMAL,
	CONSTRAINT PK_Filme PRIMARY KEY (ID_NF, ID_ITEM)
);

INSERT INTO ProdutoVendido VALUES 
(1, 1, 1, 25, 10, 5), 
(2, 2, 4, 10, 5, NULL),
(2, 3, 5, 30, 7, NULL),
(3, 1, 1, 25, 5, NULL),
(3, 2, 4, 10, 4, NULL),
(1, 2, 2, 13.5, 3, NULL);


SELECT * FROM ProdutoVendido; /* conferencia */

SELECT ID_NF, ID_ITEM, COD_PROD, VALOR_UNIT FROM ProdutoVendido WHERE DESCONTO IS NOT NULL;

UPDATE ProdutoVendido SET DESCONTO = 0 WHERE DESCONTO IS NULL;

SELECT ID_NF, SUM(QUANTIDADE * VALOR_UNIT) AS VALOR_TOTAL FROM ProdutoVendido GROUP BY ID_NF ORDER BY VALOR_TOTAL DESC;

SELECT 
    COD_PROD, SUM(QUANTIDADE) AS QUANTIDADE,
    (QUANTIDADE * VALOR_UNIT) AS VALOR_TOTAL,
    (VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100))) AS VALOR_VENDIDO 
FROM
    ProdutoVendido
GROUP BY COD_PROD
ORDER BY QUANTIDADE DESC
LIMIT 1;

SELECT COD_PROD, AVG(DESCONTO) AS MEDIA, 
        MIN(DESCONTO) AS MENOR, 
        MAX(DESCONTO) AS MAIOR, 
        COUNT(*) AS QTD_ITENS
FROM ProdutoVendido GROUP BY COD_PROD ORDER BY QUANTIDADE LIMIT 6;


/* PARTE 2 */
USE estacionamento;
SELECT v.placa, v.cor, m.Desc_2
FROM Veiculo v INNER JOIN modelo m on v.Modelo_codMod = m.codMod 
where v.cor = 'azul' or v.cor = 'branca' or  v.cor = 'prata';

CREATE TABLE  Caixa  (
   id  int NOT NULL,
   saldo_do_dia decimal null,
   data1 date NULL,
  PRIMARY KEY ( id )
);

INSERT INTO  Caixa  (id, data1 ) VALUES (1, '09/11/2013');
INSERT INTO  Caixa  (id, data1 ) VALUES (2, '10/11/2013');

DECLARE @total DECIMAL = (SELECT COUNT(*) FROM estaciona e INNER JOIN Caixa c on e.dtSaida = c.data1 WHERE e.dtSaida = c.data1)
BEGIN TRANSACTION;
	UPDATE Caixa SET saldo_do_dia = @total * 10
COMMIT;
SELECT * FROM caixa

BEGIN TRANSACTION;
SELECT p.ender, e.dtENtrada, e.dtSaida
FROM Patio p INNER JOIN Estaciona e on p.num = e.Patio_num 
where e.Veiculo_placa = 'JEG-1010';
COMMIT;

/* Exiba a quantidade de vezes os veiculos de cor verde estacionaram.*/
select COUNT(*) as 'Total_Verdes' FROM estaciona e INNER JOIN veiculo v on v.placa = e.Veiculo_placa WHERE v.cor = 'Verde';

/* Liste todos os clientes que possuem carro de modelo 1  */
SELECT c.cpf, c.nome, c.dtNasc, m.codMod FROM cliente c INNER JOIN veiculo v on c.cpf = v.Cliente_cpf 
INNER JOIN modelo m on v.Modelo_codMod = m.codMod WHERE m.codMod = 1;

/* Liste as placas, os horarios de entrada e saida dos veiculos de cor verde */
SELECT v.placa, e.hsEntrada, hsSaida FROM veiculo v INNER JOIN estaciona e on v.placa = e.Veiculo_placa 
WHERE v.cor = 'verde';

/* Liste todos os estacionamentos do veiculo de placa JJJ-2020  */
SELECT e.cod, e.Patio_num, e.Veiculo_placa, e.dtEntrada, e.dtSaida, e.hsEntrada, e.hsSaida
FROM estaciona e INNER JOIN veiculo v on v.placa = e.Veiculo_placa 
WHERE v.placa = 'JJJ-2020';

/* Exiba o CPF do cliente que possui o veiculo cujo codigo do estacionamento = 3  */
SELECT c.cpf FROM cliente c INNER JOIN veiculo v on c.cpf = v.Cliente_cpf 
INNER JOIN estaciona e on v.placa = e.Veiculo_placa WHERE e.cod = 3;

/* Exiba a descricao do modelo do veiculo cujo codigo do estacionamento = 2  */
SELECT m.Desc_2, v.placa, e.cod FROM modelo m INNER JOIN veiculo v on m.codMod = v.Modelo_codMod 
INNER JOIN estaciona e on v.placa = e.Veiculo_placa WHERE e.cod = 2;

/* Exiba a placa, o nome dos donos e a descricao dos os modelos de todos os veiculos  */
SELECT c.nome, v.placa, m.Desc_2 FROM modelo m INNER JOIN veiculo v on m.codMod = v.Modelo_codMod
INNER JOIN cliente c on c.cpf = v.Cliente_cpf;


/* PARTE 3 */
/* Consulta Aninhada - Verificado o numero de locacoes cadastradas sob cada funcionario do sistema. */
select count(aluguel_id), funcionario_id from aluguel where funcionario_id in
(select funcionario_id from funcionario) group by funcionario_id;


/* Inner Join - verificado o número de locacoes existentes para cada filme no inventario, e por fim, o número de locacoes para cada categoria de filme listada no inventario anterior.*/
SELECT count(a.aluguel_id) as total_alugueis, fc.categoria_id as CATEGORIA from aluguel a
    INNER JOIN inventario i ON i.inventario_id = a.inventario_id
    INNER JOIN filme_categoria fc ON fc.filme_id = i.filme_id
    group by CATEGORIA order by total_alugueis DESC;


/*Left Join */
/* Acessar todos os dados de enderecos do sistema, e posteriormente selecionar apenas aqueles que pertencem aos clientes.*/
SELECT count(c.endereco_id) as clientes, ci.cidade_id as cidade from cliente c
    INNER JOIN endereco e ON e.endereco_id = c.endereco_id
    LEFT JOIN cidade ci ON ci.cidade_id = e.cidade_id
    group by cidade order by clientes DESC;

/* Analisar os inventarios presentes nos alugueis, e a partir destes encontrar as categorias, fazendo por fim a filtragem para os dados presentes apenas na segunda loja.*/
SELECT count(a.aluguel_id) as total_alugueis, fc.categoria_id as CATEGORIA, c.loja_id as LOJA from aluguel a
    INNER JOIN inventario i ON i.inventario_id = a.inventario_id
    INNER JOIN filme_categoria fc ON fc.filme_id = i.filme_id
    LEFT JOIN cliente c ON c.cliente_id = a.cliente_id and c.loja_id = 2
    group by CATEGORIA order by total_alugueis DESC;


/* Outer Join -  Buscados todos os valores de alugueis de filmes de todos os exemplares no inventario e todos os valores de pagamento (dados existentes tanto na tabela aluguel quanto na tabela pagamento).*/
SELECT p.valor, a.inventario_id from pagamento p 
    FULL OUTER JOIN aluguel a ON a.aluguel_id = p.aluguel_id 
    order by p.valor;
