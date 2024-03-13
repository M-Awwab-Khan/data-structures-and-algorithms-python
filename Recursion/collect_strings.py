def collect_strings(obj: dict) -> list:
    strs = []
    for k, v in obj.items():
        if type(v) is dict:
            strs.extend(collect_strings(v))
        elif type(v) is str:
            strs.append(v)
    return strs

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collect_strings(obj)) # ['foo', 'bar', 'baz'])