-- Inserir cursos
INSERT INTO curso (sigla, nome, carga_horaria_complementar) VALUES
('ENG001', 'Engenharia Eletrônica', 60),
('ENG002', 'Engenharia de Computação', 70),
('ENG003', 'Engenharia Mecatrônica', 65),
('ENG004', 'Engenharia Civil', 80),
('ENG005', 'Engenharia Ambiental', 55),
('ENG006', 'Engenharia de Produção', 50),
('ENG007', 'Engenharia Química', 75),
('ENG008', 'Engenharia de Telecomunicações', 60),
('ENG009', 'Engenharia de Materiais', 65),
('ENG010', 'Engenharia Naval', 70),
('CIN001', 'Ciência da Computação', 40),
('CIN002', 'Sistemas de Informação', 45),
('CIN003', 'Matemática Aplicada', 50),
('CIN004', 'Física Computacional', 55),
('CIN005', 'Estatística', 40),
('CIN006', 'Engenharia de Software', 65),
('CIN007', 'Inteligência Artificial', 50),
('CIN008', 'Redes de Computadores', 60),
('CIN009', 'Segurança da Informação', 55),
('CIN010', 'Banco de Dados', 50),
('ADM001', 'Administração de Empresas', 40),
('ADM002', 'Economia', 45),
('ADM003', 'Gestão de Recursos Humanos', 50),
('ADM004', 'Marketing', 45),
('ADM005', 'Contabilidade', 55),
('ADM006', 'Logística', 50),
('ADM007', 'Finanças', 60),
('ADM008', 'Empreendedorismo', 45),
('ADM009', 'Gestão de Projetos', 55),
('ADM010', 'Gestão da Qualidade', 50);


-- Inserir usuários
INSERT INTO usuario (curso_id, email, senha, nome, administrador) VALUES
-- Administradores
('ENG001', 'maria.silva@professor.com', 'senha001', 'Maria Silva', TRUE),
('ENG002', 'joao.santos@professor.com', 'senha002', 'João Santos', TRUE),
('ENG003', 'lucas.oliveira@professor.com', 'senha003', 'Lucas Oliveira', TRUE),
('ENG004', 'ana.martins@professor.com', 'senha004', 'Ana Martins', TRUE),
('ENG005', 'pedro.gomes@professor.com', 'senha005', 'Pedro Gomes', TRUE),
('CIN001', 'carla.pereira@professor.com', 'senha006', 'Carla Pereira', TRUE),
('CIN002', 'andreia.lima@professor.com', 'senha007', 'Andréia Lima', TRUE),
('CIN003', 'bruno.silva@professor.com', 'senha008', 'Bruno Silva', TRUE),
('CIN004', 'gabriela.costa@professor.com', 'senha009', 'Gabriela Costa', TRUE),
('CIN005', 'roberto.fernandes@professor.com', 'senha010', 'Roberto Fernandes', TRUE),

