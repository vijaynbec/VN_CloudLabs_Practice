
# check the avail zones
data "aws_availability_zones" "my_azones" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}
#ata "aws_ec2_instance_type_offerings" "check-azone" {
data "aws_ec2_instance_type_offerings" "check-azone2" {
  for_each = toset(data.aws_availability_zones.my_azones.names)
  filter {
    name   = "instance-type"
    values = ["t3.micro"]
  }
  filter {
    name   = "location"
    values = [each.value]
    #values = ["us-east-1a"]
#    values = ["us-east-1e"]
  }
  location_type = "availability-zone"
}
# AWS EC2 Instance Type
variable "instance_type" {
  description = "EC2 Instnace Type"
  type = string
  default = "t3.micro"
}

