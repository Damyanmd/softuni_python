data = input()

methods = {'post': [], 'get': []}

while data != 'END':
    _, path, method = data.split('/')
    methods[method].append(path)
    data = input()

http_request = input().split('/')
method_untrim = http_request[0].lower()
command_method = ''.join(list(filter(None, method_untrim.split())))
path = http_request[1].split()

if path[0] in methods[command_method]:
    print(f'''{path[1]} 200 OK
Content-Length: 2
Content-Type: text/plain
\nOK
    ''')
else:
    print(f'''{path[1]} 404 Not Found
Content-Length: 9
Content-Type: text/plain
\nNot Found
    ''')