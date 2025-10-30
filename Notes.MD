########## Head First Python (3rd Edition) ##########
Chapter 0:
-------------------------------------------------------
Install the latest Python: https://www.python.org/downloads/
pip install --upgrade pip
Install Jupiter in VSC: 
python3 -m pip install jupyter
Install the latest release of VS Code: https://code.visualstudio.com/Download
Add 2 required extensions to VS Code: Python & Jupyter

REPL stands for “read-eval-print(Evaluated)-print-loop”. Jupyter is a REPL
	A Jupyter REPL is called a notebook.
	ipynb = interactive python notebook

= assignment operator
== comparision operator also >, <, >=, <=, !=

Python ships with a rich standard library
	The Python Standard Library (PSL) is the name used to refer to a large
	collection of Python functions, types, modules, classes, and packages
	bundled with Python. These are guaranteed to be there once Python is installed.

“BIF” is shorthand for “builtin function”.

dir = Attributes

The Big 4: list, tuple, dictionary, and set
[list]: Mutable, ordered, indexed, sequence, heterogeneous, dynamic [1, 'a', 2.0]
(tuple): Immutable, ordered, indexed, sequence, heterogeneous, dynamic (1, 'a', 2.0)
{set}: Mutable, unordered, unindexed, collection, unique, dynamic {1, 'a', 2.0}
{dict}: Mutable, ordered, indexed, key-value pairs, unique keys, dynamic {'key': 'value'}

“dynamic typing”, in that the type your variable refers to is bound at run-time, 
	not compile-time.

PyPI (and pronounced “pie-pea-eye”) - Python Package Index		

Python code is easy to read & run.
Python encourages experimentation and learning via its REPL.
Python includes the Python Standard Library (PSL).
The PSL provides practical, powerful, and generic built-in functions (BIFs).
The PSL has “The Big 4” data structures: lists, tuples, dictionaries, and sets.
Python has powerful built-in operators (like “in”).
maintain, nor test!
Python has the Python Package Index (PyPI).
Python is fun!

Notebook key combinations:
Shift+Enter Execute the current code cell, then move the focus to the 
	next cell (creating a new empty cell when at the bottom of the notebook).
Ctrl+Enter Execute the current code cell, but don’t move the focus.
Alt+Enter Execute the current code cell, then insert a new
	empty cell below the executed one. Move the focus to the new cell.

Notebook key sequences:
Esc then A Insert a new empty cell above the current cell.
	Move the focus to the new cell.
Esc then B Insert a new empty cell below the current
Esc then C Take a copy of the cell which currently has the focus.
Esc then V Paste a previously copied (or cut) cell below the currently focused cell.
Esc then X Cut the currently focused cell from the notebook.
Z Undo the last cut (there’s no need to press the ESC key here).

default variable: a single underscore character
booleans: True, False

Chapter 1: Diving in: Hit the Ground Running!
-------------------------------------------------------
Darius.ipynb
Obj in Memory: Value:Methods
fn = "Darius-13-100m-Fly.txt" #str
Variable, ID [123456] = Object, ID [123456] - Reference

Dunder = double underscores

dot operator: allows you to access the methods and attributes of an object
	Vs BIF. len(fn)
	
split(sep=None, maxsplit=-1)

Python refers to its error messages by the name traceback

Strings in Python are immutable (they cannot mutate or change once they exist).

Multiple assignment (aka unpacking), instead of parts: 
	swimmer, age, distance, stroke = fn.removesuffix('.txt').split('-')

Read error messages bottom up
removesuffix and split is a powerful combination.

Chapter 2: List of Numbers: Processing List Data 
-------------------------------------------------------
with open

Filename and Folder are referred in Block Letters

FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"

with open(FOLDER+FN) as df:
    data = df.readlines()

> The with statement is used to manage the context within which its block of code runs. Automatically arranges to close a file when you’re done with it.
readlines

indentation - A tab or four spaces.

The colon (:) indicates a code block is about to begin.

data[0].strip().split(',')

int('1') - Convert str to int
converted_time = int(minutes)*60*100 + int(seconds)*100 + int(hundredths)	

