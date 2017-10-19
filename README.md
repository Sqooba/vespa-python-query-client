
## Simple Python3 CLI to Vespa.ai's search interface

[Vespa.ai](http://vespa.ai/) seems to miss a simple CLI to issue search requests to the http interface.

At this point this simply takes a `YQL` query, url-encodes it and sends it off, while pretty printing the result. 

### Dependencies
 - `absl` - flags parsing - `pip install absl-py`
 - `requests` - http client - `pip install requests`

### Sample usage:
	
	# Simple query
	$ ./vespa-search.py --query bob
	
	# With parameters
	$ ./vespa-search.py --query bob --param hitcountestimate=True,tracelevel=2
	
	# Or a complete YQL query
	$ ./vespa-search.py --yql "select * from sources * where default contains 'bob'"

Additional functionalities will be added progressively. Currently only using python3, but should be ok with Python2 as well.

### Vespa YQL/Query Cheat sheet

##### Partial tag list matches

If `tags` is an `array<string>` field, documents can be retrieved based on the tags they contains using `weightedSet(<field>,{'<findMe1>':<weight>, ...})`. The weights will be used to rank the document, and documents do not need to contain all tags to be returned:
    
    select * from sources * where weightedSet(tags, {'juicy': 50, 'boring':1})