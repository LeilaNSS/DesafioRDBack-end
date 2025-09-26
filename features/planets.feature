Feature: Filmes da API Star Wars
  Como consumidor da API
  Quero consultar os filmes de Star Wars
  Para validar os dados e garantir que estão corretos


  Scenario: Listar todos os planetas
    When eu consulto o endpoint "/planets/"
    Then o status code deve ser 200
    And cada planeta deve ter os atributos obrigatórios

  @filme
  Scenario: Consultar um planeta válido
    When eu consulto o endpoint "/planets/1/"
    Then o status code deve ser 200
    And O planeta deve ter os atributos obrigatórios

  Scenario: Consultar um planeta inválido
    When eu consulto o endpoint "/planets/9999/"
    Then o status code deve ser 404

