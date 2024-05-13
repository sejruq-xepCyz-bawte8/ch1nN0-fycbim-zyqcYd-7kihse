import anvil.server
from anvil.js.window import awesomeColl, genresColl, keywordsColl
import _icons, _genres, _keywords

from .Awesome_Module import Awesome
from .Genres_Module import Genres
from .Keywords_Module import Keywords
print(__name__)

awesome = Awesome(collection=awesomeColl, data=_icons.icons)
genres = Genres(collection=genresColl, data=_genres.genres)
keywords = Keywords(collection=keywordsColl, data=_keywords.keywords)

