data "aws_cognito_user_pools" "fastfood-user-pool" {
  name = "fastfood-user-pool"
}

data "aws_cognito_user_pool_clients" "fastfood-user-pool-app-client" {
  user_pool_id = data.aws_cognito_user_pools.fastfood-user-pool.ids[0]
}

resource "aws_lambda_function" "fastfood_lambda_authorizer" {
  function_name = "fastfood_lambda_authorizer"
  handler       = "lambda/function.handler"
  runtime       = "python3.11"
  role          = var.academy_role

  filename = "lambda.zip"

  source_code_hash = filebase64sha256("lambda.zip")

  environment {
    variables = {
      COGNITO_CLIENT_ID    = data.aws_cognito_user_pool_clients.fastfood-user-pool-app-client.client_ids[0],
      COGNITO_USER_POOL_ID = data.aws_cognito_user_pools.fastfood-user-pool.ids[0],
      COGNITO_ADMIN_USERNAME = var.cognito_admin_username,
    }
  }
}