CREATE TABLE onibus_disp (
    id_onibus_disp INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(20) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE empresa (
    id_viagem INT AUTO_INCREMENT PRIMARY KEY,
    onibus_disp INT NOT NULL,
    preço_viagens INT NOT NULL,
    horario_chegada INT NOT NULL,
    horario_saida INT NOT NULL,
    CONSTRAINT fk_empresa_onibus_disp
        FOREIGN KEY (onibus_disp)
        REFERENCES onibus_disp(id_onibus_disp)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    id_onibus INT NOT NULL,
    data_compra DATE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    email VARCHAR(150) NOT NULL,
    CONSTRAINT uk_usuario_cpf UNIQUE (cpf),
    CONSTRAINT fk_usuario_onibus 
        FOREIGN KEY (id_onibus) 
        REFERENCES empresa(id_viagem)
);

CREATE TABLE onibus (
    id_onibus INT AUTO_INCREMENT PRIMARY KEY,
    quant_viagem INT NOT NULL,
    quant_manutencoes INT NOT NULL,
    ida_manutencao DATE NOT NULL,
    volta_manutencao DATE NOT NULL,
    id_onibus_disp INT NOT NULL,
    CONSTRAINT fk_onibus_onibus_disp
        FOREIGN KEY (id_onibus_disp)
        REFERENCES onibus_disp(id_onibus_disp)
);

CREATE TABLE motoristas (
    id_motorista INT AUTO_INCREMENT PRIMARY KEY,
    id_onibus INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    CONSTRAINT fk_motoristas_onibus 
        FOREIGN KEY (id_onibus) 
        REFERENCES onibus(id_onibus)
);

CREATE TABLE cobrador (
    id_cobrador INT AUTO_INCREMENT PRIMARY KEY,
    id_onibus INT NOT NULL,
    id_motorista INT NOT NULL, 
    nome VARCHAR(100) NOT NULL,
    CONSTRAINT fk_cobrador_onibus 
        FOREIGN KEY (id_onibus) 
        REFERENCES onibus(id_onibus),
    CONSTRAINT fk_cobrador_motorista 
        FOREIGN KEY (id_motorista) 
        REFERENCES motoristas(id_motorista)
);

CREATE TABLE rota(
    id_rotas INT AUTO_INCREMENT PRIMARY KEY,
    id_cidades INT NOT NULL,
    paradas VARCHAR(50) NOT NULL,
    quant_paradas INT NOT NULL,
    data_saida DATE NOT NULL,
    data_chegada DATE NOT NULL,
    CONSTRAINT fk_rota_empresa 
        FOREIGN KEY (id_rotas) 
        REFERENCES empresa(id_viagem),
    CONSTRAINT fk_rota_cidades 
        FOREIGN KEY (id_cidades) 
        REFERENCES cidades(id_cidades)
);

CREATE TABLE cidades(
    id_cidades INT AUTO_INCREMENT PRIMARY KEY,
    cidades_visitadas VARCHAR(100) NOT NULL,
    tempo_visita VARCHAR(50) NOT NULL
);

CREATE TABLE administrador(
    id_administrador INT AUTO_INCREMENT PRIMARY KEY,
    id_onibus_disp INT NOT NULL,
    tipo_notebook VARCHAR(50) NOT NULL,
    CONSTRAINT fk_administrador_onibus_disp 
        FOREIGN KEY (id_onibus_disp) 
        REFERENCES onibus_disp(id_onibus_disp)
