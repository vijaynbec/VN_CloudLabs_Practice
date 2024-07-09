# EC2 Instance
resource "aws_instance" "myec2vm" {
  ami = data.aws_ami.amzlinux2.id   # values pulled from data source
  instance_type = var.instance_type_ec2      # value pulled from variable.tf
  user_data = file("${path.module}/app1-install.sh")
  key_name = var.key_pair
  # value pulled from SG.tf files
  vpc_security_group_ids = [aws_security_group.allow_ssh.id, aws_security_group.allow_web.id]

  # create EC2 instance in all AZ's of VPC - for each accept the string, maps.
  # pull az information from C4 data source
  for_each = toset(data.aws_availability_zones.myaws_az.names)
  availability_zone = each.key #You can also use each.value because for list items each.key == each.value
  tags = {
  Name = "Dev-myec2vm-for-each-${each.value}"
  }
}