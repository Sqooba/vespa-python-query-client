
## Simple Python3 CLI to Vespa.ai's search interface

[Vespa.ai](http://vespa/) seems to miss a simple CLI to issue search requests to the http interface.

At this point this simply takes a `YQL` query, url-encodes it and sends it off, while pretty printing the result. 

### Dependencies
 - `absl` - flags parsing - `pip install absl-py`
 - `requests` - http client - `pip install requests`

### Sample usage:

    $ ./vespa-search.py --yql "select * from sources * where default contains 'bob';" --param hitcountestimate=True,tracelevel=2


Additional functionalities will be added progressively. Currently only using python3, but should be ok with Python2 as well.
