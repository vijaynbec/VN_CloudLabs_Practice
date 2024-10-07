# Flask_app_CICD

- Update the ECR library in the required place
- IAM Roles: EC2, Codedeploy and Codebuild
    EC2: (S3, Codedeploy, ECR)        
            AmazonEC2ContainerRegistryFullAccess
            AmazonS3FullAccess 
            AWSCodeDeployFullAccess.

     CodeDeploy: (for EC2)
             AmazonEC2RoleforAWSCodeDeploy
             AWSCodeDeployFullAccess

      Codebuild:  (for ECR)
             AmazonEC2ContainerRegistryFullAccess
  
-   Create the application code and add to repo.
-   Create ECR Repository for Images.
-   Configure/define Code Build project and  buildspec.yml and attach the role
-   Configure/define Codedeploy, deploymentgroup,deployment using appspec.yml file and attach the role.
-   Configure CodePipeline project – using GIT connection as source, Codebuild and             
-   Codedeploy details with default service role.
-   EC2 Instance preperations for application installations.
    > Launch Simple EC2 instance.
    > Attache securitygroup with Inbound traffic any.
    > Attach IAM role for EC2
    > Install code deploy agent
    > Install nginx
    > Update proxy
    > Restart nginx
    > Connect the EC2 instances and execute the below commands.
       sudo apt updatesudo apt install ruby-fullsudo apt install wgetcd /home/ubuntu
       wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
       chmod +x ./installsudo ./install auto
       sudo service codedeploy-agent status
       sudo apt install nginx
       sudo vim /etc/nginx/sites- available/default
       Update location as below:
            proxy_pass http://127.0.0.1:5000; 
       sudo systemctl restart nginx




