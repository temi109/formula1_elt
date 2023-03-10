
variable "aws_profile" {
  description = "Profile to use to authenticate to  AWS"
  type        = string
}

variable "aws_region" {
  description = "Default region to use in AWS"
  default = "eu-west-2"
  type        = string  
}

variable "aws_access_key_id" {
type = string
}

variable "aws_secret_access_key" {
  type = string
}

variable "aws_account_id" {
  description = "AWS account ID"
  type        = string
}


variable "snowflake_account" {
  type        = string
}

variable "snowflake_user" {
  type        = string
}

variable "snowflake_password" {
  type        = string
}