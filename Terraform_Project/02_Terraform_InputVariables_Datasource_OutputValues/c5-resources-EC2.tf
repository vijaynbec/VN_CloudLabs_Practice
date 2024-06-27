# EC2 Instance
resource "aws_instance" "myec2vm" {
#  ami = "ami-08a0d1e16fc3f61ea"
#  instance_type = "t2.micro"
   ami = data.aws_ami.amzlinux2.id   # values pulled from data source
   instance_type = var.instance_type_ec2      # value pulled from variable.tf
   user_data = file("${path.module}/app1-install.sh")
   key_name = var.key_pair
  # value pulled from SG.tf files
   vpc_security_group_ids = [aws_security_group.allow_ssh.id, aws_security_group.allow_web.id]
#  count = 1
    tags = {
    Name = "Dev-myec2vm"
  }
}