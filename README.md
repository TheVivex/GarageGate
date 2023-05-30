
# GarageGate

A script that allows you to read car license plates from photos and search for them in the database.




## Configuration
To run this script, fill in your mysql credentials in the data_search.py file

```python
...
mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database=""
                )
...
```


## Requirements
This project uses these libraries:
- [MySQL connector](https://pypi.org/project/mysql-connector-python/)
- [OpenCV](https://opencv.org/)
- [Imutils](https://github.com/PyImageSearch/imutils)
- [Python Tesseract](https://github.com/madmaze/pytesseract)

## Authors

- [@TheVivex](https://www.github.com/thevivex)

