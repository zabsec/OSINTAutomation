#!/bin/bash


echo -e "${RED} installing dependencies..."
apt install sherlock
git clone https://github.com/twintproject/twint
cd twint
pip3 install . -r requirements.txt
pip3 install aiohttp==3.7.0
sudo python3 setup.py install
cd ..
curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash
sudo mv ./phoneinfoga /usr/bin/phoneinfoga
chmod +x PersonalOSINT.py
echo -e "${RED} dependencies successfully installed. You can now run PersonalOSINT.py"



