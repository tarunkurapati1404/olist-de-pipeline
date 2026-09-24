# 1. Configure the AWS Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# 2. Define the AWS Region
provider "aws" {
  region = "eu-north-1" # Using your Stockholm region
}

# 3. Create the S3 Bucket for our Data Lake
resource "aws_s3_bucket" "olist_data_lake" {
  bucket = "tarun-olist-lake-terraform-2026" # Make sure this name is globally unique!
  
  tags = {
    Name        = "Olist Data Lake"
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}