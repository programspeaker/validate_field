from validate_field.validation import validate_field


received_filed = {
	'user_login_id':1,
	'user_name':'test@',
	'email':'test@gmail.com'
}
required_filed = [
    ['user_login_id','int'],
    ['user_name','alpha'],
    ['email','email']
]

validation_result = validate_field(received_filed, required_filed)
print(validation_result)