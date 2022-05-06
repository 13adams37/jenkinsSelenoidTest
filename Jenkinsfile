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
     stage('Run python env') {
        steps {
           catchError {
              script {
              	docker.image('python-web-tests').inside("--link ${c.id}:selenoid")
				}
      	    }
         }
     }
     stage('Pull browser') {
        steps {
           catchError {
            script {
				sh "pytest ${CMD_PARAMS}" 
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