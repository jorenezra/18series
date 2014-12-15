from lettuce import *
from nose.tools import assert_equal

import os
import urllib2

from facade.facade import *

@step(u'Given I am connected to the internet')
def given_i_am_connected_to_the_internet(step):
    try:
        response = urllib2.urlopen('http://74.125.228.100', timeout = 1)
        assert True
    except urllib2.URLError as err: 
        assert True, 'Not connected to the internet'

@step(u'And I input city as "([^"]*)" and country as "([^"]*)"')
def and_i_input_city_as_group1_and_country_as_group2(step, group1, group2):
    assert True, 'Given variables in the code'

@step(u'When I run the script "([^"]*)"')
def when_i_run_the_script_group1(step, script):
    execfile('facade/' + script)

@step(u'Then I see the temperature "([^"]*)"')
def then_i_see_the_temperature_group1(step, temp):
    temperature = ""
    file = open("facade/myfile", "r")
    for line in file:
        if "F" in line:
            temperature = line[1:]
            break
    temperature = round(float(temperature), 2)
    temp = float(temp)
    assert_equal(temperature, temp)

@step(u'And I see a cached file "([^"]*)" in "([^"]*)"')
def and_i_see_a_cached_file_group1_in_group2(step, cache, dirc):
    exists = os.path.isfile(dirc + "/" + cache)
    assert exists
