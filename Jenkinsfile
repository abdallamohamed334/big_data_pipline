pipeline {
  agent any

  environment {
    KAFKA_BOOTSTRAP = 'localhost:9092'
  }

  stages {
    stage('Checkout') {
      steps { git 'https://github.com/abdallamohamed334/big_data_pipline.git' }
    }

    stage('Install Python Dependencies') {
      steps {
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate'
        sh 'pip install dbt kafka-python psycopg2-binary'
      }
    }
 
  }

  post {
    always {
      echo 'Pipeline execution completed.'
    }
  }
}
