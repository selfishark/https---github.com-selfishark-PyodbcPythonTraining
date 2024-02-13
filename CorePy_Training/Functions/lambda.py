tach = range(1100, 3500, 200)

# Lambda function
# use lambda function only once,
# map(lambda x: expression)
# lambda n: int(round(n, -2))
lambda_result = list(zip(map(lambda r: 0.7724 * r * 1.0134, tach), tach))
result = lambda_result[1]
print(result)
