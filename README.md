gymail
======

gymail is a simple python mail notification script.
<br>
#### Usage description

``` 
usage: gymail.py [-h] -e {error,warning,info} -s SUBJECT -m MSG

Simple sendmail script.

optional arguments:
  -h, --help            show this help message and exit
  -e {error,warning,info}, --event {error,warning,info}
                        Formats html style for email accordingly.
  -s SUBJECT, --subject SUBJECT
                        Subject of email.
  -m MSG, --msg MSG     Email message goes here.
  ```
  <br>
  #### Example:
  `gymail.py -e info -s Backup -m "Backup was successful"`
  <br>
  #### Configuration:
  Add your mail provider data to /etc/gymail.conf 
