pipeline {
    agent {
       node {
         label 'agent_dev1'
      }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sahana-sonu/MultiBranch.git', credentialsId: 'test_pipeline'
            }
        }
        
        stage('Compile') { 
            when {
                branch 'dev'
            }
            steps {
                bat 'javac Testfile.java'
                bat 'java Testfile'
            }
        }

        stage('Run') {
            when {
                branch 'main'
            }
            steps {
                bat 'python test_ops.py'
            }
        }
    }
}

