CODE_CHANGES = getCode()
BRANCH_NAME = getBranch()
pipeline {
    agent any
    stages{
        stage("Build") {

             when {

                expression {

                   BRANCH_NAME == 'dev' && CODE_CHANGES == true
                }
             }

             steps {

                 echo 'building the app...'
             }
         }

         stage("Test") {

             when {

              expression {

                 BRANCH_NAME == 'dev' || BRANCH_NAME == 'prod'}
              }

             }

             steps {

                 echo 'testing the app...'
             }
         }

         stage("Deploy") {
             steps{

                 echo 'deploying the app'
             }
         }

        }


    post{

       always {

          echo 'executes whether build fails or pass'
       }

       success {

          echo 'executes if build success'
       }

       failure {

         echo 'executes if build fails'
       }
    }

}

       

