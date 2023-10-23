def get_nested_value(obj, key_path):
    keys = key_path.split('/')
    print(f"Keys are :{keys}")
    for key in keys:
        if isinstance(obj, dict) and key in obj:
            print(f"Key {key} Iteration - Object Value : {obj}")
            obj = obj[key]
            print(f"Key is : {key}, Obj is : {obj}")
        else:
            return None
    return obj

# Test cases
object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
value1 = get_nested_value(object1, key1)
# Output would be 'd'
print(f"The result is : {value1}")  

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
value2 = get_nested_value(object2, key2)
# Output would be 'a'
print(f"The result is : {value2}")  