pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                echo "Finished"
            }
        }
        stage('Clone and generate File system') {
            steps {
                sh "git clone https://github.com/ananthm1254/file_system.git"
                sh "git pull"
                sh "git checkout feature/file-system-improvement"
                sh "python3 file_generator.py"
            }
        }
        stage('Build Library') {
            steps {
                sh "make build"
            }
        }
    }
}