Feature: CMD Login

  @completed
  Scenario: Login to CMD application with valid parameters
    Given I launch Chrome browser
    When I open CMD Login home page
    And Enter username "ctg@credentialmydoc.com" and password "ctgadmin2018"
    And Click on login button
    Then User must succesfully login to the Dashboard page

  Scenario Outline: Login to CMD application with multiple parameters
    Given I launch Chrome browser
    When I open CMD Login home page
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must succesfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin@123 |
      | ctg@credentialmydoc.com | ctgadmin2018 |
      | admin45                 | adbkjhbj     |
      | svbfb                   | dsvgew       |

