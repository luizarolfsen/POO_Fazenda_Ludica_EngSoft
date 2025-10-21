# POO_Fazenda_Ludica_EngSoft
Exercício aula 08 de Engenharia de Software - Professor Luan
Objetivo: Aplicar os conceitos de Classe, Objeto, Herança e Polimorfismo, além de iniciar a prática de Encapsulamento, criando um sistema simples de gerenciamento de animais em uma fazenda lúdica.

Enunciado
Você foi contratado(a) para desenvolver um pequeno sistema que simula a interação com animais em uma fazenda. Utilize Python e siga as instruções abaixo, aplicando os pilares da POO estudados.

1. Abstração e Classe Base (Animal)
Crie uma Classe Base chamada Animal. Esta classe deve abstrair as características e comportamentos comuns a todos os animais da fazenda:

Atributos (Abstração):

nome (string)

idade (inteiro)

Métodos (Abstração/Polimorfismo):

__init__(self, nome, idade): O construtor para inicializar os atributos.

emitir_som(self): Deve ser um método genérico. Implemente-o para apenas retornar a string "O animal emite um som." (Este método será especializado nas subclasses).

apresentar(self): Retorna uma string no formato: "Olá, sou [nome] e tenho [idade] anos."

2. Herança e Especialização
Crie as seguintes Subclasses que herdam da classe Animal:

Subclasse 1: Cachorro

Deve herdar todos os atributos e métodos de Animal.

Deve adicionar um novo atributo específico: raca (string).
  
Polimorfismo: Sobrescreva o método emitir_som() para retornar a string "Au! Au!".

Subclasse 2: Gato

Deve herdar todos os atributos e métodos de Animal.

Deve adicionar um novo atributo específico: cor_pelo (string).

Polimorfismo: Sobrescreva o método emitir_som() para retornar a string "Miau!".

Subclasse 3: Vaca

Deve herdar todos os atributos e métodos de Animal.

Deve adicionar um novo atributo específico: producao_leite_litros (float).

Polimorfismo: Sobrescreva o método emitir_som() para retornar a string "Muuu!".

3. Encapsulamento (Proteção de Dados)
Na classe Vaca, aplique o encapsulamento no atributo producao_leite_litros:

Modifique o atributo para ser privado (em Python, use o prefixo __). Ex: __producao_leite_litros.

Crie um método getter público chamado obter_producao_leite() que retorna o valor de __producao_leite_litros.

Crie um método setter público chamado registrar_ordenha(litros) que permite modificar o valor de __producao_leite_litros (simulando a ordenha diária).

4. Teste e Demonstração
No seu código principal (fora das classes):

Crie instâncias (Objetos) de cada uma das subclasses:

Um objeto Cachorro (ex: "Rex", 3 anos, "Labrador").

Um objeto Gato (ex: "Mimi", 5 anos, "Branco").

Um objeto Vaca (ex: "Mimosa", 7 anos, 25.5 litros).

Chame os métodos para cada objeto:

Chame o método apresentar() para todos os objetos e imprima o resultado.

Chame o método emitir_som() para todos os objetos e imprima o resultado.

Teste de Encapsulamento:

Para o objeto Vaca, imprima a produção atual utilizando o método getter.

Chame o método registrar_ordenha() para mudar a produção de leite (ex: para 28.0 litros).

Imprima novamente a produção de leite para confirmar a mudança.

Instruções de Entrega do Exercício Prático
Para este exercício, a entrega não será apenas o código-fonte, mas também o processo de Engenharia de Software amplamente utilizado na indústria: o Controle de Versão com Git e GitHub.

1. Preparação e Controle de Versão (Git e GitHub)
O controle de versão é crucial para gerenciar mudanças no código, colaborar com outros desenvolvedores e manter um histórico confiável do projeto.

Criação do Repositório:

Acesse sua conta no GitHub (crie uma se ainda não tiver).

Crie um novo repositório com um nome claro e relevante (exemplo: POO_Fazenda_Lúdica). Escolha a opção para inicializar o repositório com um arquivo README.md.

Desenvolvimento do Código:

Crie o arquivo Python (fazenda_ludica.py ou similar) com a solução do exercício na sua máquina local.

Utilize o Git para inicializar o repositório localmente.

Commit e Envio (Push):

Adicione o arquivo Python ao Git.

Faça o primeiro commit com uma mensagem clara (ex: "Implementação das classes Animal, Cachorro e Gato com Herança e Polimorfismo").

Sincronize seu repositório local com o GitHub, enviando (dando push) seu código para o repositório remoto que você criou.

Verificação:

Certifique-se de que o seu arquivo Python (com o código-fonte completo) e o arquivo README.md estão visíveis no seu repositório público do GitHub.

2. Formato de Entrega
A entrega final do exercício será feita através deste formulário, garantindo que o professor tenha acesso imediato ao seu trabalho.

Obtenção do Link:

Acesse a página principal do seu repositório no GitHub.

Copie a URL completa da barra de endereços (exemplo: https://github.com/SeuUsuario/POO_Fazenda_Lúdica).

Preenchimento do Formulário Google:

No formulário, você deverá fornecer as seguintes informações:

RA

Seu Nome Completo.

IMPORTANTE: Certifique-se de que o seu repositório está configurado como PÚBLICO no GitHub. Repositórios privados não poderão ser acessados para correção, resultando em nota zero para o exercício. O prazo de entrega deve ser rigorosamente respeitado.

Este exercício garantirá que vocês pratiquem a definição de classes, o uso de herança para reutilizar a estrutura base, o polimorfismo na especialização do método emitir_som(), e a importância do encapsulamento para proteger e controlar o acesso a dados críticos.