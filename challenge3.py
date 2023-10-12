# We have a nested object. We would like a function where you pass in the object and a key and get back the value.

def get_nested_obj_value(obj, key):
    if isinstance(key, str):
        key = key.split('/')
    if len(key) == 1:
        return obj.get(key[0])
    
    return get_nested_obj_value(obj.get(key[0]), '/'.join(key[1:]))

object = {"a":{"b":{"c":{"d":"e"}}}}
key = "a/b/c/d"
print(get_nested_obj_value(object, key)) 

object = {"x":{"y":{"z":"a"}}}
key = "x/y/z"
print(get_nested_obj_value(object, key))
