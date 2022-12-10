# Week 4 Coding problems

### Execute your first API call (Difficulty 4 out of 10)

In VS Code, download an extension called Thunder Client.  Thunder client is an extension that allows you to make API calls and save them.  If you've heard of the software called Postman, Thunder Client essentially does the same thing.

Using Thunder Client, create an API call to an API of your choosing.  A general list of public APIs is available on [Github](https://github.com/public-apis/public-apis)

Choose from one of the available categories and pick a specific API to hit.  

---

### Execute an API call in Python (Difficulty 5 out of 10)

Using Python, execute the same API call within a script.  In order to do this, you'll need to use the `requests` module.  More information on it can be found on [Pypi](https://pypi.org/project/requests/), which is the primary package repository for Python.

You will have to use PIP to install this module.

---

### Execute an API call to Nautobot (Difficulty 7 out of 10)

There is a publicly available Nautobot server out there reachable via [this url](https://demo.nautobot.com).

Use either Thunder Client or Python to execute an API call to this public Nautobot server.  Your API call should return all of the information for the _devices_.

---

### Find each device's respective site name (Difficulty 8 out of 10)

Every device in Nautobot should belong to a specific physical site.  If you did the last exercise correctly, you should have received an HTTP response from the Nautobot API.  

This response has some metadata relating to the HTTP information, but most importantly, it should contain JSON data representing all of the devices in Nautobot's database.

In this exercise, use the JSON data contained within the response to create a data structure (list, dictionary, tuple, etc...) that maps each device to its respective site.  The format of your data structure is totally up to you.