#!/usr/bin/python3
__author__ = 'eayin'
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys

# Reading the configuration from config.conf
conf_path = "/etc/gymail.conf"
conf = {}
try:
    with open(conf_path) as f:
        code = compile(f.read(), conf_path, 'exec')
        exec(code, conf)
except Exception as err:
    print(err)
    print("* * * * * * * * *\n %s is missing.\n" % conf_path)
    sys.exit(0)
# Functions
def send_mail(event, subject, message):
    msg = MIMEMultipart('alternative')
    # Create message container; the correct MIME type is multipart/alternative.
    msg['From'] = conf["me"]
    msg['To'] = conf["you"]
    error_style = """<style type="text/css">body { background-color:red;} p { color:black; font-size:28px;}</style>"""
    warning_style = """<style type="text/css">body { background-color:yellow;} p { color:black; font-size:28px;}</style>"""
    info_style = """<style type="text/css">body { background-color:green;} p { color:black; font-size:28px;}</style>"""
    template = "<html>%s<body><p>%s</p></body></html>" # Alternatively to %s there is markupsafe or string.format().
    if event == "error":
        html = template % (error_style, message)
        msg['Subject'] = "error: " + subject
    elif event == "warning":
        html = template % (warning_style, message)
        msg['Subject'] = "warning: " + subject
    elif event == "info":
        html = template % (info_style, message)
        msg['Subject'] = "info: " + subject
    part1 = MIMEText(message, 'plain')
    part2 = MIMEText(html, 'html') # Thunderbird is always html, just in the source you can see the plain message
    msg.attach(part1)
    msg.attach(part2)
    s = smtplib.SMTP('smtp.gmail.com:587') # Send the message via local SMTP server.
    s.starttls()
    s.login(conf["username"], conf["password"])
    s.sendmail(conf["me"], conf["you"], msg.as_string())
    s.quit()

parser = argparse.ArgumentParser(description='Simple sendmail script.')
parser.add_argument('-e','--event', choices=['error', 'warning', 'info'], help='Formats html style for email accordingly.', required=True)
parser.add_argument('-s','--subject', help='Subject of email.', required=True)
parser.add_argument('-m','--msg', help='Email message goes here.', required=True)
args = parser.parse_args()
send_mail(args.event, args.subject, args.msg)

