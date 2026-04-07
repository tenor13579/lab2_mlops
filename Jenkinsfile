pipeline {
    agent any 
    
    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

       stage('Fetch data') {
            steps {
                sh './venv/bin/python3 data_fetch.py'
            }
        } 

        stage('Preprocess data') {
            steps {
                sh './venv/bin/python3 data_preprocess.py'
            }
        }

        stage('Train model') {
            steps {
                sh './venv/bin/python3 train_model.py'
            }
        }

        stage('Evaluate model') {
            steps {
                sh './venv/bin/python3 evaluate_model.py'
            }
        }
    }
}