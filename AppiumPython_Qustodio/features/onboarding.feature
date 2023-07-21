
Feature: Onboarding Process

  Scenario Outline: app launch and swipe screens validation
    Given the app is launched
    When user performs "<Swipe_Direction>" swipe
    Then should be able to see the next "<Screen_Name>" screen
    Examples:
    | Swipe_Direction | Screen_Name |
    | Left            | Onboarding  |

  Scenario Outline: New User can Sign-Up
    Given the app is launched
    When user performs a tap on "<ButtonName>" button
      And user enter details on sign up screen "<username>", "<email>" and "<password>"
      And user taps on policy agreement
      And user performs a tap on submit button
    Then user should be able to see welcome screen
    Examples:
    | ButtonName| username | email                | password |
    | GetStarted| aditya   | testadi@3gmail.com   | testtest |


  Scenario Outline: User is able to protect device
    Given the app is launched
    And user is logged in with "<username>" and "<password>"
    When user clicks on protect device button
    Then user enters device name
    And user enters child details
    And selects the avatar
    Then user gets enable qustodio page
    And user is able to select settings
   Then user is able to finsh setup
    Examples:
      | username | password |



  Scenario Outline: User is not able to login with invalid credentials
    Given the app is launched
    When user tries to login with invalid "<username>" and "<password>"
    Then user is given error message
    Examples:
      | username | password |



