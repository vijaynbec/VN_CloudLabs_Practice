# EC2 Instance
resource "aws_instance" "myec2vm" {
  ami = data.aws_ami.amzlinux2.id
  instance_type = var.instance_type
#  instance_type = var.instance_type_list[1]   # for list
#  instance_type = var.instance_type_map["dev"]   # for map
  user_data = file("${path.module}/app1-install.sh")
#  key_name = var.instance_keypair
  vpc_security_group_ids = [ aws_security_group.vpc-ssh.id, aws_security_group.vpc-web.id   ]
  count = 3
  tags = {
    "Name" = "Countdemo-${count.index}"
  }
}
