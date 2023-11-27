pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    
                    sh 'ssh ubuntu "/home/ubuntu/cicdassignment/app.py"'
                    sh 'ssh ubuntu "/home/ubuntu/cicdassignment/app.py && pip install -r requirements.txt"'
                    sh 'ssh ubuntu "/home/ubuntu/cicdassignment/app.py && systemctl restart your-app-service"'
                }
            }
        }
    }
}
