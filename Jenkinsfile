pipeline {
    agent any
    stages {
        stage('Copy files to Ansible Conrol Node') {
            steps { 
                echo 'Copy all necessary files to Ansible Conrol Node'
                sshagent(["ansible-key-server"]){   
                    sh 'scp -o StrictHostKeyChecking=no ansible/* root@188.166.163.179:/root'
                withCredentials([sshUserPrivateKey(credentialsId: "ec2-server",keyFileVariable: "keyfile",usernameVariable: 'user')]){
                    sh "scp ${keyfile} root@188.166.163.179:/root/ssh-key.pem"    
                    }
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
