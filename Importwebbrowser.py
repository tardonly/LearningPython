import webbrowser
a = input("Enter the first number")
b = input("Enter the second one")
url = 'http://www.python.org/'

if a + b == 4:
    webbrowser.open(url)
else:
    print "Try to make the sum to 4!"
