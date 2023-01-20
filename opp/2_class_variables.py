class HtmlDoc:
    __extension = 'html'
    version = 5

print(HtmlDoc.__name__)

# get the value of a class variable
print(HtmlDoc._HtmlDoc__extension)
print(getattr(HtmlDoc, '_HtmlDoc__extension'))
# print(HtmlDoc.anything_else) # generate and exception

# set the value of a class variable
HtmlDoc.version = 5.5
print(getattr(HtmlDoc, 'version'))
setattr(HtmlDoc, 'version', 10)
print(getattr(HtmlDoc, 'version'))

# get all class variables
print(HtmlDoc.__dict__) # return a dict of class variables


