pipeline {
    agent any

    stages {
        stage('Clone and generate File system') {
            steps {
                sh "rm -rf file_system"
                sh "git clone https://github.com/ananthm1254/file_system.git"
                sh "cd file_system"
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