Loops
for t in times:
	print(t)
for i in range(5):
    print(i)

while True:
    print("True")

i: int = 0
while i < 5:
    print(i)
    i += 1

the while loop in Python is used much less than an equivalent for.
while not False:
    print("True")

converts = [] #empty list
everything in Python is an object

append() add an element to the end of the list

import statistics #PSL
round BIF gets rid of unwanted decimal places
str BIF converts its argument to a string.

Chapter 3: List of files
-------------------------------------------------------
Functions - reuse code
	The def keyword defines a new, bespoke function.
	The return statement allows a bespoke function to return a result.
	A named chunk of code
Modules - USe it share code
	"module.function" Ex: swimclub.read_swim_data
	When you put code in it’s o wn file (with a .py extension), you create a module.
	The import statements lets you reuse a module, e.g., import swimclub
Files - Store data
	The os module (included as part of the PSL) lets your Python code talk to your underlying operating system.
	os.listdir(swimclub.FOLDER)
	
in operator
	It’s great at searching (aka checking for membership).
	
if ":" in t: #1:30.96 vs 43.35
True or False

if:
elif:
else:

Append - Add an element to the end of the list
Remove - Remove an element from the list

ListDir - List of files in a directory
Enumerate - BIF that provides numbers on iteration.

""" """ #docstring - to comment a whole block of code

If a function tries to return more than one result, the collection of returned values are bundled together as a single tuple (immutable sequence).

os module (included as part of the PSL) lets your Python code talk to your underlying operating system
sort vs sorted

enumerate. It can be used to number the iterations of any for loop.

Chapter 4: Make Charts from Data
-------------------------------------------------------

f-strings - format specifier
average = str(minutes) + ":" + str(seconds) + "." + hundredths
vs
average = f"{minutes}:{seconds}.{hundredths}"
print ("Name:" +name,", Age:" +str(age))
print (f"Name:{name}, Age:{age}")

#determines whether a script is being run directly or imported as a module into another script.
Practice.py >>
    print("First Module s Name: {}".format(__name__))
    >>First Module s Name: __main__
Test.py >>
    import Practice
    print("Second Module's Name: {}".format(__name__))
    >>First Module s Name: Practice
    >>Second Module's Name: __main__

hfpy_utils: The hfpy_utils module provides a conversion function that can convert a value from one range into a value in another range. Called (in a feat of unknowable imagination) convert2range, this function was used to ensure the width of the bars on the Coach’s chart didn’t end

The reverse method (which comes built into every Python list) swaps the order of a named list in-place, and saved us from the embarrassment of showing the Coach a swimmer’s chart with an incorrect bar order

SVG = scalable vector graphics

Chapter 5: Getting Organized
-------------------------------------------------------
Data Structure Choices

 list-set-list trick: it’s just that you used a function chain to call a set on a list, then you called a list again on the set. 
 When it comes to performing lookups, there can be only one data structure of choice, and that’s Python’s dictionary {Key: Value}. keys must be unique

enumurate adds a counter to an iterable and returns an enumerate object. This object can then be used in a for loop to conveniently access both the index (or count) and the corresponding item from the iterable. 

pprint - Pretty Print

Chapter 6: Building a webapp
-------------------------------------------------------
Flask: takes advantage of Python’s decorator feature, which uses the @ symbol to mark a function for special treatment. In Flask, the @app decorator lets you associate an incoming URL with any Python function.
Out of the box, the @app decorator supports the GET and POST methods of HTTP.
Flask’s render_template does all the heavy lifting when hooking into Jinja2’s template mechanism.

pip: the Package Installer for Python.
When you see the “@” symbol used in this way, you are looking at a Python decorator
Debugger

Chapter 7: Run your code Anywhere
-------------------------------------------------------

