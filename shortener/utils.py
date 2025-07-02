import pyshorteners


def shorten_url(url):
    shortener = pyshorteners.Shortener()
    try:
        shortened_url = shortener.tinyurl.short(url)
        print("shortened url : ", shortened_url)
        return shortened_url
    except Exception as e:
        return str(e)
