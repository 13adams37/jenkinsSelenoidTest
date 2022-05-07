pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("python-web-tests", "-f Dockerfile .")
      	     }
          }
       }
    }
     stage('Pull browser') {
        steps {
            catchError {
            script {
				docker.image('selenoid/chrome:99.0')
      	      }
           }
        }
     }
	stage('Run tests') {
		steps {
			 sh '''#!/bin/bash
					docker run -d -t --link selenoid python-web-tests cmd.exe
			 '''
		}
	}
     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'report']]
    	   ])
  	        }
         }
     }
}