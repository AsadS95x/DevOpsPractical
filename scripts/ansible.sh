
sudo apt-add-repository -y --update ppa:ansible/ansible
sudo apt-get install -y ansible

ansible-playbook -i ansible/inventory.yaml ansible/playbook1.yaml