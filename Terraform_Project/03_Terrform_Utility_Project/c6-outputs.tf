# Terraform Output Values
output "EC2_DNS_NAME" {
  description ="DNS_NAME"
  value = [for inst_dns in aws_instance.myec2vm: inst_dns.public_dns]
}

# output by EC2 Public DNS by To set
output "EC2_DNS_NAME_by_toset" {
  description ="DNS_NAME1_by_toset"
  value = toset([for inst_dns in aws_instance.myec2vm: inst_dns.public_dns])
}

# Out by map
output "EC2_DNS_NAME_by_tomap" {
  description ="DNS_NAME1_by_tomap"
  value =  { for az, inst_dns in aws_instance.myec2vm: az=> inst_dns.public_dns }
}
output "return_value2_each_az" {
  value = [for id in data.aws_ec2_instance_type_offerings.check-azone2: id.instance_types]
}

# output for each az with details
output "return_value3_each_az_details" {
  value = {for id,details in data.aws_ec2_instance_type_offerings.check-azone2:
           id=> details.instance_types}
}

# output for each az with details - remove the unsupported az
output "return_value4_filter_az" {
  value = {
  for id, details in data.aws_ec2_instance_type_offerings.check-azone2 :
  id=> details.instance_types if length(details.instance_types) != 0
  }
}

# output for each az with details - remove the unsupported az use the key functions
output "return_value5_filter_az_keys" {
  value = keys({
  for id, details in data.aws_ec2_instance_type_offerings.check-azone2 :
  id=> details.instance_types if length(details.instance_types) != 0
  })
}

# output for each az with details - remove the unsupported az use the key functions
output "return_value6_filter_az_first_keys" {
  value = keys({
  for id, details in data.aws_ec2_instance_type_offerings.check-azone2 :
  id=> details.instance_types if length(details.instance_types) != 0
  })[1]
}