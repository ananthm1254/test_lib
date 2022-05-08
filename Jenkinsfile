pipeline {
    agent any

    stages {
        stage('Clone and generate File system') {
            steps {
                sh "rm -rf file_system"
                sh "git clone https://github.com/ananthm1254/file_system.git"
                sh "cd file_system && git checkout feature/file-system-improvement"
                sh "cd file_system && python3 file_generator.py --page_count=16"
                sh "mkdir -p logs"
            }
        }
        stage('Build Library') {
            steps {
                sh "cd file_system && make build 2>&1 | tee ../logs/file_system_build.log"
            }
        }
        stage('Build Python Test Framework') {
            steps {
                sh "sudo python3 setup.py build"
                sh "sudo python3 setup.py install"
                sh "pip install -r requirements_dev.txt"
            }
        }
        stage('Test-1'){
            steps {
                sh "python3 -m flake8 libs test_runner test_scripts -v 2>&1 | tee logs/flake8.log"
            }
        }
        stage('Test-2'){
            steps {
                sh "./run_tests.sh test_scripts/template_test.py --build_library=file_system/build/libfilesystem.so"
                sh "./run_tests.sh test_scripts/write_read_compare_direct.py --build_library=file_system/build/libfilesystem.so"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'logs/*.log'
        }
    }
}