Add a stylesheet to your webapp to add a splash of color. And be sure to put your stylesheet in the static folder.
◾
Remember: any changes made to your base HTML template are applied to all of the templates which inherit from base.
◾
If your code generates HTML without reference to the base template, any CSS applied in the base (or anything else, for that matter) is not shared.
◾
It’s possible to put any arbitrary Python code between the {{ and }} tags within a Jinja template. Just be careful not to use too complex an expression.
◾
As in previous chapters, the use of the removesuffix and split string methods lets you chain methods together to get lots of work done with a small amount of code.
◾
Deploying your webapp to the cloud is possible with many different online services, but our favorite remains PythonAnywhere.
◾
Your locally running Flask code can (more times than not) be deployed on PythonAnywhere with next to no code changes.
◾
WSGI stands for Web Server Gateway Interface, and is a standard specification for embedding Python code within a web browser. Flask ships with a small WSGI-compliant test web server that exists to let you test your webapp locally on your own computer. PythonAnywhere supports WSGI, too, as do all the other big players in the web-hosting ecosystem.

Chapter 8: Working with HTML (Web Scraping)
-------------------------------------------------------
slices: 0,1,2,3,4,5.....-3,-2,-1
nums = [0,1,2,3,4,5,6,7,8,9]
nums = nums[:]
nums[:4] #[0,1,2,3]
nums[-1] #9
nums[-2] #8
nums[2:4] #[2, 3] - Start at the first number, stop before the second
nums[7:-1]
nums[::2] #[0, 2, 4, 6, 8] slices every second value from the sequence
nums[::3] #[0, 3, 6, 9] slices every third value from the sequence
nums[::-1] #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0] returned in reversed order

import gazpacho
    html = gazpacho.get(URL)
    soup = gazpacho.Soup(html)
    tables = soup.find("table")


Chapter 9: Working with data (Data Manipulation)
-------------------------------------------------------

All of Python’s four built-in data structures—list, dictionary, tuple, and set—are great on their own, but they really shine when used together or nested within themselves. In this chapter a classic arrangement, the dictionary of dictionaries, demonstrated how to build out and use a hierarchical data structure.

Another classic use case was demonstrated when a dictionary provided a small lookup table, making conversions from one value to another a snap.

The open BIF, used in earlier chapters to read data from files, became a data structure writing machine thanks to its write mode (“w”). You used this BIF when you wrote code to save your dictionary-of-dictionaries as JSON.

They may not have had a starring role in this chapter, but f-strings, when they did appear, stole the show.

You learned how to create a small utility program, which you then executed outside of VS Code and its Jupyter Notebook environment. You even arranged for your utility to execute on a daily basis on PythonAnywhere.

Chapter 9.5: working with elephants dataframes (Tabular Data)
-------------------------------------------------------
PyPI
pandas - import pandas as pd, pd.read_html(URL)
tables[0].head() #[0] - first dataframe, #head() - display only the first 5 rows, instead of entire DF

df = dataframe
df = tables[0][["Event","Time"]]
df.head()
df.to_dict()
df.tail() #display the last 5 rows
df[df["Event"].str.contains("relay")] #A pandas conditional expression can be used to select rows. In this next cell, the data in the Event column is converted to a string, which is then searched for “relay” using the contains function
~ #list the records which do not have the word
df[~df["Event"].str.contains("relay")]

If all you need to do is quickly extract
data from HTML tables, it’s hard to beat
pandas. If you need to access data from
elsewhere in a HTML page, we think
gazpacho is a great choice. But, as stated,
it’s OK to mix’n’match.

pandas is the leading data analysis tool used by Python programmers. It’s used everywhere.
◾
pandas provides excellent support for arranging your data in tabular form: data is arranged in row/column format. The name given to this tabular form in pandas is dataframe.
◾
The import pandas as pd line of code may well be one of the most used within the Python data science space, and is right up their with import numpy as np. The as keyword allows you to specify a shorthand alias for a name in Python.
◾
The read_html function (which is part of pandas) grabs, reads, then converts any HTML page into a list of tables, with each slot containing a dataframe. It’s a pretty cool function (assumming all you need to do is scrape <table> data).
◾
The head function, lets you view the first five rows of data in any dataframe.
◾
The to_dict function (the real star of the show in this chapter) converts the data in a dataframe to a Python dictionary.
◾
If the default conversion isn’t what you want, you can adjust the behavior of to_dict by passing in parameters. The "records" parameter almost did the trick in this chapter (but not quite).
◾
Each pandas dataframe supports the set_index function which lets you reshape your dataframe.
◾
Although web scraping code written with pandas is generally fewer lines of code than the equivalent written with gazpacho, it does not necessarily follow that the pandas code is “better.”

