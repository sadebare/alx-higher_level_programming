#!/usr/bin/python3
"""adds all arguments to a Python list and save them to file"""
import sys
import json
import os.path
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file.py
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file.py


filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, filename)
