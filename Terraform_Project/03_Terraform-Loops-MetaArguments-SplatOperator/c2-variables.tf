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

# AWS instance type as LIST
variable "instance_type_list" {
  description = "EC2 instance types LIST"
  type = list(string)  # type as list
  default = ["t2.micro", "t3.small"]  # list in []
}

# AWS instance type as MAP

variable "instance_type_map" {
  description = "EC2 instance type as MAP"
  type = map(string)        # type as map
  default = {            # map in {}
    "dev" = "t2.micro"
    "qa" = "t3.small"
  }
}