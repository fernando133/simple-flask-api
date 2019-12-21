CREATE TABLE `inscricao` (
  `id` INT NOT NULL,
  `nome_completo` VARCHAR(100) NULL,
  `data_nascimento` DATE NULL,
  `rg` VARCHAR(45) NULL,
  `cpf` VARCHAR(45) NULL,
  `celular` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `rua` VARCHAR(45) NULL,
  `numero` VARCHAR(45) NULL,
  `bairro` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `cep` VARCHAR(45) NULL,
  `complemento` VARCHAR(45) NULL,
  `escolaridade` VARCHAR(45) NULL,
  `formacao` VARCHAR(45) NULL,
  `foco_aulas` VARCHAR(45) NULL,
  `caminho_historico` VARCHAR(45) NULL,
  `caminho_diploma` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

ALTER TABLE `inscricao` 
ADD COLUMN `assinatura` VARCHAR(45) NULL AFTER `date_time`,
ADD COLUMN `lingua_estrangeira` VARCHAR(45) NULL AFTER `assinatura`;
ADD COLUMN `link_aula` VARCHAR(500) NULL AFTER `lingua_estrangeira`;


