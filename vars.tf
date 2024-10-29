variable "region" {
  type    = string
  default = "us-east-1"
}

variable "cognito_admin_username" {
  type    = string
  default = "admin@fastfood.com"
}

variable "academy_role" {
  type = string
  default = "arn:aws:iam::152915761077:role/LabRole"
}