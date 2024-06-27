# Written values from TF after implementing a TF apply

# Output Public IP and Public DNS

output "ec2-public-ip" {
  value = aws_instance.myec2vm.public_ip
}
output "ec2-arn" {
  value = aws_instance.myec2vm.arn
}

output "ec2-dns" {
  value = aws_instance.myec2vm.public_dns
}

output "ec2-instance-state" {
  value = aws_instance.myec2vm.instance_state
}