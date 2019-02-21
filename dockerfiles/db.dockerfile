
# base image
FROM mysql:latest

# Add a database
ENV MYSQL_DATABASE HHNAPP
# Add root password
ENV MYSQL_ROOT_PASSWORD p@ssw0rd

# Add a user
ENV MYSQL_USER HHNAPP
# Add the password
ENV MYSQL_PASSWORD password

RUN mysql_ssl_rsa_setup