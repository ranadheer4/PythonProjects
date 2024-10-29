Feature: CMD Login
  Background: common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login

  Scenario: Login to CMD application with valid parameters
    Then user must login to the cmd homepage

  Scenario: Search user
    When navigates to search page
    Then search page should display

  Scenario: Advanced user search
    When navigates to advanced search page
    Then advanced search page should display

