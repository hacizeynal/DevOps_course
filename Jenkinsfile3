pipeline {
    agent any
    tools {
        maven "maven-3.8.6"}
    stages {
        stage('Build App') {
            steps {
                script{
                    echo 'Building the Application'
                    sh "mvn package"
                    }
            }
        }
        stage('Deploying Step') {
            steps {
                echo 'Deploy the App'
            }
        }
    }
}