Feature: Open main page

    Open index.html

    Scenario: Open main page and check all elements
        Given I want to open main page
        Then I see the default title
        And All elements: calculator and ruler
        But Not operation result

    Scenario: Check initial calculator state
        Given I want to open main page
        Then First input is pre-filled with int
        And Second input is pre-filled with int
        And Operator is either + or -
        But Result input is empty

