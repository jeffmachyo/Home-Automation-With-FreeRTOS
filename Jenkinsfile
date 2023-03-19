pipeline {
  agent any
  stages {
    stage('Checkout') {
        steps {
            sh 'echo "Checking Out..."'
            checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jeffmachyo/Home-Automation-With-FreeRTOS.git']])
        }
        }
    stage('Build') {
      steps {
        //   cmakeBuild(
        //     installation: 'InSearchPath'
        //   )
        sh 'echo "Building..."'
        sh 'chmod +x ./installer.sh'
        sh 'bash ./installer.sh'
        // archiveArtifacts artifacts: 'Version_1/out/build/*', fingerprint: true
      }
    }
    // stage('Test') {
    //   steps {
    //     //   cmakeBuild(
    //     //     installation: 'InSearchPath'
    //     //   )
    //     sh 'echo "Running..."'
    //     sh 'chmod +x ./Version_1/run.sh'
    //     sh 'bash ./Version_1/run.sh'
    //   }
    // }
  }
}

// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jeffmachyo/Home-Automation-With-FreeRTOS.git']])
//             }
//         }
//         stage('Build') {
//             steps {
//                 sh 'export PYTHONPATH="$WORKSPACE:./src/main/python:./src/test/python:$PYTHONPATH"'
//                 sh 'echo $PYTHONPATH'
//                 sh 'python3 src/test/python/programmingtheiot/part01/unit/system/SystemCpuUtilTaskTest.py'
//             }
//         }
//     }
// }