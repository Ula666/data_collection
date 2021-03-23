# Dictionaries - use key valued pairs to save the data
# data can be retrieved by it's value or the key
# syntax: {}
# dict{}, List [], Tuples()

dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lessons": 3,
    "completed_lessons_name": ["variables", "data types", "collections"]
}
# print(dev_ops_student)
# # confirm the type
# print(type(dev_ops_student))
# to retrieve a value, we use a key
# print(dev_ops_student["name"])
# print(dev_ops_student["completed_lessons"])
# # to get item from a dictionary in a list
# print(dev_ops_student["completed_lessons_name"][1])
#
# print(dev_ops_student.keys())
# print(dev_ops_student.values())

# add " operators" in completed lesson name
dev_ops_student["completed_lessons_name"].append("Operators")
# to change the completed lesson from 3 to 4
dev_ops_student["completed_lessons"] = 4
# remove the data types from completed lessons name
dev_ops_student["completed_lessons_name"]. remove("data types")

print(dev_ops_student)


# Sets


