def stringify_numbers(obj: dict) -> dict:
    for k, v in obj.items():
        if type(v) is dict:
            obj[k] = stringify_numbers(v)
        elif type(v) is int:
            obj[k] = str(v)
    return obj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringify_numbers(obj))