# creating a new users add to groups

resource "aws_iam_group" "Terraform_groups" {
  name = "Terraform-Gr"
}

resource "aws_iam_user_group_membership" "TF-Group-assign" {
  user = aws_iam_user.Terraform_users.name

  groups = [
    aws_iam_group.Terraform_groups.name
  ]
}