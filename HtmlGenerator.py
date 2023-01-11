from mako.template import Template

class HtmlGenerator:
    
    def __init__(self):
        pass

    def generate_html_doc(self, data):

        chat_history_html = Template(filename="./Templates/SortedConversationHistory.html").render(data=data)
        f = open("./Output/SortedConversationHistory.html", "w")
        f.write(chat_history_html)
        f.close()
