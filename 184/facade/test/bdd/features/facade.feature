
Feature: Weather forecast application to retrieve the temperature of a given city

As a user I wish to be able to view the temparature of my city

Scenario: Retrieve my city's temperature
Given I live in Iligan City, PH
And I run the python application
Then I see a temperature of "<value returned from api.http://openweathermap.org>"


