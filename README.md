# YSoft app
Solution of assignment for internship in YSoft

## Create Python 3 application

Application accepts following parameters on command line
* user name – string
* printer name – string
* path to input file with data
* path to output file in JSON format

If incorrect number or wrong parameters are provided, application should display some kind of help

Application should read data from input file and store result in output JSON file in following way
* userName: value presented as the first parameter
* printerName: value presented as the second parameter
* data: content from the input file

Application should be covered by unit tests

Application will print on stdout sum of letters (lower case ascii) stored in the input file
  e.g. if file contains text: ysoftprintmanagement
  the application should display:
  * a: 3
  * e: 2
  * i: 1
....

Non-ascii characters are not considered
