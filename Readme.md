Resources to get started

REST API
- https://www.restapitutorial.com

Google Books API
Google Books API "lets you perform programmatically most of the operations that you can do interactively on the Google Books website". For this challenge you will only use the `volumes`  endpoint which is publicly available. **There is no need to authorize requests or to acquire an API key.**

Documentation:

- https://developers.google.com/books/docs/overview
- https://developers.google.com/books/docs/v1/using#WorkingVolumes

Tools / Libraries:

- Postman, curl (bash), Invoke-RestMethod (powershell)

Python libraries:

- json, yaml (pyyaml), requests

Challenges
Getting data
1. Get data

Using curl (or Invoke-RestMethod when on powershell), call the Google Books API and answer the following questions by examing the json responses.

	- How many pages does book with ISBN 9780884271956 have?
	- When was "The Phoenix Project" by Gene Kim published?

Learnings:

Read and understand API documentation
Interpret API responses / JSON
Execute simple GET calls to an endpoint
Use query parameters in a GET request
Scripting API calls


2. Get title by ISBN

Write a script in Python that shows the title of a book for a given ISBN number.



Learnings:

Use Python to execute REST API calls
Parse Json responses into Python data objects for further manipulation


Loop through data
3. Get titles by ISBN list

Improve script to show titles of books for the following ISBN numbers:  `["9780141036144","9780099518471", "9780099560432", "9781784971571"]`

4. Show specific book data

Using the Google Books API, write a script that given an author, does the following:

Show the amount of results that match the query
Print ID, Title and ISBN number to screen
Learnings:

Process multiple items in an API response.
Cherry pick specific data from a larger data set


Bonus: Create yaml
5. Create a yaml file based on the book list in question 3, that contains ID, Title, ISBN and amount of page (if present, otherwise set it to 'N/A').

Learnings:

Convert json objects to yaml