## Written values from TF after implementing a TF apply
#
## Output Public IP and Public DNS
#
#output "ec2-public-ip" {
#  value = aws_instance.myec2vm.public_ip
#}
#output "ec2-arn" {
#  value = aws_instance.myec2vm.arn
#}
#
#output "ec2-dns" {
#  value = aws_instance.myec2vm.public_dns
#}
#
#output "ec2-instance-state" {
#  value = aws_instance.myec2vm.instance_state
#}
# for loop with list,map and map advanced
/*
1. Loop with list
2. Loop with Map
3. Loop with Map Advanced
4. splat operators - returns to list
5. Latest splat operators - returns to list
*/

# Loop with list
output "for_out_list" {
  description = "Loop with list"
  value = [for instance in aws_instance.myec2vm: instance.public_dns]
}

# Output with Map
output "for_out_map" {
  description = "Loop with map"
  value = {for instance in aws_instance.myec2vm: instance.id => instance.public_dns}
}

# Output with Map Advanced
output "for_out_map2" {
  description = "Loop with map2"
  value = {for i, instance in aws_instance.myec2vm: i=> instance.public_dns}
}

# output via splat operators - return the list
output "splat_out_publicdns" {
  description = "values by splat operator"
  value = aws_instance.myec2vm.*.public_dns
}

# output via splat operators - return the list
output "splat_out_publicdns_latest" {
  description = "values by splat latest operator"
  value = aws_instance.myec2vm[*].public_dns
}