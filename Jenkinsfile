pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup venv and Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'venv\Scripts\activate && pytest tests/'
            }
        }

        stage('Train Model') {
            steps {
                bat 'venv\Scripts\activate && python model/train.py'
            }
        }

        stage('Deploy') {
            steps {
                bat 'venv\Scripts\activate && start "" /B python app/app.py'
            }
        }

    }
}
