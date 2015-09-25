from timeofday_nick_patrick import *

def from_line_split_test_empty():
    assert from_line_split([]) == []

def from_line_split_test_from():
    #Tests that the function is catching lines beginning with "From"
    assert from_line_split(["From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"]) == [["From", "stephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"]]

def from_line_split_test_not_from():
    #Tests that the function is not catching lines that dont begin with "From"
    assert from_line_split(["Return-Path: <postmaster@collab.sakaiproject.org>"]) == []

def build_count_dict_test_empty():
    assert build_count_dict([]) == {}

def build_count_dict_test_name():
    #Tests that the dictionary key is catching the right index in the list
    assert build_count_dict([["From", "stephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"]]) == {"09" : 1}
 
