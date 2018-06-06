#!/bin/python

# This is a python script to assist with mass html trasformations and
# refactorings

# Author: Thomas Helmkay

from bs4 import BeautifulSoup
import sys

def read_file(path):
    with open(path) as f:
        return f.read()

def attr_predicate(tag):
    return tag.has_attr("th:text")

def process_tag_list(tags):
    filter_string = "{{::'builder' | strings}}"
    for tag in tags:
        th_key = tag["th:text"]
        key = th_key[2:-1]
        del tag["th:text"]
        contents = filter_string.replace("builder",key)
        tag.append(contents)

def handle_file(file_path):
    soup = BeautifulSoup(read_file(file_path), 'html.parser')
    thymeleaf = soup.find_all(attr_predicate)
    # only process if not empty
    if thymeleaf:
        process_tag_list(thymeleaf)
        # write the soup bakc at the file path
        with open(file_path,'wb') as f:
            pretty = soup.prettify()
            f.write(pretty)
# goal of this command is to migrate the th:text tag to an angular filter
if __name__ == "__main__":
    # Read the file paths from std in
    file_path = sys.argv[1]
    #TODO check proepr file path
    handle_file(file_path)
