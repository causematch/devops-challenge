DevOps Coding Challenge
==========================

This repository contains a simple REST api, implemented in Python.
The API documentation is available at ``/openapi.json``, you can interact
with it at ``/docs``.

Your assignment is to deploy it to AWS or GCP.  Make whatever changes or
additions to the repo are needed and include instructions for using your work.

You will need a cloud account.  You can create one or use one you have already.
You should be able to use only free-tier resources for this assignment.


Requirements
--------------

* Use any AWS or GCP services you like.  Be prepared to explain
  your decisions.  (We prefer cheap and scalable, but please use criteria
  that make most sense to you).

  Note the API uses in-memory storage but long-term persistence is not required.

* Provide a mechanism for deploying new versions of the code, and the
  credentials needed to do this.  If you have other resources in the
  account, make sure we can only access what is related to this assignment.

* Provide a mechanism for deploying the api to a different account

* Automate as much as possible

* Document every step

* Make it easy

* You may use any tools you deem necessary, but be sure to provide
  instructions for installing them on the latest debian linux or
  derivative distro.

* If you write your own scripts, please write them in bash, python, or rust.
  Everything should work on a linux machine.


Extra Credit
-------------

If you have time, you may do more.  Here are some ideas for additional work
to get your creative juices flowing.  Use your own judgement and do what
you think would provide the most value.

* Make the api logs easily accessible.

* Provide a way to determine what git revision is deployed and when it was deployed.

* Securely expose USERNAME and PASSWORD environment variables to the api,
  which will cause it to require basic auth.  Send us the credentials.

* Make it work on both AWS and GCP.
