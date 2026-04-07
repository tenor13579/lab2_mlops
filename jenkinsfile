pipeline {
    agent any 
    stages {
        stage('Install dpendencies') {
            steps {
                sh "pip install -r lab2/requirements.txt"
            }
        }

       stage('Fetch data') {
            steps {
                sh "python3 lab2/data_fetch.py"
            }
        } 

        stage('Preprocess data') {
            steps {
                sh "python3 lab2/data_preprocess.py"
            }
        }

        stage('Train model') {
            steps {
                sh "python3 lab2/train_model.py"
            }
        }

        stage('Install dpendencies') {
            steps {
                sh "python3 lab2/evaluate_.py"
            }
        }
    }
}