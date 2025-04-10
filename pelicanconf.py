AUTHOR = 'h29'
SITENAME = 'h29'
SITEURL = ""
DESCRIPTION = 'hamada2029. Python, JavaScript, SVG.'
STATIC_PATHS = ['images', 'favicon']

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'
DATE_FORMATS = {
    'en': '%Y-%m-%d',
    'jp': '%Y-%m-%d',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
    ("about", "about.html")
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)


MY_SOCIALS = {
    'github': {'nm': 'hamada2029', 'ac': 'hamada2029'},
    'twitter': {'nm': '__h29__', 'ac': '__h29__'}
}

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = 'themes/urban-theme'
