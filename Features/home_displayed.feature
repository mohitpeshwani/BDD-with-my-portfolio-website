Feature: To verify the end to end functionality of the portfolio website

  Scenario: To check wheather the logo no the webpage is visible or not
    Given I go to the website
    When Looking for the logo in the header


  Scenario Outline: checking the menu bar of my portfolio website
    Given I go to the website
    When Menu bar in desktop mode
    Then verifying wheather the buttons <items>
    Examples:
      | items    |
      | home     |
      | blogs    |
      | about    |