Chapter 10: Databases (Getting Organized)
-------------------------------------------------------
SQLite: It comes with Python
DB4S - GUI
https://www.sqlite.org/mostdeployed.html
https://docs.python.org/3/library/sqlite3.html

%pip install DBcm --upgrade
import DBcm
db_details = "CoachDB.sqlite3"

SQL = """
    select time()
""" #The query is shown within a triple-quoted string, and assigned to a variable called “SQL”.

with DBcm.UseDatabase(db_details) as db:
    db.execute(SQL) #The “SQL” variable is passed to the “execute” function
    results = db.fetchall() #or fetchone, fetchmany
results
#The “fetchall” method always returns a list of tuples, even when the SQL is asking—as in this case—for a *single* value.

 db.execute(SQL)

SQL = """select * from swimmers"""
with DBcm.UseDatabase(db_details) as db:
    db.execute(SQL)
    results = db.fetchall()
results

When it comes to managing the data associated with your applications, not much beats a database.
◾
When you install Python, you get SQLite for free.
◾
SQLite is a single-process, file-based, database management engine that requires very little admin to run. All of your interactions with the engine can be executed from within Python code. This makes using SQLite an excellent choice when starting out, as you can experiment with ease.
◾
When used with with, DBcm lets you connect to an underlying database engine (either SQLite or MySQL/MariaDB), then execute an arbitrary number of SQL queries/statements. When the code block associated with your with statement ends, a “commit” is sent to the engine, and your database connection is automatically closed.
◾
If you use a filename with DBcm’s UseDatabase class, SQLite is used. As you’ll learn in a later chapter, a dictionary of credential information can also be provided to UseDatabase, allowing you to use DBcm with an existing MySQL/MariaDB installation.
◾
The Python DB-API provides a number of methods for interacting with your chosen database engine, including execute, fetchall, fetchmany, and fetchone.
◾
The execute method sends an SQL query/statement to your chosen database engine.
◾
The fetchall method returns results as a list of tuples (when at least one row is returned) or an empty list (when no results are returned from your database engine).
◾
The fetchmany method operates like fetchall, but for the fact that you can specify a maximum number of rows to return. Repeated calls to fetchmany allows you to implement pagination (should you need it).
◾
The fetchone method returns one, and only one, tuple of results from your database engine. Like with fetchall and fetchmany, the results can be empty.
◾
Depending on the database engine you’re using, you may be able to request additional information about the database and the tables you are working with. For example, SQLite provides the pragma table_list and pragma table_info commands, whereas MySQL/MariaDB provide the equivalent show tables and describe commands.
◾
Despite SQL being a very established database technology, each database engine implements its own dialect. This can make life interesting…
◾
When using SQL queries/statements in your Python code, the recommendation is to put them within multiline triple-quoted strings. Of course, this is only a recommendation, so you don’t have to do this. However, other coders reading your code may well thank you when you do (and, remember, that “other programmer” may be you in six months’ time).
◾
Python database engines support the notion of parameterized queries/statements. The use of placeholders can protect your code from all manner of SQL Injection Attacks, and the use of placeholders is strongly encouraged. Using f-strings to achieve the same effect (i.e., parameterized queries/statements) might lead to a world of pain… just don’t try and say we didn’t warn you.
◾
Most placeholder technologies expect data to be passed into SQL queries using a tuple, even when there’s only one parameter. This can lead to weird looking tuples. Remember (42,), which looks weird, but works.
◾
When executing multiple SQL queries/statements against your database (perhaps within a tight loop), it’s better to place your loop within a database-connecting with statement than to constantly connect/execute/disconnect to your database within a tight loop. Your database engine (and, by extension, your database sys-admins) will thank you when you do.
◾
When using SQL, the SELECT statement lets your read data, the INSERT statement lets you add data, and the DELETE statement removes data from a table. There’s also an UPDATE statement that can change data (but you’ve yet to need to perform any changes, so UPDATE has yet to make an appearance in this book).

