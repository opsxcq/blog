---
title: "Making mopidy search in my beets library as I want to"
date: 2017-02-04T00:00:00Z
draft: true
tags: ["mopidy", "music"]
---
* I want to be able to just type any beets query and get it's result

Simple way to access via python

```
lib = beets.library.Library("/music/beetslibrary.blb")
lib.items(unicode('punk'))._row_count
```

It will show how many items matched the query `punk`


# Quick intro about beets queries

Search by:

 * `genre` - Search by genre.
 * `year` - Query by year
 * `title` -
 * `artist` -
 * `year:1990..1999`
 * `length:..4:30`

## Advanced search

Exclude (`^`) - Exclude the result matching the filter from the final result.

Regular expressions on a single field `"artist::Ann(a|ie)"`

Regular expressions on **ALL** fields `":Ho[pm]eless"`

Sorting

Queries can specify a sort order. Use the name of the field you want to sort on,
followed by a + or - sign to indicate ascending or descending sort. For example,
this command:

`genre+ year+`

# Debugging

To debug I ran mopidy with `-v` flag, this is enough to print the logs that will
be needed.

# Code

Here is the new `search` function

```python
    def search(self, query=None, uris=None, exact=False):
        logger.debug(u'Search query: %s in uris: %s' % (query, uris))
        # import pdb; pdb.set_trace()
        query = self._sanitize_query(query)
        logger.debug(u'Search sanitized query: %s ' % query)
        if exact:
            return self._find_exact(query, uris)
        albums = []
        if not query:
            uri = 'beetslocal:search-all'
            tracks = self.lib.items()
            albums = self.lib.albums()
        else:
            uri = uricompose('beetslocal',
                             None,
                             'search',
                             query)
            if 'any' in query:
                filtered = ''
                normalized =  [ (token.strip())for token in query['any'][0].split(',')]
                for token in normalized:
                    filtered = filtered + " " + "\"" +token+ "\""
                logger.debug(u'Running beets query: %s' % filtered)
                tracks = self.lib.items(filtered)
            else:
                track_query = self._build_beets_track_query(query)
                logger.debug(u'Build Query "%s":' % track_query)
                tracks = self.lib.items(track_query)
                if 'track_name' not in query:
                    # when trackname queried dont search for albums
                    album_query = self._build_beets_album_query(query)
                    logger.debug('Build Query "%s":' % album_query)
                albums = self.lib.albums(album_query)
        logger.debug(u"Query found %s tracks and %s albums"
                     % (len(tracks), len(albums)))
        return SearchResult(
            uri=uri,
            tracks=[self._convert_item(track) for track in tracks],
            albums=[self._convert_album(album) for album in albums]
        )

```

# Test

![working](mopidy-query-working.png)

# Add to Rofi

Shell

`mpc -f '%artist% - %title%' search any 'genre:punk, ^green day, ^yellow'`

Use rofi to choose the current 


```
#!/bin/bash

if [ -z "$1" ]
then
  mpc lsplaylists
else
  mpc clear >/dev/null
  mpc load $1 >/dev/null
  mpc play >/dev/null
fi
```

And invoke rofi with 

`rofi -show 'Choose your playlist' -modi 'Choose your playlist:./list.sh'`

# Useful References

 * [https://beets.readthedocs.io/en/v1.3.16/dev/plugins.html](https://beets.readthedocs.io/en/v1.3.16/dev/plugins.html)
 * [Mopidy Beets local plugin](https://github.com/rawdlite/mopidy-beets-local/blob/master/mopidy_beetslocal/library.py)
 * [Query Reference](http://beets.readthedocs.io/en/v1.4.4/reference/query.html)
