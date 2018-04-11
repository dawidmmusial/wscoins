from urllib import request

def get_cryptocurrency(url):
    """Get cryptocurrency info from url"""
    jurl = request.urlopen(url)
    data = jurl.read().decode('utf-8')
    return data