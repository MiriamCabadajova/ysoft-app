# YSoft app
Solution of assignment for internship in YSoft

# Create Python 3 application:

application accepts following parameters on command line
* user name – string
* printer name – string
* path to input file with data
* path to output file in JSON format
if incorrect number or wrong parameters are provided, application should display some kind of help
application should read data from input file and store result in output JSON file in following way
userName: value presented as the first parameter
printerName: value presented as the second parameter
data: content from the input file
application should be covered by unit tests
application will print on stdout sum of letters (lower case ascii) stored in the input file
e.g. if file contains text: ysoftprintmanagement
the application should display:
a: 3
e: 2
i: 1
....
non-ascii characters are not considered
package the application using pyinstaller
send us both package and the source code
bonus points: store the source code at Github, just make sure, that there are no binary files (e.g. pyc), by using proper .gitignore
