# EC2 Instance
resource "aws_instance" "myec2vm" {
  ami = "ami-08a0d1e16fc3f61ea"
  instance_type = "t2.micro"
  user_data = file("${path.module}/app1-install.sh")
  count = 1
    tags = {
    Name = "Dev-myec2vm"
  }
}