-- Não-administradores
('ENG001', 'victor.souza@aluno.com', 'senha011', 'Victor Souza', FALSE),
('ENG001', 'larissa.oliveira@aluno.com', 'senha012', 'Larissa Oliveira', FALSE),
('ENG001', 'danilo.pereira@aluno.com', 'senha013', 'Danilo Pereira', FALSE),
('ENG001', 'beatriz.goncalves@aluno.com', 'senha014', 'Beatriz Gonçalves', FALSE),
('ENG001', 'carlos.martins@aluno.com', 'senha015', 'Carlos Martins', FALSE),
('ENG001', 'sabrina.farias@aluno.com', 'senha016', 'Sabrina Farias', FALSE),
('ENG001', 'jose.augusto@aluno.com', 'senha017', 'José Augusto', FALSE),
('ENG001', 'amanda.santos@aluno.com', 'senha018', 'Amanda Santos', FALSE),
('ENG001', 'gabriel.melo@aluno.com', 'senha019', 'Gabriel Melo', FALSE),
('ENG001', 'juliana.reis@aluno.com', 'senha020', 'Juliana Reis', FALSE),
('ENG002', 'renato.souza@aluno.com', 'senha021', 'Renato Souza', FALSE),
('ENG002', 'julio.borges@aluno.com', 'senha022', 'Julio Borges', FALSE),
('ENG002', 'maria.fernanda@aluno.com', 'senha023', 'Maria Fernanda', FALSE),
('ENG002', 'pedro.lopes@aluno.com', 'senha024', 'Pedro Lopes', FALSE),
('ENG002', 'carla.costa@aluno.com', 'senha025', 'Carla Costa', FALSE),
('ENG002', 'thais.souza@aluno.com', 'senha026', 'Thais Souza', FALSE),
('ENG002', 'renan.pereira@aluno.com', 'senha027', 'Renan Pereira', FALSE),
('ENG002', 'mariana.goncalves@aluno.com', 'senha028', 'Mariana Gonçalves', FALSE),
('ENG002', 'jorge.santos@aluno.com', 'senha029', 'Jorge Santos', FALSE),
('ENG002', 'nathalia.martins@aluno.com', 'senha030', 'Nathalia Martins', FALSE),
('ENG003', 'gabriel.lima@aluno.com', 'senha031', 'Gabriel Lima', FALSE),
('ENG003', 'leticia.alves@aluno.com', 'senha032', 'Leticia Alves', FALSE),
('ENG003', 'roberto.melo@aluno.com', 'senha033', 'Roberto Melo', FALSE),
('ENG003', 'isabela.reis@aluno.com', 'senha034', 'Isabela Reis', FALSE),
('ENG003', 'lucas.souza@aluno.com', 'senha035', 'Lucas Souza', FALSE),
('ENG003', 'claudia.oliveira@aluno.com', 'senha036', 'Claudia Oliveira', FALSE),
('ENG003', 'marcos.pereira@aluno.com', 'senha037', 'Marcos Pereira', FALSE),
('ENG003', 'jessica.costa@aluno.com', 'senha038', 'Jessica Costa', FALSE),
('ENG003', 'antonio.borges@aluno.com', 'senha039', 'Antonio Borges', FALSE),
('ENG003', 'michele.silva@aluno.com', 'senha040', 'Michele Silva', FALSE),
('ENG004', 'andre.santos@aluno.com', 'senha041', 'André Santos', FALSE),
('ENG004', 'marta.gomes@aluno.com', 'senha042', 'Marta Gomes', FALSE),
('ENG004', 'thiago.silva@aluno.com', 'senha043', 'Thiago Silva', FALSE),
('ENG004', 'renata.fernandes@aluno.com', 'senha044', 'Renata Fernandes', FALSE),
('ENG004', 'marcio.pereira@aluno.com', 'senha045', 'Marcio Pereira', FALSE),
('ENG004', 'monique.melo@aluno.com', 'senha046', 'Monique Melo', FALSE),
('ENG004', 'ricardo.costa@aluno.com', 'senha047', 'Ricardo Costa', FALSE),
('ENG004', 'andreia.oliveira@aluno.com', 'senha048', 'Andreia Oliveira', FALSE),
('ENG004', 'mario.reis@aluno.com', 'senha049', 'Mario Reis', FALSE),
('ENG004', 'sara.martins@aluno.com', 'senha050', 'Sara Martins', FALSE),
('ENG005', 'marina.souza@aluno.com', 'senha051', 'Marina Souza', FALSE),
('ENG005', 'giovanni.borges@aluno.com', 'senha052', 'Giovanni Borges', FALSE),
('ENG005', 'julia.lima@aluno.com', 'senha053', 'Julia Lima', FALSE),
('ENG005', 'fabio.reis@aluno.com', 'senha054', 'Fabio Reis', FALSE),
('ENG005', 'larissa.pereira@aluno.com', 'senha055', 'Larissa Pereira', FALSE),
('ENG005', 'guilherme.gomes@aluno.com', 'senha056', 'Guilherme Gomes', FALSE),
('ENG005', 'renata.santos@aluno.com', 'senha057', 'Renata Santos', FALSE),
('ENG005', 'bruno.reis@aluno.com', 'senha058', 'Bruno Reis', FALSE),
('ENG005', 'victoria.martins@aluno.com', 'senha059', 'Victoria Martins', FALSE),
('ENG005', 'matheus.pereira@aluno.com', 'senha060', 'Matheus Pereira', FALSE),
('CIN001', 'roberto.silva@aluno.com', 'senha061', 'Roberto Silva', FALSE),
('CIN001', 'amanda.souza@aluno.com', 'senha062', 'Amanda Souza', FALSE),
('CIN001', 'luan.pereira@aluno.com', 'senha063', 'Luan Pereira', FALSE),
('CIN001', 'patricia.oliveira@aluno.com', 'senha064', 'Patricia Oliveira', FALSE),
('CIN001', 'marcio.santos@aluno.com', 'senha065', 'Marcio Santos', FALSE),
('CIN001', 'laura.reis@aluno.com', 'senha066', 'Laura Reis', FALSE),
('CIN001', 'jose.martins@aluno.com', 'senha067', 'José Martins', FALSE),
('CIN001', 'bianca.costa@aluno.com', 'senha068', 'Bianca Costa', FALSE),
('CIN001', 'pedro.souza@aluno.com', 'senha069', 'Pedro Souza', FALSE),
('CIN001', 'vanessa.lima@aluno.com', 'senha070', 'Vanessa Lima', FALSE),
('CIN002', 'mario.silva@aluno.com', 'senha071', 'Mario Silva', FALSE),
('CIN002', 'nathalia.souza@aluno.com', 'senha072', 'Nathalia Souza', FALSE),
('CIN002', 'guilherme.costa@aluno.com', 'senha073', 'Guilherme Costa', FALSE),
('CIN002', 'renan.santos@aluno.com', 'senha074', 'Renan Santos', FALSE),
('CIN002', 'clara.melo@aluno.com', 'senha075', 'Clara Melo', FALSE),
('CIN002', 'daniela.oliveira@aluno.com', 'senha076', 'Daniela Oliveira', FALSE),
('CIN002', 'luiz.martins@aluno.com', 'senha077', 'Luiz Martins', FALSE),
('CIN002', 'joana.reis@aluno.com', 'senha078', 'Joana Reis', FALSE),
('CIN002', 'emilia.lima@aluno.com', 'senha079', 'Emilia Lima', FALSE),
('CIN002', 'felipe.pereira@aluno.com', 'senha080', 'Felipe Pereira', FALSE),
('CIN003', 'rafael.souza@aluno.com', 'senha081', 'Rafael Souza', FALSE),
('CIN003', 'viviane.santos@aluno.com', 'senha082', 'Viviane Santos', FALSE),
('CIN003', 'gabriel.silva@aluno.com', 'senha083', 'Gabriel Silva', FALSE),
('CIN003', 'julia.costa@aluno.com', 'senha084', 'Julia Costa', FALSE),
('CIN003', 'andre.lima@aluno.com', 'senha085', 'André Lima', FALSE),
('CIN003', 'carol.reis@aluno.com', 'senha086', 'Carol Reis', FALSE),
('CIN003', 'marcelo.santos@aluno.com', 'senha087', 'Marcelo Santos', FALSE),
('CIN003', 'felipe.oliveira@aluno.com', 'senha088', 'Felipe Oliveira', FALSE),
('CIN003', 'beatriz.souza@aluno.com', 'senha089', 'Beatriz Souza', FALSE),
('CIN003', 'lucas.pereira@aluno.com', 'senha090', 'Lucas Pereira', FALSE),
('CIN004', 'elena.martins@aluno.com', 'senha091', 'Elena Martins', FALSE),
('CIN004', 'gustavo.costa@aluno.com', 'senha092', 'Gustavo Costa', FALSE),
('CIN004', 'amanda.alves@aluno.com', 'senha093', 'Amanda Alves', FALSE),
('CIN004', 'sergio.pereira@aluno.com', 'senha094', 'Sergio Pereira', FALSE),
('CIN004', 'marta.reis@aluno.com', 'senha095', 'Marta Reis', FALSE),
('CIN004', 'thiago.santos@aluno.com', 'senha096', 'Thiago Santos', FALSE),
('CIN004', 'luan.martins@aluno.com', 'senha097', 'Luan Martins', FALSE),
('CIN004', 'veronica.lima@aluno.com', 'senha098', 'Veronica Lima', FALSE),
('CIN004', 'rogerio.souza@aluno.com', 'senha099', 'Rogerio Souza', FALSE),
('CIN004', 'mariana.oliveira@aluno.com', 'senha100', 'Mariana Oliveira', FALSE);

