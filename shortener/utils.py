import pyshorteners


def shorten_url(url):
    shortener = pyshorteners.Shortener()
    try:
        shortened_url = shortener.tinyurl.short(url)
        return shortened_url
    except Exception as e:
        return str(e)
