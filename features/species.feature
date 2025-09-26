Feature: Species da API Star Wars
  Como consumidor da API
  Quero consultar os species de Star Wars
  Para validar os dados e garantir que estão corretos



  Scenario: Listar todos os species
    When eu consulto o endpoint "/species/"
    Then o status code deve ser 200
    And cada specie deve ter os atributos obrigatórios


  Scenario: Consultar uma specie válido
    When eu consulto o endpoint "/species/1/"
    Then o status code deve ser 200
    And A specie deve ter os atributos obrigatórios

  @Specie
  Scenario: Consultar uma specie inválido
    When eu consulto o endpoint "/species/9999/"
    Then o status code deve ser 404
