pipeline {
    agent any
    stages {
        stage('Copy files to Ansible Conrol Node') {
            steps { 
                echo 'Copy all necessary files to Ansible Conrol Node'
                sshagent(["ansible-key-server"]){   
                    sh 'scp -o StrictHostKeyChecking=no ansible/* root@188.166.163.179:/root'
                withCredentials([sshUserPrivateKey(credentialsId: "ec2-server",keyFileVariable: "keyfile",usernameVariable: 'user')]){
                    sh 'scp $keyfile root@188.166.163.179:/root/ssh-key.pem' 
                    }
                } 
            }
        }
        stage('Execute Ansible Playbook') {
            steps { 
                
                script{
                    echo 'Configuring EC2 instances via Ansible'
                    def remote = [:]
                    remote.name = "ansible-server"
                    remote.host = "188.166.163.179"
                    remote.allowAnyHosts = true
                    withCredentials([sshUserPrivateKey(credentialsId: "ansible-key-server",keyFileVariable: "keyfile",usernameVariable: 'user')])
                    {   
                    remote.user = user
                    remote.identityFile = keyfile
                    sshCommand remote: remote, command: 'ls -la' 
                    }
                     

                }
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
