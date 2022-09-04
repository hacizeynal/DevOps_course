pipeline {
    agent any
    stages {
        stage('Copy files to Ansible Conrol Node') {
            steps { 
                echo 'Copy all necessary files to Ansible Conrol Node'
                sshagent(["ansible-key-server"]){
                    sh 'scp -o StrictHostKeyChecking=no ansible/* root@188.166.163.179:/root'
                }
            }
        }
        stage('Building Step') {
            steps { 
                echo 'Building App'
            }
        }
        stage('Testing Step') {
            steps { 
                echo 'Testing App'
            }
        }
        stage('Deploying Step') {
            steps { 
                echo 'Deploy the App'
            }
        }
    }
}
