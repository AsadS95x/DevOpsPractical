#!/bin/bash

declare -a dirs=(Service2-FE Service3-Loc Service4-Size Service5-Price)

for dir in ${dirs[@]}; do
    cd ${dir}
    sudo python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 -m pytest --cov=. --cov-report xml -v
    deactivate
    cd ..
done

#lordhelpme