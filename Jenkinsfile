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
        catchError {
            script {
				docker.image('python-web-tests').inside("--link ${c.id}:selenoid") {sh "pytest ${CMD_PARAMS}"}
        	     }
      	    }
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