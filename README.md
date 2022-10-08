# ZotLab
A online ICS queue that helps TAs and Lab Tutors maximize tutor effectiveness.

**Unofficial Plan

Oct 4th Tuesday



#### Language

Python (both front-end and back-end)



#### UI, Libraries, and Frameworks

- Webpage
  1. pyWebIO https://github.com/pywebio/PyWebIO/
  2. Django https://github.com/django/django
  3. Flask https://github.com/pallets/flask
- GUI
  1. Tkinter https://docs.python.org/3/library/tkinter.html
- Connection
  1. Socket https://docs.python.org/3/library/socket.html
  2. Netifaces https://github.com/al45tair/netifaces
- Compiler
  1. py2app https://github.com/ronaldoussoren/py2app
  2. Python 3.10+



#### Description

Introducing ZotLab, an online ICS LAB queuing program written primarily in Python. Its function is mainly divided into two parts, namely "queue" and "feedback".

When students need Lab help, they can post a request through the website and fill in their location in the classroom (which seat). Students will be placed in a queuing system that will notify them of their position in the queue and estimated time to receive assistance.

Regarding the feedback system, students can grade and give feedback to the tutoring TA or lab tutor in anonymous. The whole process follows *ratemyprofessors.com*. The goal of the system is to help the tutor reflect on himself and do better in the weekly journal.

The entire program will store data and provide services on a server deployed in the cloud, and user interaction will be mainly performed on web pages.

The main purpose of developing Zot Lab is to help Lab Tutor arrange their session more efficiently, avoiding the traditional way for students to raise their hands or write their names on the whiteboard (there is a great chance that tutor cannot identify people by name in most cases). This also solves social phobias and helps more students to make good use of the lab time. Tutors and TAs also get valuable feedback and stats.
