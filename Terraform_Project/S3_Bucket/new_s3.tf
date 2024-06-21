provider "aws" {
  profile = "default" # AWS Credentials Profile configured on your local desktop terminal  $HOME/.aws/credentials
  region  = "us-east-1"
}
resource "aws_s3_bucket" "example" {
   bucket = "luxxy-covid-testing-system-pdf-pt-vs12"
#   acl = "private"
 }

