from validation import validate_field

received_filed = {
    'id':1,
    'name':"testuser",
    'email':'testmail@gmail.com',
    'mobile':'+918330069872',
    'password':"testpass@122#",
    'is_active':True
}
required_filed = [
    ['id','int'],
    ['name','alpha'],
    ['email','email'],
    ['mobile','phone'],
    ['password','str'],
    ['is_active','dddbool']
]

validation_result = validate_field(received_filed, required_filed)
print(validation_result)
