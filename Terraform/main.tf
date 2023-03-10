#Create an encrypted bucket and restrict access from public
# resource "aws_s3_bucket" "stage_bucket_load" {
#   bucket = local.bucket_name

# }

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = "~> 0.56.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = var.aws_region
  profile = "Temidayo"
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

locals {
  bucket_name  = "temi-formula1"
}

provider "snowflake" {
    account          = var.snowflake_account
    region           = "uk-south.azure" 
    username         = var.snowflake_user
    role             = "ACCOUNTADMIN"
    password         = var.snowflake_password
}