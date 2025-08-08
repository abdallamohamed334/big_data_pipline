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

    stage('Start Kafka (Docker)') {
      steps {
        dir('docker/kafka') {
          sh 'docker compose up -d'
        }
        sh 'sleep 20' // وقت للتحضير
      }
    }

    stage('Run Producer') {
      steps {
        sh '. venv/bin/activate && python data_ingest/producer.py'
      }
    }

    stage('Run Consumer') {
      steps {
        sh '. venv/bin/activate && python data_ingest/consumer.py'
      }
    }

    stage('Run DBT Transform') {
      steps {
        sh '. venv/bin/activate && cd data_transformation && dbt run'
      }
    }
  }

  post {
    always {
      echo 'Pipeline execution completed.'
    }
  }
}
