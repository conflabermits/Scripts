# Toolbox Container

A container meant to avoid [some of] the frustration of troubleshooting network and connectivity issues in docker containers deployed to restrictive environments.

## Requirements

* MSSQL and mysql CLI clients
* Net tools (ping, nslookup, dig, etc.)
* Editors (vim, emacs, nano?)
* gzip
* python2 and python3
    * requests module
* ruby 2.x
* Corretto java?
* httpd/apache2
    * Extra credit: include config to run a simple HTML page on demand
* Other tools:
    * screen
    * tree
    * column
    * bc
* Include a README and a DOCS folder with simple instructions for:
    * Accessing MSSQL and mysql databases via CLI
    * Starting and accessing the HTML page on apache
    * Common network troubleshooting commands
* Either or both:
    * Directory used to pull files into the container on build or start
    * Simple volume mount to transfer files in and out of the container easily
* Deployable
