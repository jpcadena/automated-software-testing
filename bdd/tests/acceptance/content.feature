Feature: Test that pages have correct content
  Scenario: Blog page has a correct title
    Given I am on the blog page
    Then There is a title shown on the page
    And The title tag has content "This is the blog page"
