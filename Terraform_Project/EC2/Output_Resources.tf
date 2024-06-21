provider "aws" {
  profile = "default" # AWS Credentials Profile configured on your local desktop terminal  $HOME/.aws/credentials
  region  = "us-east-1"
}
# creating elastic IP
resource "aws_eip" "lb" {
  domain   = "vpc"                   # vpc its get created
}

output "PUBLIC_IP-Value-for_EIP" { value = aws_eip.lb.public_ip }  # get single attribute
output "Public_DNS_Value_EIP" {value = aws_eip.lb.public_dns}  # get single attribute
output "Public_IP_DNS_Value_EIP" {value = "https://${aws_eip.lb.public_dns}:8080"} # get single attribute with alters
output "Public_ALL_Value_EIP" {value = aws_eip.lb}  # get all attribute
output "value" {value = "https://${aws_eip.lb.public_dns}:8080"} # get single attribute with alters

