Feature: A script that procures the current temperature of a place through the facade design pattern

As a user I want to know the temperature of a specific place

Scenario: Get today's temperature of the city
Given I am connected to the internet
And I input city as "Iligan" and country as "PH"
When I run the script "facade.py"
Then I see the temperature "26.63"
And I see a cached file "myfile" in "/home/joren/18activities/18series/184/facade/facade"
