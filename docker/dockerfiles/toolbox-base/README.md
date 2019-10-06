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

## Notes

### Packages

| Package | Provides |
| --- | --- |
| dnsutils | dig, nslookup |
| screen | screen |
| tree | tree |
| bc | bc |
| bsdmainutils | column |
| gzip | gzip, gunzip |
| iputils-ping | ping |
| curl | curl |
| wget | wget |
| gnupg2 | gnupg, gnupg2 |
| vim | vim |
| emacs | emacs |
| nano | nano |
| python | python2.7 |
| apache2 | apache2 |
| java-common, java-1.8.0-amazon-corretto-jdk | java |
| ruby | ruby |
| lsb-release, mysql-community-client | mysql |

### mysql info

The syntax is as follows for both MariaDB and MySQL client:

mysql -u user -p -e 'Your SQL Query Here' database-name

OR

mysql -u USER -p PASSWORD -h MYSQLSERVERNAME -e 'select * from foo...' database-name

Where,

-u : Specify mysql database user name
-p : Prompt for password
-e : Execute sql query
database : Specify database name

https://www.cyberciti.biz/faq/run-sql-query-directly-on-the-command-line/

