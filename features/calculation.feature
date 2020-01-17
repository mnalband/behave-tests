Feature: Check basic calculations

    Scenario: Calculate given numbers correctly
        Given I want to open main page
        And I want to calculate given numbers
        Then Input correct answer
        And Click submit
        Then See happy elephant

    Scenario: Calculate given numbers incorrectly
        Given I want to open main page
        Then Input incorrect answer
        And Click submit
        Then See angry monkey

    Scenario: Submit empty result and check for error
        Then Click submit
        And See angry monkey
