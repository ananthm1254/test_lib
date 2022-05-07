pipeline {
    agent any

    stages {
        stage('Clone and generate File system') {
            steps {
                sh "rm -rf file_system"
                sh "git clone https://github.com/ananthm1254/file_system.git"
                sh "cd file_system && git checkout feature/file-system-improvement"
                sh "cd file_system && python3 file_generator.py"
            }
        }
        stage('Build Library') {
            steps {
                sh "cd file_system && make build"
            }
        }
        stage('Test') {
            steps {
                sh "sudo python3 setup.py build"
                sh "sudo python3 setup.py install"
                sh "pip install -r requirements_dev.txt"
                sh "python3 -m flake8 libs test_runner test_scripts -v"
            }
        }
    }
}