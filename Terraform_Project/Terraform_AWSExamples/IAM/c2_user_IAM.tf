# creating new users
resource "aws_iam_user" "Terraform_users" {
  name = "TF-User1"
  tags = {
    key = "Terraform"
  }
}