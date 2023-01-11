#!/usr/bin/env python3

from JsonParser import JsonParser
from HtmlGenerator import HtmlGenerator

def main():
    
    # Parse chat history JSON
    jsonParser = JsonParser()
    chat_history_json_list = jsonParser.get_json_string_from_file("./SnapchatData/mydata/json/chat_history.json")

    # Generate sorted chat history html file
    htmlGenerator = HtmlGenerator()
    htmlGenerator.generate_html_doc(chat_history_json_list)

if __name__ == "__main__":
    main()
