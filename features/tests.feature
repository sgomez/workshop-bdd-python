#language: en
Feature: Pay for a menu
    Rules:

    - 1 point for each euro.
    - 10 points equals a discount of 1 euro.
    - VAT is 10%.

    Background:
        Given the following menus:
            | number | price |
            | 1      | 10    |
            | 2      | 12    |
            | 3      | 8     |

    Scenario: Earning points by paying cash
        Given that I have bought 5 menus of number 1
        When I ask for the bill, I receive a bill for 55 euros
        And I pay in cash with 55 euros
        Then the bill is paid
        And I have earned 50 points

    Scenario: Paying with cash and points
        Given that I have bought 5 menus of number 1
        When I ask for the bill, I receive a bill for 55 euros
        And I pay with 10 points and 54 euros
        Then the bill is paid
        And I have earned 0 points

    Scenario: Paying with points
        Given that I have bought 5 menus of number 1
        When I ask for the bill, I receive a bill for 55 euros
        And I pay with 500 points and 5 euros
        Then the bill is paid
        And I have earned 0 points

    Scenario: Trying to pay the VAT with points
        Given that I have bought 5 menus of number 1
        When I ask for the bill, I receive a bill for 55 euros
        And I pay with 550 points and 0 euros
        Then there are 5 euros left to pay

    Scenario: Buying menus of various types
        Given that I have bought 1 menu of number 1
        And that I have bought 2 menus of number 2
        And that I have bought 2 menus of number 3
        When I ask for the bill, I receive a bill for 55 euros
        And I pay in cash with 55 euros
        Then the bill is paid
        And I have earned 50 points
