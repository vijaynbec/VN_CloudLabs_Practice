# data source for aws_ami

data "aws_ami" "amzlinux2" {
#  executable_users = ["self"]
  most_recent      = true
  owners           = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

# list data source for AZ's
data "aws_availability_zones" "myaws_az" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}