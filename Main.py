#!/usr/bin/env python3

import argparse
import sys

from JsonParser import JsonParser
from HtmlGenerator import HtmlGenerator

def main():

    # Parse arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument("data_path", help="chat_history.json exported from Snapchat")
    args = argparser.parse_args()

    # Check args passed in for validity
    path_to_chat_history = args.data_path
    path_to_chat_history_list = path_to_chat_history.split('/')

    # get last element in list, should be file name
    chat_history_file_name = path_to_chat_history_list[-1]

    # check if file name is "chat_history.json"
    if chat_history_file_name != "chat_history.json":
        print("[ERROR] Incorrect file, should be \"chat_history.json\"")
        sys.exit(-1)
    
    # Parse chat history JSON
    jsonParser = JsonParser()
    chat_history_json_list = jsonParser.get_json_string_from_file(path_to_chat_history)

    # Generate sorted chat history html file
    htmlGenerator = HtmlGenerator()
    htmlGenerator.generate_html_doc(chat_history_json_list)

if __name__ == "__main__":
    main()
