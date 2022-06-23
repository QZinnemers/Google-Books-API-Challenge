import yaml
import requests

'''
2. Get title by ISBN
Write a script in Python that shows the title of a book for a given ISBN number.
'''


def getbooks(isbn):
    # request to endpoint
    res = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn+'&=')
    bookInfo = res.json()  # convert to json
    BookTitle = bookInfo['items'][0]['volumeInfo']['title']  # read title
    print(BookTitle)

# todo: error catching


def customInput():
    isbnInput = input("Enter the ISBN Number: ")
    if len(isbnInput) == 0:
        isbnInput = "9780884271956"  # default value
    getbooks(isbnInput)

# customInput()
# ==================================================


'''
3. Get titles by ISBN list
Loop through data
'''


def loopIsbn():
    collection = ["9780141036144", "9780099518471",
                  "9780099560432", "9781784971571"]
    for x in collection:
        getbooks(x)

# loopIsbn()


# ==================================================
'''
4. Show specific book data
Using the Google Books API, write a script that given an author, does the following:
Show the amount of results that match the query
Print ID, Title and ISBN number to screen

'''


def specificData(author):
    # request to endpoint

    res = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q=inauthor:' + author + '&=')

    bookInfo = res.json()  # convert to json
    totalMatch = str(len(bookInfo['items']))
    print(f''+author + ' has a total of ' + totalMatch + ' book matches')
    print('Here is a list of all the books:')
    print('================================')

    for x in range(int(totalMatch)):
        id = bookInfo['items'][x]['id']
        title = bookInfo['items'][x]['volumeInfo']['title']
        isbn = bookInfo['items'][x]['volumeInfo']['industryIdentifiers'][-1]['identifier']
        print(f'Title: ' + title + ' || ID: ' + id + ' || ISBN: ' + isbn)

    print('================================')


# specificData("Jeff Cox")  # OPT get user input

# ==================================================
'''Bonus: Create yaml'''


def yamlData():
    collection = ["9780141036144", "9780099518471",
                  "9780099560432", "9781784971571"]

    combinedBooks = []

    for x in collection:
        res = requests.get(
            f'https://www.googleapis.com/books/v1/volumes?q=isbn:'+x+'&=')
        bookJson = res.json()  # convert result  to json

        my_dict = {}
        my_dict['id'] = bookJson['items'][0]['volumeInfo']['title']
        my_dict['title'] = bookJson['items'][0]['volumeInfo']['title']
        my_dict['isbn'] = bookJson['items'][0]['volumeInfo']['industryIdentifiers'][-1]['identifier']
        my_dict['pages'] = bookJson['items'][0]['volumeInfo']['pageCount']
        combinedBooks.append(my_dict)

    print(yaml.dump(combinedBooks, default_flow_style=False))
    yamlFile = open("bookData.yml", "w")
    yamlFile.write(yaml.dump(combinedBooks, default_flow_style=False))
    yamlFile.close()


yamlData()
