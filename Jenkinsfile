pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/IlyasNgou/house-price-predictor.git'
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
                bat 'nohup python app/app.py &'
            }
        }
    }
}
