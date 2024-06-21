provider "aws" {
  profile = "default" # AWS Credentials Profile configured on your local desktop terminal  $HOME/.aws/credentials
  region  = "us-east-1"
}
variable "inst_type" {
  type = list
  default = ["t2.macro", "t2.nano","t2.medium"]
}
# Resource Block
resource "aws_instance" "ec2demo" {
  ami           = "ami-05c13eab67c5d8861" # Amazon Linux in us-east-1, update as per your region
  instance_type = var.inst_type[count.index]
  count = 3  # count paremeter to increase
  tags          = {
    Name = "First EC2 by Terraform"
  }
}