#!/bin/bash

chsh -s /bin/bash

OLDHOSTNAME=$(hostname)
NEWHOSTNAME=$(sysctl hw.model | awk '{print tolower()}' | sed -e 's/[0-9,]//g' -e 's/macbook/macbook-/')
sudo hostname "${NEWHOSTNAME:-macbook-air}"

cd ~/.ssh && ssh-keygen && cat id_rsa.pub
echo "## ADD PUBLIC KEY TO GITHUB: https://github.com/settings/keys ##"
read -p "When finished, press Enter"

cd ~/ && mkdir -p local/git && cd ~/local/git && git clone git@github.com:conflabermits/Scripts.git

echo "Enter git name then press Enter"
read -e name
git config --global user.name "${name}"
echo "Enter email address then press Enter"
read -e email
git config --global user.email "${email}"


