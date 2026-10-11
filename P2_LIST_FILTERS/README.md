# Python Book Grouping with `itertools.groupby()`

A small Python project that organizes a collection of books by a user-selected attribute: name, author, or publication year.

## Features

- **User Input:** Choose which attribute to use for grouping.
- **Dynamic Sorting:** Sorts book dictionaries according to the selected key.
- **Data Grouping:** Uses `itertools.groupby()` to group books with matching values.
- **Formatted Output:** Displays each group under its corresponding attribute value.

## Technologies

- Python
- `itertools.groupby()`
- Lambda functions
- Dictionaries and lists
- `sorted()`

## How It Works

1. Stores book information in a list of dictionaries.
2. Asks the user to choose an attribute: `name`, `author`, or `publication_year`.
3. Uses a lambda function to access the selected dictionary key.
4. Sorts the books by the selected attribute.
5. Groups books with matching values using `groupby()`.
6. Prints the results grouped by the selected attribute.

## Example

**Input:**

    Filter by: author

**Output:**

    GEORGE ORWELL
    {'name': '1984', 'publication_year': 1949, 'author': 'George Orwell'}
    {'name': 'Animal Farm', 'publication_year': 1945, 'author': 'George Orwell'}

    J. K. ROWLING
    {'name': 'Harry Potter and the Chamber of Secrets', ...}
    {'name': "Harry Potter and the Philosopher's Stone", ...}

*The output is abbreviated for readability.*

## How to Run

1. Clone the repository.
2. Make sure Python is installed.
3. Run the script:

   ```bash
   python main.py