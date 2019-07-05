from .Lei import Parse, Get




parse = Parse()
href_list = parse.parse_url()
history_href_list = parse.get_history_href(href_list)
# fp = open('CVN.txt', 'w', encoding='utf-8')
print(history_href_list)



