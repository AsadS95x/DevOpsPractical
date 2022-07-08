pipeline {
    agent any
    stages {
        stage('Install Dependancies') {
            steps {
                sh "bash scripts/dependancies.sh"
            }
        }

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
                sh "docker login --username $DOCKER_UNAME --password $DOCKER_PWORD"
                sh "bash scripts/containers.sh"
            }
        }

//        stage('Run Ansible'){
//            steps{
//               sh "bash scripts/ansible.sh"
//            }
//        }

        stage('Deploy') {options {
        timeout(time: 3, unit: 'MINUTES') }
            steps{
                sh "docker-compose up"
            }
        }
    }
   
}