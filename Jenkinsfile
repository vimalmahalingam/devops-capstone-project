pipeline {
    agent any

    environment {
        GITHUB_CREDS = credentials('github-creds')
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        DOCKER_IMAGE = "vimalmahalingam/devops-capstone-project"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vimalmahalingam/devops-capstone-project',
                    credentialsId: 'github-creds'
            }
        }

        // ✅ Updated Build & Test stage
        stage('Build & Test') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Set Docker Context') {
            steps {
                bat 'docker context use desktop-linux'
            }
        }

        stage('Docker Build') {
            steps {
                bat "docker build -t %DOCKER_IMAGE%:${env.BUILD_NUMBER} ."
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat "echo %DOCKERHUB_CREDS_PSW% | docker login -u %DOCKERHUB_CREDS_USR% --password-stdin"
                bat "docker push %DOCKER_IMAGE%:${env.BUILD_NUMBER}"
            }
        }

        stage('Deploy') {
            steps {
                bat "docker rm -f devops-capstone || exit 0"
                bat "docker run -d --name devops-capstone -p 8081:8080 --restart=always %DOCKER_IMAGE%:${env.BUILD_NUMBER}"
            }
        }

        stage('Monitoring') {
            steps {
                bat "docker ps -a"
                bat "docker logs --tail 50 devops-capstone"
            }
        }
    }
}
