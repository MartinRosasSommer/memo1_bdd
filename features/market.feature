Feature: Going to the market

  Scenario: Buying water
    Given 100 pesos
    When trying to pay
    Then the cashier should receive the money