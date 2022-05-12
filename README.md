# FinalProject_CSDL

# On Ubuntu:

## Install mysql

sudo apt-get clean

sudo apt-get purge mysql*

sudo apt-get update

sudo apt-get install -f

sudo apt-get install mysql-server-5.7

/etc/init.d/mysql start

service mysql start

## Install mongodb

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo service mongod start


=> Check: mongo

pip install pymongo


==> Install redis
pip install redis
