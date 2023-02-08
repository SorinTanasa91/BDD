Feature: Check inventory functionality
  Background:
    Given login: I am an user on the login page
    When login:I fill the username with wrong values "standard_user"
    When login:I fill the password with the wrong value "secret_sauce"
    When login:I click the login button
    Then inventory: I am in an inventory page

    @test1
    Scenario: Inventory click settings button
      When inventory: I click on the settings button
      Then inventory: Settings list is displayed

    @test2
    Scenario: Check if logo is displayed
    Then inventory: Logo is displayed

    @test3
    Scenario:Click the cart icon
      When inventory: I click on the cart
      Then cart: Url has changed