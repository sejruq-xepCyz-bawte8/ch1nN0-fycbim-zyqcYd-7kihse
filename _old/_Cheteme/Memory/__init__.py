
from anvil.js.window import awesomeColl, genresColl, keywordsColl, worksColl, contentColl, readerCall, authorsColl
import _icons, _genres, _keywords, _works, _content, _reader, _authors

from .Awesome_Module import Awesome
from .Genres_Module import Genres
from .Keywords_Module import Keywords
from .Works_Module import Works
from .Authors_Module import Authors
from .Content_Module import Content
from .Reader_Module import Reader
print(__name__)

awesome = Awesome(collection=awesomeColl, data=_icons.icons)
genres = Genres(collection=genresColl, data=_genres.genres)
keywords = Keywords(collection=keywordsColl, data=_keywords.keywords)
works = Works(collection=worksColl, data=_works.works)
authors = Authors(collection=authorsColl, data=_authors.authors)
content = Content(collection=contentColl, data=_content.content)
reader = Reader(collection=readerCall, data=_reader.reader)





