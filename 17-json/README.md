# JSON module basics

Using the python built-in json module and teh requests library

Add requests dependency

``` bash
uv add requests
```

Using json.loads to read the json from the url response

```python
    response = request.get(url)
    response_json = json.loads(response.text)
```

Using json.dump to serialize a python object or dict into json format

```python
data = {
    'name': 'John'
        {
            'id': 2323,
            'gender': 'male'
        },

    'name': 'Lisa'        
        {
            'id': 1323,
            'gender': 'female'
        },
}
```

Write json with context manager

``` python
    with open(data.json, 'w') as file:
        json.dump(data, file, indent = 4 )
```

In bash command you can use python's `json.tool <filename>` to validate the json file

```bash
    py -m json.tool data.json
```