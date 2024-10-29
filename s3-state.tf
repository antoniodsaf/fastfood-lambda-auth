terraform {
  backend "s3" {
    bucket = "fastfood-tf"
    key = "lambda-auth/terraform.tfstate"
    region = "us-east-1"
  }
}