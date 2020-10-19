Feature: Driving a car

  Scenario: Speeding up car
    Given A car
    When Stepping on accelerator pedal
    Then Speed should raise

  Scenario: Slowing down car
    Given A car
    When Stepping on brake pedal
    Then Speed should decrease
