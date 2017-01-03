
# set up virtual venv (optional)
## install virtualvenv
sudo apt-get install python-pip
sudo pip install virtualenv
## create and activate virtualvenv for the hfg project
mkdir hfg
cd hfg
virtualenv venv
source venv/bin/activate
## install mongodb community
## https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
sudo apt-get install -y mongodb-org

## install  eve
## http://python-eve.org/quickstart.html#quickstart
cd hfg
git clone http://github.com/nicolaiarocci/eve.git eve
cd eve
python setup.py install

# get robomongo for admin ui for viewing mongodb
http://askubuntu.com/questions/739297/how-to-install-robomongo-ubuntu-system-please-let-me-know/781793

## install 