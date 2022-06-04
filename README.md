# Spam Filter
## Description
The main program is _filter.py_. It classifies whereas an email is spam or not


Folders _1_ and _2_ contain testing data(emails). There is _!text.txt_ file inside these folders which contain classification(spam or not spam) of each email.

To use this program you can add the following piece of code to the _filter.py_:
```python
if __name__ == '__main__':
    c = MyFilter()
    c.train("1")
    c.test("2")
```

In this case we training by using data of the folder 1 and then test(make prediction) emails of the folder 2. To improve accuracy of prediction you can train more data.