-- Inserir categorias
INSERT INTO categoria (curso_id, horar_multiplicador, nome, horas_maximas, descricao) VALUES
('ENG001', 1.5, 'Curso Extracurricular', 40, 'Cursos de aprimoramento em áreas complementares à engenharia.'),
('ENG002', 1.2, 'Palestra Técnica', 20, 'Palestras sobre temas técnicos relevantes para engenharia.'),
('ENG003', 2.0, 'Seminário Técnico', 30, 'Seminários sobre inovações e tópicos avançados na engenharia.'),
('ENG004', 2.5, 'Congresso de Engenharia', 50, 'Congresso sobre tendências e pesquisas em engenharia.'),
('ENG005', 1.8, 'Workshop Prático', 25, 'Workshops práticos em áreas específicas de engenharia.'),
('ENG006', 1.5, 'Publicação Científica', 30, 'Publicação de artigos em revistas científicas especializadas.'),
('ENG007', 2.0, 'Curso de Certificação', 40, 'Cursos para certificação em novas tecnologias e práticas profissionais.'),
('ENG008', 1.7, 'Jornada de Engenharia', 35, 'Eventos técnicos com diversos temas de engenharia.'),
('ENG009', 2.2, 'Curso de Atualização Profissional', 45, 'Cursos focados na atualização de conhecimentos profissionais.'),
('ENG010', 1.8, 'Mesa Redonda Técnica', 20, 'Discussões sobre temas relevantes para o campo da engenharia.'),
('CIN001', 1.5, 'Curso de Programação', 35, 'Cursos sobre diferentes linguagens e técnicas de programação.'),
('CIN002', 1.7, 'Palestra sobre Tecnologia', 25, 'Palestras sobre novas tecnologias e tendências em computação.'),
('CIN003', 2.0, 'Seminário de Computação', 30, 'Seminários sobre tópicos avançados em ciência da computação.'),
('CIN004', 2.2, 'Congresso de TI', 50, 'Congresso sobre tecnologias emergentes e práticas em TI.'),
('CIN005', 1.6, 'Workshop de Desenvolvimento', 30, 'Workshops focados no desenvolvimento de software e ferramentas.'),
('CIN006', 1.5, 'Publicação de Pesquisa', 30, 'Publicação de pesquisas acadêmicas em tecnologia da informação.'),
('CIN007', 1.8, 'Curso de Engenharia de Dados', 40, 'Curso sobre engenharia e gestão de dados.'),
('CIN008', 1.9, 'Jornada de Tecnologia', 35, 'Eventos sobre novas tendências e desafios tecnológicos.'),
('CIN009', 2.0, 'Certificação em Segurança', 45, 'Certificação em práticas e técnicas de segurança da informação.'),
('CIN010', 1.7, 'Mesa Redonda de TI', 25, 'Discussões sobre temas atuais e desafios em tecnologia da informação.'),
('ADM001', 1.6, 'Curso de Administração Geral', 30, 'Cursos sobre fundamentos e práticas de administração de empresas.'),
('ADM002', 1.8, 'Palestra sobre Gestão', 20, 'Palestras sobre técnicas de gestão e administração.'),
('ADM003', 2.0, 'Seminário Administrativo', 25, 'Seminários sobre administração e tópicos relacionados.'),
('ADM004', 2.2, 'Congresso de Administração', 50, 'Congresso sobre estratégias e práticas em administração empresarial.'),
('ADM005', 1.7, 'Workshop de Estratégia', 35, 'Workshop sobre planejamento e estratégia empresarial.'),
('ADM006', 1.5, 'Publicação de Artigo em Gestão', 30, 'Publicação de artigos em revistas de gestão e administração.'),
('ADM007', 1.9, 'Curso de Gestão de Projetos', 40, 'Curso sobre técnicas e ferramentas de gestão de projetos.'),
('ADM008', 1.6, 'Jornada de Administração', 30, 'Eventos focados em administração e práticas empresariais.'),
('ADM009', 2.0, 'Certificação em Liderança', 45, 'Certificação em técnicas de liderança e desenvolvimento de equipes.'),
('ADM010', 1.8, 'Mesa Redonda Administrativa', 25, 'Discussões sobre gestão e administração de negócios.'),
('CIN007', 1.7, 'Curso de Desenvolvimento Web', 35, 'Curso sobre técnicas e ferramentas para desenvolvimento web.'),
('CIN010', 1.6, 'Palestra sobre IA', 20, 'Palestra sobre inteligência artificial e suas aplicações.'),
('CIN009', 2.0, 'Seminário de Análise de Dados', 30, 'Seminário sobre técnicas de análise e visualização de dados.'),
('CIN008', 2.1, 'Congresso de Redes de Computadores', 50, 'Congresso sobre redes e arquitetura de computadores.'),
('CIN008', 1.8, 'Workshop de Ciência de Dados', 30, 'Workshop sobre análise e ciência de dados.'),
('CIN009', 1.5, 'Publicação de Artigo em TI', 30, 'Publicação de artigos em revistas de tecnologia e computação.'),
('CIN010', 1.9, 'Curso de Sistemas Distribuídos', 40, 'Curso sobre sistemas distribuídos e suas aplicações.'),
('CIN010', 1.7, 'Jornada de Desenvolvimento', 35, 'Eventos sobre desenvolvimento de software e melhores práticas.'),
('CIN006', 2.0, 'Certificação em Métodos Ágeis', 45, 'Certificação em metodologias ágeis de desenvolvimento de software.'),
('CIN007', 1.8, 'Mesa Redonda Tecnológica', 25, 'Discussões sobre inovações e desafios em tecnologia.')

