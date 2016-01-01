gymail
======

gymail is a simple python mail notification script with three eligible event types
(error, warning and info), for each a different visual style is applied in the html body.
Use it in cli or as python module.
<br>

## Configuration:
Add your mail provider data to /etc/gymail.conf 

## CLI usage

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

## CLI example:
`gymail.py -e info -s Backup -m "Backup was successful"` <br>

## Module usage:
    from gymail import core
    core.send_mail(event='info', message='example', subject='example')
