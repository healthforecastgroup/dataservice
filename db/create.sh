# #ubuntu update (optional )
# sudo apt-get update && sudo apt-get upgrade
# install posgres #should do 9.4 just be cause it has json support, but cant get ubuntu to install 9.4
sudo apt-get install postgresql-9.3
sudo su
su - postgres
sudo -u postgres psql
# ALTER USER postgres PASSWORD '1234';
sudo -u postgres createdb hfgdb
sudo apt-get install pgadmin3
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
pip install psycopg2
pip install sqlalchemy