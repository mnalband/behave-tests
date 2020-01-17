Feature: Use ruler for random calculations

   Use ruler for random calculations

    Scenario: Check ruler's initial state
        Given I want to open main page
        And I want to check ruler state
        Then I see range '20'
        And Ruler controls
        And Ruler start
        And Ruler continue '1' times
        And Input numbers are in range '20'

    Scenario: Increase ruler range
        Given I want to increase ruler range 1 times
        Then I see range '30'
        And Input numbers are in range '30'
        And Ruler continue '2' times

    Scenario: Decrease ruler range
        Given I want to decrease ruler range 2 times
        Then I see range '10'
        And Input numbers are in range '10'
        And Ruler continue '0' times

    Scenario: Check that maximum range is 100 even if clicks continue
        Given I want to increase ruler range 15 times
        Then I see range '100'
        And Input numbers are in range '100'

    Scenario: Check that minimum range is 10 even if clicks continue
        Given I want to decrease ruler range 15 times
        Then I see range '10'
        And Input numbers are in range '10'
