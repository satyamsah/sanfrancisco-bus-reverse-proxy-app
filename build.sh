sudo apt-get install -y python3
sudo apt-get install -y python3-venv
python3 -m venv myenvsat
source myenvsat/bin/activate

sudo apt-get install -y python-pip python-dev build-essential 
sudo pip install -y --upgrade pip 
sudo pip install -y --upgrade virtualenv 
pip install -r requirements.txt
sudo chown -R $USER: .
python proxy-net.py
