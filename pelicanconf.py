AUTHOR = 'Dmitry Kolomatskiy'
SITENAME = "Mitya's Self-Explanatory"
SITEURL = "https://lemontree210.github.io"

PATH = "content"
STATIC_PATHS = ["images"]
THEME = "blue-penguin-dark"

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'  # Thu 05 June 2025
DATE_FORMATS = {
    'en': '%B %-d, %Y',        # "June 5, 2025"
    'ru': '%-d %B %Y г.',      # "5 июня 2025 г."
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("My LinkedIn profile", "https://www.linkedin.com/in/dmitry-kolomatskiy/"),
)

# Social widget
SOCIAL = (
    ("My LinkedIn profile", "https://www.linkedin.com/in/dmitry-kolomatskiy/"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
