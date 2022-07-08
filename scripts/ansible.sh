sudo apt update 
sudo apt install software-properties-common
sudo apt-add-repository -y --update ppa:ansible/ansible
sudo apt-get install -y ansible

ansible-playbook -i ansible/inventory.yaml ansible/playbook1.yaml
