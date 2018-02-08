This repository contains the data used in the paper "'More than Meets the Eye' – Analyzing the Success of User Queries in a Library Discovery System" (tbp.).

The CSV files use comma as delimiter and " as escape character.
They are UTF-8 encoded with Unix linebreaks, and the first line of each contains column headers.
The `stats.py` Python 3 script can be used to print some basic statistics on the two sets.

* `popular.csv` is the complete "Popular Searches" dataset of 5776 rows, each containing aggregated data for a *month*. It contains the following columns:
	* `year`: The year
	* `month`: The month number (starting at 1 for January)
	* `searches`: The number of the times the query (`Search String` in `Active Tab`) was carried out in the given month
	* `search string`: The raw query string
	* `search string cleaned`: The cleaned query string
	* `active tab`: The tab in which the search was made, can take the values `default_tab` (the local library catalogue + Primo Central Index), `library_catalogue` (just the local library catalogue) or `alle_bibliotek` (the library catalogues of all Norwegian research libraries in the Bibsys consortium).
	* `signed in`: The number of times the user was signed-in.
	* `on campus`: The number of times the user was using an IP address from UiO.
	* `results`: Average number of results per search

* `popular_top50.csv` is the overall top 50 (cleaned) queries from the Popular Searches dataset. It contains the following columns, all but the first which hold manual annotations:
	* `search string cleaned`: The cleaned query string
	* `query type`: either `author`, `title`, `author+title`, `isbn`, `topic`, `topic/title` or `_unknown`.
	* `intended resource`: the type of resource we believe the user was looking for.
	* `successful`: whether the query returned meaningful results.
	* `pensum-related`: whether the query was for curriculum material.
	* `total searches`: the total number of searches for this (cleaned) query string across the Popular Searches dataset.

* `zero.csv` is the complete "Zero Results" dataset of 39925 rows, each containing aggregated data for a *day*. Columns:
	* `date`: The date
	* `searches`: The number of the times the query (`Search String` in `Active Tab`) was carried out in the given day
	* `search string`: The raw query string
	* `search string cleaned`: The cleaned query string
	* `fields searched`: The search fields used.
	* `search type`: type of operator used, either `keyword` (default), `exact` (phrase) or `starts with`)
	* `active tab`: The tab in which the search was made, can take the values `default_tab` (the local library catalogue + Primo Central Index), `library_catalogue` (just the local library catalogue) or `alle_bibliotek` (the library catalogues of all Norwegian research libraries in the Bibsys consortium).
	* `resource type`: resource type pre-filter (e.g. Books or Articles)
	* `signed in`: The number of times the user was signed-in.
	* `on campus`: The number of times the user was using an IP address from UiO.

* `zero_sample.csv` is the sample of 50 random queries from the "Zero Results" dataset. Note that since `zero.csv` is sorted randomly, these are actually the first 50 rows of that set. In addition to the columns from `zero.csv`, the following manually annotated columns have been added:
	* `type of query`: Type of query. One of `author`, `citation`, `isbn`, `title`, `topic` or `source text` (excerpt from fulltext?)
	* `reason no results`: The reason a query failed. One of
	  * `wrong scope`: no results in this tab/scope, but results could be found by switching to another tab/scope
	  * `wrong field`: using the wrong search field
	  * `not available`: search for a known item that just doesn't exist in Oria
	  * `pasted citation`: a citation formatted to some citation style. Removing parts of the string might be necessary to produce results in Oria.
	  * `misspelling`
	  * `not indexed`: search for elements of an available item that aren't searchable. E.g. a book chapter title in a book.
	  * `_unknown`: a query we could not categorize with some certainty
	  * `system issue`: spurious cases where some data are missing and it makes no sense that zero results are returned
	* `resource`: the type of resource we believe the user searched for (without specifying explicitly)
	* `meant`: notes about what we think the user was looking for. This column is incomplete!
	* `pensum`: whether the user was looking for curriculum material
	* `still 0 res?`: whether we still got zero results when we carried out the same search April 18-20, 2017.
	* `spelling suggestion`: whether we got a "Did you mean...?" notice from the system when we carried out the same search April 18-20, 2017.
