pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup venv') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python model/train.py'
            }
        }

        stage('Deploy') {
            steps {
                bat 'start "" /B python app/app.py'
            }
        }

    }
}
