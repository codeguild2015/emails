from emails_nick_patrick import *



def list_split_test_empty():
    assert list_split([]) == []

def list_split_test_from():
    assert list_split(["From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"]) == [["From", "stephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"]]

def list_split_test_not_from():
    assert list_split(["Return-Path: <postmaster@collab.sakaiproject.org>"]) == []

def build_count_dict_empty():
    assert build_count_dict([]) == {}

def build_count_dict_name():
    assert build_count_dict([["From", "stephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"]]) == {"stephen.marquard@uct.ac.za" : 1}
 
def prep_most_last():
    assert prep_out_most({"Patrick" : 10, "Nick" : 20}) == ("Nick", 20)

def prep_most_first():
    assert prep_out_most({"Patrick" : 35, "Nick" : 10}) == ("Patrick", 35)

print("Success!")