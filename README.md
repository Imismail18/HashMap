# HashMap Implementation in Python

A custom hash map data structure implementation featuring collision resolution through chaining. This project demonstrates fundamental hash table concepts with core operations optimized for average O(1) time complexity.

## Features

- **Insert/Update**: Add or update key-value pairs with O(1) average time complexity
- **Retrieve**: Fast key lookup with O(1) average performance
- **Remove**: Delete entries efficiently with O(1) average time complexity
- **Iteration**: Access all keys, values, or key-value pairs
- **Searching**: Search for single or multiple keys simultaneously
- **Collision Handling**: Chaining-based collision resolution for robust performance

## Installation

Simply copy the `hashmap.py` file to your project:

```bash
git clone <repository-url>
cd Hashmap
```

## Quick Start

```python
from hashmap import HashMap

# Create a HashMap with capacity of 10
hmap = HashMap(capacity=10)

# Add key-value pairs
hmap.put("name", "Alice")
hmap.put("age", 25)
hmap.put("city", "New York")

# Retrieve values
print(hmap.get("name"))  # Output: Alice
print(hmap.get("age"))   # Output: 25

# Check if key exists
print("name" in hmap)  # Output: True

# Remove a key
hmap.remove("city")

# Get all keys, values, or items
print(hmap.keys())    # Output: ['name', 'age']
print(hmap.values())  # Output: ['Alice', 25]
print(hmap.items())   # Output: [('name', 'Alice'), ('age', 25)]

# Search for multiple keys
results = hmap.search("name", "age", "city")
print(results)  # Output: {'name': True, 'age': True, 'city': False}

# Get the size
print(len(hmap))  # Output: 2
```

## API Reference

### Constructor

```python
HashMap(capacity: int)
```
Initializes an empty hash map with specified capacity. **Time Complexity: O(capacity)**

### Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `put(key, value)` | Insert or update a key-value pair | O(1) avg, O(n) worst |
| `get(key)` | Retrieve value by key; raises KeyError if not found | O(1) avg, O(n) worst |
| `remove(key)` | Remove a key-value pair; raises KeyError if not found | O(1) avg, O(n) worst |
| `__contains__(key)` | Check if key exists (using `in` operator) | O(1) avg, O(n) worst |
| `keys()` | Return list of all keys | O(n) |
| `values()` | Return list of all values | O(n) |
| `items()` | Return list of all key-value pairs | O(n) |
| `search(*keys)` | Search for one or multiple keys | O(n) |
| `__len__()` | Get number of key-value pairs | O(1) |
| `__repr__()` | String representation of the hash map | O(n) |

## Time Complexity Analysis

### Average Case (Balanced Hash Distribution)
- **Insert**: O(1)
- **Lookup**: O(1)
- **Delete**: O(1)

### Worst Case (Hash Collisions)
- **Insert**: O(n) - where n is bucket size
- **Lookup**: O(n) - where n is bucket size
- **Delete**: O(n) - where n is bucket size

### Other Operations
- **Keys/Values/Items**: O(n) - where n is total number of entries
- **Search**: O(n) - where n is number of keys to search

## Hash Function

The implementation uses a polynomial rolling hash function:
```
hash(key) = ((hash * 31) + ord(character)) % capacity
```

This ensures efficient distribution of keys across buckets while maintaining simplicity.

## Implementation Details

- **Collision Resolution**: Chaining (each bucket is a list of key-value tuples)
- **Load Factor**: No automatic resizing; choose appropriate initial capacity
- **Key Types**: Any hashable type (strings, numbers, etc. via conversion to string)

## Example Use Cases

```python
# Caching system
cache = HashMap(capacity=100)
cache.put("user_1", {"name": "Alice", "email": "alice@example.com"})

# Frequency counter
counter = HashMap(capacity=26)
for char in "hello":
    if char in counter:
        counter.put(char, counter.get(char) + 1)
    else:
        counter.put(char, 1)

# Mapping data
mappings = HashMap(capacity=50)
mappings.put("USA", "Washington DC")
mappings.put("France", "Paris")
mappings.put("Japan", "Tokyo")
```
## Project Structure

```text
📂 Hashmap/
├── 📄 hashmap.py
├── 📄 README.md
```

## Contributing

Feel free to fork this repository and submit pull requests for improvements or optimizations.

**Note**: This is an educational implementation. For production use, consider Python's built-in `dict` which is highly optimized and production-ready.

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)
Created as a learning project to understand hash table fundamentals and data structure design.

## License

MIT License

Copyright (c) 2026 Ismail

Created as a learning project to understand hash table fundamentals and data structure design.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



---

