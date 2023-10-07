CREATE DATABASE alunos;

USE alunos;

CREATE TABLE `alunos`.`resumo_aluno` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `idade` INT NOT NULL,
  `nota_1_semestre` FLOAT NOT NULL,
  `nota_2_semestre` FLOAT NOT NULL,
  `nome_professor` VARCHAR(150) NOT NULL,
  `numero_da_sala` INT NOT NULL,
  PRIMARY KEY (`id`));

INSERT INTO resumo_aluno (nome,idade,nota_1_semestre,nota_2_semestre,nome_professor,numero_da_sala) VALUES ('HETTORE',32,8.5,9.5,'JOSÉ',12);

DROP TABLE RESUMOALUNO;
 SELECT * FROM resumo_aluno;