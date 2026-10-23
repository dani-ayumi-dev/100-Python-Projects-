
# Dictionary Key Transformation with Python

## About the Project

This project demonstrates how to transform dictionary keys in a list of dictionaries using Python's `map()`, `partial()`, and dictionary comprehension.

The goal is to rename the key `"animal"` to `"insect"` while preserving the associated values and the other dictionary keys.

## Technologies and Concepts

- **Python**
- `map()` — applies a function to each item in an iterable.
- `functools.partial()` — creates a specialized function by pre-filling arguments.
- **Dictionary comprehension** — creates new dictionaries by transforming key-value pairs.
- `list()` — converts an iterable into a list.

## Dataset

The project uses a list of dictionaries containing information about different animals, including their names, colors, and number of legs.

Example:

```python
{"animal": "butterfly", "color": "yellow", "legs": 6}
```

## Expected Transformation

The key `"animal"` is renamed to `"insect"`, while the remaining keys and values stay unchanged.

```python
{"insect": "butterfly", "color": "yellow", "legs": 6}
```

## How It Works

1. A function defines the key-replacement operation.
2. `partial()` creates a specialized version of that function with the old and new key names.
3. Dictionary comprehension constructs a new dictionary with the transformed keys.
4. `map()` applies the transformation function to each dictionary in the dataset.
5. The results can be converted into a list for further processing.

## Learning Objectives

This exercise helped me practice:

- Working with lists of dictionaries.
- Creating reusable functions.
- Understanding how `map()` processes iterable elements.
- Using `partial()` to pre-fill function arguments.
- Transforming dictionary keys without changing their associated values.

## Future Improvements

- Allow users to choose which key to rename.
- Handle dictionaries that do not contain the specified key.
- Extend the function to support multiple key transformations.
- Add automated tests to validate the results.

---

**Project Type:** Python Practice Project  
**Focus:** Functional Programming and Data Transformation
