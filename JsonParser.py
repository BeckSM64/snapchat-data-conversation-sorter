
import json
from operator import itemgetter

class JsonParser():
    
    def __init__(self):
        self.combined_chat_history_list = []

    def get_json_string_from_file(self, jsonFile):
        f = open(jsonFile)
        data = json.load(f)

        try:
            self.combined_chat_history_list = data["Received Saved Chat History"] + data["Sent Saved Chat History"]
            self.combined_chat_history_list.sort(key = itemgetter('Created'), reverse=False)
            # self.combined_chat_history_list.sort(key = itemgetter('Created'), reverse=False)

        except:
            print("ERROR: Invalid JSON file")
        
        return self.combined_chat_history_list
