FROM toolbox-base:latest

### MYSQL APT INSTALL ##
#ENV DEBIAN_FRONTEND noninteractive
#
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/repo-codename select bionic'
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/repo-distro select ubuntu'
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/repo-url string http://repo.mysql.com/apt/'
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-preview select '
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-product select Ok'
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-server select mysql-5.7'
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-tools select Ok'
##RUN debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/unsupported-platform select abort'
#
#RUN { \
#        echo mysql-apt-config mysql-apt-config/repo-codename select bionic; \
#        echo mysql-apt-config mysql-apt-config/repo-distro select ubuntu; \
#        echo mysql-apt-config mysql-apt-config/repo-url string http://repo.mysql.com/apt; \
#        echo mysql-apt-config mysql-apt-config/select-preview select ''; \
#        echo mysql-apt-config mysql-apt-config/select-product select Ok; \
#        echo mysql-apt-config mysql-apt-config/select-server select mysql-5.7; \
#        echo mysql-apt-config mysql-apt-config/select-tools select Ok; \
#        echo mysql-apt-config mysql-apt-config/unsupported-platform select abort; \
#    } | debconf-set-selections
#
#RUN wget http://dev.mysql.com/get/mysql-apt-config_0.7.2-1_all.deb
#RUN dpkg -i mysql-apt-config_0.7.2-1_all.deb
#RUN apt-get update
#RUN apt-get install -y mysql-community-client

## Step 1: Import the public repository GPG keys
#RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
#
## Step 2: Register the Microsoft Ubuntu repository
#RUN curl -o /etc/apt/sources.list.d/microsoft.list https://packages.microsoft.com/config/ubuntu/18.04/prod.list
#
## Step 3: Update the list of products
#RUN apt-get update
#
## Step 4: Install mssql-cli AND/OR tools+odbc
##RUN apt-get install mssql-cli
#RUN apt-get install mssql-tools unixodbc-dev
## Resources:
### https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017
### https://www.mssqltips.com/sqlservertip/5305/installing-and-using-mssqlcli-on-linux-for-sql-server/
#
## Step 5: Add to path
##RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"'

# OR #
# Get package directly from MS repo:
# https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/mssql-tools/mssql-tools_17.4.1.1-1_amd64.deb
# https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/msodbcsql17/msodbcsql17_17.4.2.1-1_amd64.deb
# sudo dpkg -i msodbcsql_<version>.deb
# sudo dpkg -i mssql-tools_<version>.deb
# sudo apt-get -f install

# Run sqlcmd with parameters for your SQL Server name (-S), the user name (-U), and the password (-P). In this tutorial, you are connecting locally, so the server name is localhost. The user name is SA and the password is the one you provided for the SA account during setup.
# sqlcmd -S localhost -U SA -P '<YourPassword>'
# Mssql-cli -S 'SQL instance' -U 'user id' -P 'password'

