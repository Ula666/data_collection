## Data collections in Python:

- Lists and Tuples
- Dictionaries
- Sets
 ### dict{}, List [], Tuples()
### What is a list?
- Commonly used to store the data
- Lists are MUTABLE
- syntax [ ] used to create a list
example:
- ` shopping_list = ["bread", "chocolate", "avocados", "milk"]`
- `print(shopping_list[1])`

### To change a value in a list
- `shopping_list[0] = "orange"`
- `print(shopping_list)`

### To add a new value to a list
- `shopping_list.insert(1, "ice cream")`
- `shopping_list.append("apple")`


### To remove a value from a list
- `shopping_list.remove("orange")`

### pop() deletes the last item from the list
- `shopping_list.pop()`


##Tuples:
- are the same as lists but they are IMMUTBLE, cannot be changed
- syntax: tuples`()`
- `essential = ("paracetamol", "tooth paste", "tea")`

# Dictionaries
- Dictionaries - use key valued pairs to save the data
- data can be retrieved by it's value or the key
- syntax `{}`
- ```dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lessons": 3,
    "completed_lessons_name": ["variables", "data types", "collections"]
    }


### To retrieve a value, we use a key
`print(dev_ops_student["name"])`

### To get item from a dictionary in a list
- `print(dev_ops_student["completed_lessons_name"][1])`

- Add "Operators" in completed lesson name
`dev_ops_student["completed_lessons_name"].append("Operators")`
- Change the completed lesson from 3 to 4
`dev_ops_student["completed_lessons"] = 4`
- Remove the "data types" from completed lessons name
`dev_ops_student["completed_lessons_name"]. remove("data types")`
  

