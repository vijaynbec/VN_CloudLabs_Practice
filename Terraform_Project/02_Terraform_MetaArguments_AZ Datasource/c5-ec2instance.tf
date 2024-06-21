

# list down avaliblity zones
data "aws_availability_zones" "list_azones" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}


# EC2 Instance
resource "aws_instance" "myec2vm" {
  ami = data.aws_ami.amzlinux2.id
  instance_type = var.instance_type
##  instance_type = var.instance_type_list[0] # from list
#  instance_type = var.instance_type_map["dev"]  # from map
  user_data = file("${path.module}/app1-install.sh")
#  key_name = var.instance_keypair
  vpc_security_group_ids = [ aws_security_group.vpc-ssh.id, aws_security_group.vpc-web.id]
# Create instance in all AZ's by using for_each
  for_each = toset(data.aws_availability_zones.list_azones.names)
  availability_zone = each.key
  # each.key return the same value
  tags = {
    "Name" = "EC2Demo_foreach-${each.value}"
  }
}