Chapter 11: List Comprehensions (Databases Integrations)
-------------------------------------------------------

 SQL = """SELECT tax_percent_str FROM Tax WHERE province = ?"""
 #? = the query expects to receive a date value
“*” is shorthand for “everything” and, when used in this context, imports all the names defined in the named module to the current namespace. Using

!py -3 #That exclamation mark (!) tells Jupyter to run the command at your operating system prompt.

This chapter was chock-full of code that integrated the data in your database engine with the Coach’s webapp.
◾
Despite all of your database integration code, there are only two takeaways from all of this chapter’s material we really want you to remember, and it’s these two words: list and comprehension.
◾
A list comprehension lets you rewrite a multiline for loop as a single line. Not only is the resulting single line of code less code (duh!), it’s also faster than its multiline equivalent, and list comprehensions can appear almost anywhere in your code (unlike the multiline loop equivalent). This makes list comprehensions very, very cool.
◾
Python programmers the world over love list comprehensions. Consequently, you’ll come across them being used in lots of places in other programmer’s code.
◾
It is possible to create set and dictionary comprehensions, too, but you did not need them in this chapter, so they did not feature. However, if you understand how a list comprehension works, you’ll have no problem applying what you know to set and dictionary comprehensions.
◾
There’s no such thing as a tuple comprehension (so don’t even go there).
◾
Comprehensions are typically one of two types: transformational and filtering.
◾
Transformational comprehensions (also called mappings) convert the values in one list to a new list of converted values.
◾
Filtering comprehensions are easy to spot: they have an if condition that must hold in order for a value to be appended to a target list.
◾
It’s perfectly acceptable to have a compehension that is both transformational and filtering (although we’re not sure what to call a list comprehension that does double-duty like this… mapfilter, maybe?).
◾
Did we mention that Python programmers love list comprehensions?

Chapter 12: deployment revisited (The Finishing Touches)
-------------------------------------------------------
Moving from SQLite to MariaDB is not hard, but you do need to get the details right (recall the autoincrement to auto_increment adjustments, for instance).
◾
Despite SQLite and MariaDB using SQL, their dialects differ in subtle ways. Additionally, placeholders in MariaDB use %s, whereas SQLite uses ?, so care is needed here.
◾
The only other changes to the code revolved around setting the correct database credentials (in the db_details variable). The rest of the code worked with no changes thanks to your use of DBcm.

Symbols
-------------------------------------------------------
+ (concatenation operator) 117, 189, 190
= (assignment operator) 52
:= operator (assignment expression) 607
~ (NOT in pandas) 434
: (colon)
indicating indented code 26
in Python syntax 92
your BFF 92
{} (curly braces)
around data rather than code blocks 2
and dictionaries 239
f-string 190
Jinja2 statements 292
_ (default variable) 15
{{}} (double curly braces, with Jinja2) 330
## (double-hashes for commenting-out code) 583
*_ (ignoring values in tuple) 186
? (question mark), SQL placeholder 475
%s (placeholder for MariaDB) 581, 582
[] (square brackets). See square brackets ([])
* (with import statement) 526

+++++++++++++++++++++++++
#type annotations"
#age: int = 10
#name: str = "Sri"

def calc(a: int, b: int, opr: str) -> int:
    if opr == '+':
        print(f"{a} {opr} {b}")
        return a + b
    elif opr == '-':
        print(f"{a} {opr} {b}")
        return a - b
    elif opr == '*':
        print(f"{a} {opr} {b}")
        return a * b
    elif opr == '/':
        print(f"{a} {opr} {b}")
        return a / b
    else:
        print("Invalid operation"+opr)        

print(calc(1, 2, '-*'))




Error Handling:
try:
    print(1/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
except typeError:
    print("Type Error") 

import Practice
print("Second Module's Name: {}".format(__name__))

import math 
print(math.sqrt(16))    

import math as m
print(m.sqrt(16))    

