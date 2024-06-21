# listing existing users

output "users-terraform" {
  description = "for loop list"
  value = aws_iam_user_group_membership.TF-Group-assign.user
#  value = aws_iam_group.Terraform_groups.name
}



