#!/bin/bash
#!/bin/bash

sudo apt-get update
sudo apt install python3.10-venv

declare -a dirs=(Service2-FE Service3-Loc Service4-Size Service5-Price)

for dir in ${dirs[@]}; do
    cd ${dir}
    sudo python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 -m pytest '''--cov=application --cov-report=html'''
    deactivate
    cd ..
done

#lordhelpme