# Terraform Settings Block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      #version = "~> 3.21" # Optional but recommended in production
    }
  }
}

# Provider Block
provider "aws" {
  profile = "default" # AWS Credentials Profile configured on your local desktop terminal  $HOME/.aws/credentials
  region  = "us-east-1"
}
#import {
#  to = aws_instance.myec21
#  id = "i-0c5312331e4cd2a4f"
#}

# terraform plan -generate-config-out=generated_resources.tf    => for above lines

#resource "aws_instance" "myec21" {
#    ami =  "ami-0230bd60aa48260c6"
#    instance_type = "t2.micro"
#}
#  terraform import aws_instance.myec21 i-0c5312331e4cd2a4f  => generate the state file above 3 lines