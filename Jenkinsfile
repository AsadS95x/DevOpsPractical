pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash scripts/tests.sh"
            }
        }
        stage('Build and push containers') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose build --parallel"
                sh "docker-compose push"
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