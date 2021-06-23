from urllib import parse
import re

def get_protocol(scheme):
    if scheme in ('http', 'https'):
        return scheme
    return None

def get_host_and_port(netloc, scheme):
    if ':' not in netloc:
        default_port = 80 if scheme == 'http' else 443
        netloc = f'{netloc}:{default_port}'

    return netloc.split(':')

def get_path(path):
    if path:
        return path
    return '/'

def get_fragment(fragment):
    return fragment

def get_query(query):
    return query

def validate_url(url, regex):
    components = parse.urlparse(url)
    protocol = get_protocol(components.scheme)
    host, port = get_host_and_port(components.netloc, components.scheme)
    path = get_path(components.path)
    query = get_query(components.query)
    fragment = get_fragment(components.fragment)
    if re.match(regex, url) is not None:
        return (f'''Protocol: {protocol}
Host: {host}
Port: {port}
Path: {path}
Query: {query}
Fragment: {fragment}
    ''')
    else:
        return ('Invalid URL')

urls_undecoded = [
    'http://softuni.bg/',
    'https://softuni.bg:447/search?Query=pesho&amp;Users=true#go',
    'http://google:443/'
]

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

for url in urls_undecoded:
    print(validate_url(url, regex))

