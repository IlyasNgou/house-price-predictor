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
