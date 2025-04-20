pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python model/train.py'
            }
        }

        stage('Deploy') {
            steps {
                sh 'nohup python app/app.py &'
            }
        }
    }
}
