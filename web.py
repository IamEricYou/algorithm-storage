import http.server
import socketserver
import requests
import json
import pprint

#PORT = 8000
#
#Handler = http.server.SimpleHTTPRequestHandler
#
#with socketserver.TCPServer(("", PORT), Handler) as httpd:
#    print("serving at port", PORT)
#    httpd.serve_forever()
#

l = 'http://kf.salti.co.kr/api/cms_api_order_info.php?order_info={%22order_num%22:%2220200518001%22,%22barcode%22:%2220200518001_1%22}'
r = requests.get(l)
# print(r.content)
print(r.text)
