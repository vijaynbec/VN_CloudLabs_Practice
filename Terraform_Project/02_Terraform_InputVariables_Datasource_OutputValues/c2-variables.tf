# Input Variables

# AWS Regions
variable "aws_region_ec2" {
  description = "AWS Regions to launch the AWS resources"
  type = string
  default = "us-east-1"
}
# Instance Type
variable "instance_type_ec2" {
  description = "EC2 Instance Type"
  type = string
  default = "t2.micro"
}
# instance Key pair
variable "key_pair" {
  description = "static key pair to associate with instance"
  type = string
  default = "terraform-key"
}