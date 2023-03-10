
resource "aws_s3_bucket" "stage_bucket_load" {
  bucket = local.bucket_name
}