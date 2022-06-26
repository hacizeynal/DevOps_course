pipeline {
    agent any
    stages {
        stage('Welcome Step') {
            steps {
                echo 'Welcome to JenkinsTest'
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
                script{
                    def dockerCommands = "docker run -p 3080:80 -d zhajili/my_aws_app:1.1"
                    echo 'Deploy the Application in AWS EC2'
                        sshagent(['ec2-aws']) {
                            sh "ssh -o StrictHostKeyChecking=no ec2-user@3.73.122.101 ${dockerCommands}"
                        }
                    }

            }
        }
    }
}