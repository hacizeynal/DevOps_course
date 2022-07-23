pipeline {
    agent any
    stages {
        stage('Welcome Step ') {
            steps { 
                echo 'In this demo we will deploy application to EKS !'
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
            environment{
               AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
               AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
                }
            steps { 
                echo 'Deploy the App'
                sh "kubectl create deployment first_eks_deployment --image=nginx"
            }
        }
    }
}
