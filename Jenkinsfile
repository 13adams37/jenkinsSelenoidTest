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
          	     docker.image('selenoid').withRun('-p 4444:4444 -v /run/docker.sock:/var/run/docker.sock ',
            	'-timeout 600s -limit 2') { c ->
              	docker.image('python-web-tests').inside("--link ${c.id}:selenoid") {
                    	sh "pytest ${CMD_PARAMS}"
                	    }
                   }
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