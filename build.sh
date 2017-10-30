sudo apt-get install python3

python3 -m venv ENV
. ENV/bin/activate

sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
pip install -r requirements.txt
sudo chown -R $USER: .
python proxy-net.py


