if [ -z "$(docker --version 2> /dev/null)" ]; then
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker $USER
fi