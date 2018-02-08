This repository contains the data used in the paper "'More than Meets the Eye' – Analyzing the Success of User Queries in a Library Discovery System" (tbp.).

### Contents

The CSV files use comma as delimiter and " as escape character.
They are UTF-8 encoded with Unix linebreaks, and the first line of each contains column headers.
The `stats.py` Python 3 script can be used to print some basic statistics on the two sets.

* `popular.csv` is the complete "Popular Searches" dataset with 5776 rows, each containing aggregated data for a *month*. It contains the following columns:
	* `year`: The year.
	* `month`: The month number (starting at 1 for January).
	* `searches`: The number of the times the query was carried out in the given month.
	* `search string`: The raw query string.
	* `search string cleaned`: The cleaned query string.
	* `active tab`: The tab/scope in which the search was made, either `default_tab` (the University of Oslo library catalogue + the Primo Central Index), `library_catalogue` (just the library catalogue) or `alle_bibliotek` (the library catalogues of all Norwegian academic libraries part of the Bibsys consortium).
	* `signed in`: The number of searches where the user was signed-in.
	* `on campus`: The number of times where the user was using an IP address from the University of Oslo.
	* `results`: The average number of results per search.

* `popular_top50.csv` is the overall top 50 (cleaned) queries from the Popular Searches dataset. It contains the following columns, all but the first which contain manually coded values:
	* `search string cleaned`: The cleaned query string.
	* `query type`: Either `author`, `title`, `author+title`, `isbn`, `topic`, `topic/title` or `_unknown`.
	* `intended resource`: The type of resource we assume that the user was looking for.
	* `successful`: Whether the first result page included the resource likely sought for.
	* `curriculum-related`: Whether the resource likely sought for could be identified as curriculum material.
	* `total searches`: The total number of searches for this (cleaned) query string across the Popular Searches dataset.

* `zero.csv` is the complete "Zero Results" dataset with 39925 rows, each containing aggregated data for a *day*. Columns:
	* `date`: The date.
	* `searches`: The number of the times the query was carried out in the given day.
	* `search string`: The raw query string.
	* `search string cleaned`: The cleaned query string.
	* `fields searched`: The search fields used.
	* `search type`: type of operator used, either `keyword` (default), `exact` (phrase) or `starts with`).
	* `active tab`: The tab/scope in which the search was made, either `default_tab` (the University of Oslo library catalogue + the Primo Central Index), `library_catalogue` (just the library catalogue) or `alle_bibliotek` (the library catalogues of all Norwegian academic libraries part of the Bibsys consortium).
	* `resource type`: Resource type selected in the search box (e.g. Books or Articles).
	* `signed in`: The number of searches where the user was signed-in.
	* `on campus`: The number of times where the user was using an IP address from the University of Oslo.

* `zero_sample.csv` is the sample of 50 random queries from the "Zero Results" dataset. In addition to the columns in `zero.csv`, the following manually coded columns have been added:
	* `type of query`: Type of query. One of `author`, `citation`, `isbn`, `title`, `topic` or `source text` (excerpt from fulltext?)
	* `reason no results`: The “reason” for zero results. One of the following values:
	  * `wrong scope`: No results in this tab/scope, but results would be found by switching to another tab/scope.
	  * `wrong field`: Query entered in the wrong search field.
	  * `not available`: Search for a valid resource that just didn't exist in Oria.
	  * `pasted citation`: The query is a citation formatted to some citation style, likely to have been pasted. Removing parts of the string might be necessary to find the resource.
	  * `misspelling`
	  * `not indexed`: Search for elements (of a valid resource) that weren't searchable. E.g. for a book chapter title in a book.
	  * `_unknown`: A query we couldn't categorize with some certainty.
	  * `system issue`: Spurious case where some data was missing, and it made no sense that zero results were returned.
	* `resource`: The type of resource we assume the user looked for.
	* `meant`: Notes about what we assume the user was looking for. This column is incomplete!
	* `curriculum-related`: Whether the resource likely sought for could be identified as curriculum material.
	* `still 0 res?`: Whether we still got zero results when we carried out the same search April 18-20, 2017.
	* `spelling suggestion`: Whether we got a "Did you mean...?" notice from the system when we carried out the same search April 18-20, 2017.


### Note on privacy

The risk that search queries can identify the user behind the queries indirectly should be taken seriously.
Famously, following the 2006 AOL data release, the New York Times managed to reveal the identify of one of the users based on hundreds of searches over a three-month period ([Michael Barbaro & Tom Zeller, Jr., *A Face Is Exposed for AOL Searcher No. 4417749.* N.Y. Times, Aug.  9, 2006](https://www.nytimes.com/2006/08/09/technology/09aol.html?_r=0). See also the account in [Paul Ohm. *Broken Promises of Privacy: Responding to the Surprising Failure of Anonymization.* UCLA Law Review, vol. 57 (2019), p. 1701](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1450006)).

The identification risk in this dataset is small because there are no anonymized user identifiers included. There are thus no links between different queries, and identifying a user from a single query is much harder than identifying one from a series of queries over time.

There is nothing that prevents a single query from being revealing, but we have yet to see examples of anything that resembles the kind of revealing searches you find in general purpose search engines like Google. Oria searches tend to be “business-like”, to-the-topic.

Finally, we have removed information that could potentially guide identification together with other information, such as the time of the day a search was made, or the browser or operating system used.
