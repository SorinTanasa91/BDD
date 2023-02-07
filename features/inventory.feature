Feature: Check inventory functionality
  Background:
    Given login: I am an user on the login page
    When login:I fill the username with wrong values "standard_user"
    When login:I fill the password with the wrong value "secret_sauce"
    When login:I click the login button
    Then inventory: I am in an inventory page

    Scenario: Inventory click settings button
      When inventory: I click on the settings button
      Then inventory: Settings list is displayed

