Feature: Allow the creation of new draft posts

  Scenario: Create a new post
     Given a beak server
      When the user tries to create a valid post
      Then the post is created

  Scenario: Fail to create a title-less post
     Given a beak server
      When the user tries to create a post with no title
      Then the response is a 400 error
