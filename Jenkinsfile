//https://docs.aws.amazon.com/AmazonECR/latest/userguide/push-oci-artifact.html

pipeline {
    agent any
    
    
    
    environment {
        DOCKERHUB_USER = credentials('dockerhub-username')
        DOCKERHUB_PASS = credentials('dockerhub-password')
        CHART_NAME = "helm-chart"
        AWS_DEFAULT_REGION = "ap-south-1"
        AWS_CREDENTIALS_ID = "aws-ecr-credentials"
        AWS_ACCOUNT_ID = "021891584638"
        ECR_REPO = 'abdulp07'
        ECR_REGION = "ap-south-1"  
        
    }

    stages {
        stage('Chekout') {
            

            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/abdulp07-git/w20-djangoapp.git'

            }

        }
        
        stage("django-image"){
            steps {
                script {
                    def dockerImage = "abdulp07/w20django"
                    def tag = "v${BUILD_NUMBER}"
                    def fullImageName = "${dockerImage}:${tag}"
                    sh "docker build -t ${fullImageName} ."
                    
                }
                
            }
        }
        
        stage("Push image to docker hub"){
            steps {
                script {
                    def dockerImage = "abdulp07/w20django"
                    def tag = "v${BUILD_NUMBER}"
                    def fullImageName = "${dockerImage}:${tag}"
                    
                    sh '''
                    #!/bin/bash
                    
         echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin
                    '''

                    sh "docker push ${fullImageName}"
                    
                }
            }
            
            post {
                always {
                    sh 'docker logout'
                    sh 'docker rmi abdulp07/w20django:v${BUILD_NUMBER}'
                }
            }
        }
        
        
        stage ("Update new tag in Charts"){
            steps {
                sh './replacetag.sh'
                sh 'helm package $CHART_NAME'
                
            }
        }
        
        
        stage('Login to AWS ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${AWS_CREDENTIALS_ID}"]]) {
                    script {
                        // Log in to AWS ECR
                        sh '''
                            aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | \
                            helm registry login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
                        '''
                    }
                }
            }
        }
        
        
        stage('Push Helm Chart to ECR') {
    steps {
        script {
            // Push the Helm chart to ECR
            sh """
    # Check if the repository exists
    set +e
    REPO_EXISTS=\$(aws ecr describe-repositories --repository-names "${CHART_NAME}" --region "${ECR_REGION}" --query "repositories[0].repositoryName" --output text 2>/dev/null)
    set -e

    if [ "\${REPO_EXISTS}" != "${CHART_NAME}" ]; then
        echo "Repository does not exist. Creating repository ${CHART_NAME}..."
        aws ecr create-repository --repository-name "${CHART_NAME}" --region "${ECR_REGION}"
        echo "Repository ${CHART_NAME} created."
    else
        echo "Repository ${CHART_NAME} already exists."
    fi
    
    # Push the Helm chart to the ECR repository
    helm push ${CHART_NAME}-0.1.${BUILD_NUMBER}.tgz oci://${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
"""
        }
    }

    post {
        always {
            sh 'rm -f ${CHART_NAME}-0.1.${BUILD_NUMBER}.tgz'
        }
    }
}

        
        
    } // stages closed




}//Pipeline closed


