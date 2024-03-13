def nestedevensum(obj: dict) -> int:
    s = 0
    for i in obj.values():
        if type(i) is dict:
            s += nestedevensum(i)
        elif type(i) == int and i % 2 == 0:
            s += i
    return s

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

print(nestedevensum(obj1)) # 6
print(nestedevensum(obj2)) # 10