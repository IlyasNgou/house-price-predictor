pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup venv & Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/'
            }
        }

        stage('Trivy Scan') {
            steps {
                bat 'trivy fs --exit-code 1 --severity HIGH,CRITICAL .'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t home-prediction-app .'
            }
        }

        stage('Docker Compose Up') {
            steps {
                bat 'docker-compose up --build -d'
            }
        }

        stage('Ansible Deploy') {
            steps {
                bat 'docker build -t ansible-runner ./ansible'
                bat 'docker run --rm -v %cd%:/ansible ansible-runner deploy.yml'
            }
        }
    }
}
