pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh 'sudo apt update'
                sh 'sudo apt install python3 python3-pip python3-venv -y'
                sh "bash scripts/tests.sh"
            }
        }
        stage('Make Space-Remove existing images'){
            steps {
                sh 'docker system prune --all --volumes --force'
            }
        stage('Build and push containers') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker login --username $DOCKER_UNAME --password $DOCKER_PWORD"
                sh "bash scripts/containers.sh"
            }
        }
        stage('Run Ansible'){
            steps{
                sh "bash scripts/ansible.sh"
            }
        }
        stage('Deploy'){
            steps{
                sh "docker-compose up"
            }
    }
    }
   
}