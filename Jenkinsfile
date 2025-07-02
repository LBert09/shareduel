pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building the project..."
                sh 'python test.py'
            }
        }
        stage('Test') {
            steps {
                echo "Testing the project..."
            }
        }
    }
}