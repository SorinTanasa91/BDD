Feature: Check the login functionality
  Background:
    Given login: I am an user on the login page

    @smoke
    Scenario: Try to login with wrong credentials
      Given login: I am not an user on the login page
      When login:I fill the username with wrong values "username"
      When login:I fill the password with the wrong value "password"
      When login:I click the login button
      Then login:Error message is displayed with the message "Epic sadface: Username and password do not match any user in this service"
    @test
    Scenario: Try to login with different values
      Given login: I am not an user on the login page
      When login: Click the login button
      Then login: Error message is displayed with the message: "Epic sadface: Username is required"
    @login
    Scenario: Try to login with correct values
      Given login: I am an user on the login page
      When login:I fill the username with values "standard_user"
      When login:I fill the password with value "secret_sauce"
      When login:I click the login button
      Then Inventory: The url has changed

    @outline_test
    Scenario Outline: Try to login with different values
      When login:I fill the username with wrong value "username"
      When login:I fill the password with the wrong value "password"
      When login:I click the login button
      Then login:Error message is displayed with the message "error"

       Examples:
      | username        | password         |  error                                  |
      | username_123    |   wrong          |  Epic sadface: Username and password do not match any user in this service     |
      | wrong           |   pwd            |  Epic sadface: Username and password do not match any user in this service     |

    Scenario: Try to login without password, only username
      When login: I fill the password with the wrong value "password"
      When login: O click the login button
      Then login: Error message is displayed with the message: "Epic sadface: Password is required"