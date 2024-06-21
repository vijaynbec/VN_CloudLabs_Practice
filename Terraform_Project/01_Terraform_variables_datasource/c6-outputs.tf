# Terraform Output Values
# EC2 Instance Public IP
#output "instance_publicip" {
#  description = "EC2 Instance Public IP"
#  value = aws_instance.myec2vm.public_ip
#}
#
## EC2 Instance Public DNS
#output "instance_publicdns" {
#  description = "EC2 Instance Public DNS"
#  value = aws_instance.myec2vm.public_dns
#}
# Output from loop list
output "output_by_list" {
  description = "for loop list"
  value = [ for inst in aws_instance.myec2vm: inst.public_dns]
  }

# Output from loop Map
output "output_by_map" {
  description = "for loop map"
  value = [ for inst_dns in aws_instance.myec2vm: inst_dns.public_dns]
  }
# Output from short or splash operators
output "output_by_splash" {
  description = "by splash operator"
  value = aws_instance.myec2vm[*].public_dns
  }