-- Inserir atividades
INSERT INTO atividade (usuario_id, categoria_id, titulo, data, status, carga_horaria, comentario) VALUES
(187,'108b12b3-3130-4833-8d42-245a1d9e239d', 'Palestra sobre Circuitos Elétricos', '2024-08-01 14:00:00+00', 'Concluída', 12.0, 'Certificado de conclusão enviado.'),
(188,'108b12b3-3130-4833-8d42-245a1d9e239d', 'Workshop de Algoritmos', '2024-08-02 10:00:00+00', 'Concluída', 15.0, 'Certificado em revisão.'),
(189,'108b12b3-3130-4833-8d42-245a1d9e239d', 'Seminário sobre Robótica', '2024-08-03 09:00:00+00', 'Não Iniciado', 20.0, 'Aguardando certificado.'),
(190,'108b12b3-3130-4833-8d42-245a1d9e239d','Congresso de Materiais de Construção', '2024-08-04 16:00:00+00', 'Concluída', 18.0, 'Certificado de conclusão recebido.'),
(190,'592ae434-f44b-49ed-a9c8-96012fa6b6b4','Curso de Gestão Ambiental', '2024-08-05 13:00:00+00', 'Concluída', 14.0, 'Certificado enviado para análise.'),
(200,'592ae434-f44b-49ed-a9c8-96012fa6b6b4','Curso de Gestão da Produção', '2024-08-06 14:00:00+00', 'Concluída', 12.0, 'Certificado recebido e validado.'),
(200,'592ae434-f44b-49ed-a9c8-96012fa6b6b4', 'Palestra sobre Processos Químicos', '2024-08-07 15:00:00+00', 'Em Andamento', 22.0, 'Certificado está em processo de revisão.'),
(200,'592ae434-f44b-49ed-a9c8-96012fa6b6b4', 'Workshop de Telecomunicações', '2024-08-08 16:00:00+00', 'Não Iniciado', 16.0, 'Certificado pendente.'),
(208,'592ae434-f44b-49ed-a9c8-96012fa6b6b4', 'Curso de Ciência dos Materiais', '2024-08-09 10:00:00+00', 'Concluída', 20.0, 'Certificado de conclusão enviado.'),
(209,'592ae434-f44b-49ed-a9c8-96012fa6b6b4', 'Congresso de Engenharia Naval', '2024-08-10 14:00:00+00', 'Concluída', 19.0, 'Certificado recebido e aprovado.'),
(211,'592ae434-f44b-49ed-a9c8-96012fa6b6b4', 'Workshop de Programação Orientada a Objetos', '2024-08-11 11:00:00+00', 'Em Andamento',  14.0, 'Certificado está sendo preparado.'),
(212,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Curso Avançado de Banco de Dados', '2024-08-12 09:00:00+00', 'Não Iniciado', 16.0, 'Certificado pendente de recebimento.'),
(213,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Curso de Simulação Computacional', '2024-08-13 10:00:00+00', 'Concluída', 18.0, 'Certificado enviado e recebido.'),
(214,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Curso de Estatística para Dados', '2024-08-14 12:00:00+00', 'Em Andamento',  22.0, 'Certificado em fase de revisão.'),
(215,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Curso Avançado de Engenharia de Software', '2024-08-15 13:00:00+00', 'Concluída', 20.0, 'Certificado recebido e validado.'),
(216,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Curso de Inteligência Artificial', '2024-08-16 14:00:00+00', 'Não Iniciado', 25.0, 'Certificado pendente.'),
(217,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Workshop de Redes de Computadores', '2024-08-17 09:00:00+00', 'Em Andamento', 18.0, 'Certificado em revisão.'),
(218,'7d66b522-c4c2-45c9-8682-25b61cf8af1e', 'Seminário sobre Gestão de Projetos', '2024-08-18 11:00:00+00', 'Concluída', 15.0, 'Certificado enviado e aprovado.'),
(219,'5167a075-437f-465c-bbf1-684cba8b516f', 'Curso de Análise de Dados', '2024-08-19 10:00:00+00', 'Concluída', 14.0, 'Certificado recebido.'),
(220,'5167a075-437f-465c-bbf1-684cba8b516f', 'Workshop de Arquitetura de Computadores', '2024-08-20 13:00:00+00', 'Não Iniciado', 16.0, 'Certificado pendente.');

select * from atividade
