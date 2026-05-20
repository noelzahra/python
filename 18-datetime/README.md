## Datetime library

Using datetime.strptime() to get the date object from a string. Format the dat to European standard with .strftime()

```python
 log_date = datetime.strptime(daybatch[item], '%m/%d/%Y%I:%M:%S %p')
 ```
 ```python
 log_date_formatted = log_date.strftime('%d-%m-%Y %H:%M:%S %p') 
```