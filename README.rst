Validate Field
=======================

This is a project that is used to validate fields which is empty or it contain accurate values. Before touching the database we can check and raise appropriate error message if any mistmatch on it, else return True.

.. code-block:: bash

    1)  Check value is missed or empty
    2)  Check wether the datatype is correct or not
        2.1)    int = Specifies the integer 
        2.2)    str = Specifies the string  
        2.3)    email = Specifies the email  
        2.4)    phone = Specifies the phone number  
        2.5)    alpha = Specifies the alphabetes  
        2.6)    '' = Specifies the null value, is equal to str

Installing
=======================

.. code-block:: bash
    
    pip install validate-field

Usage
=======================
Enter received_field(values that comes from the front-end side) and required_field(list of values that need to be check in th back-end)

.. code-block:: bash

    from validate_field.validation import validate_field
    
    received_filed = {
        'id':1,
        'name':"testuser",
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_filed = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_filed, required_filed)
    print(validation_result)
    
    Result
    ====================
    >> True
 

**Usecase 1** :- Check field is missing or not

Rule : name field is mandatory(required field)

Scenario : Avoid 'name' field

.. code-block:: bash

    received_field = {
        'id':1,
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> name is not found
 

**Usecase 2** :- Check field is empty or not("")

Rule : name field is mandatory(required field)

Scenario : Avoid 'name' field value(name = "")


.. code-block:: bash

    received_field = {
        'id':1,
        'name':"",
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> name is not found
 
 
**Usecase 3** :- Check integer field(int)

Rule : 'id' field only allow integer values

Scenario : Pass string value to the field 'id'

.. code-block:: bash

    received_field = {
        'id':"a",
        'name':"testuser",
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> id is not an integer value
  
 
**Usecase 4** :- Check alpha field(alpha)

Rule : 'name' field only allow alphabetes
 
Scenario : Pass integer values along with the field 'name'

.. code-block:: bash

    received_field = {
        'id':1,
        'name':"testuser123",
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> name is only allow alphabets
    
 
**Usecase 5** :- Check email field(email)

Rule : 'email' should be in correct format
 
Scenario : Pass incorrect format to the field 'email'

.. code-block:: bash

    received_field = {
        'id':1,
        'name':"testuser",
        'email':'testmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >>email is not a valid email
 
 
**Usecase 6** :- Check phonenumber field(phone)

Rule : 'mobile' should be in correct format(Correct country code)
 
Scenario : Pass 'mobile' field with invalid country code +90

.. code-block:: bash

    received_field = {
        'id':1,
        'name':"testuser",
        'email':'testmail@gmail.com',
        'mobile':'+908330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> mobile is not a valid phone number


**Usecase 7** :- Check phonenumber field(phone)

Rule : 'mobile' should be in correct format(Correct length)
 
Scenario : Pass 'mobile' field with invalid length +918330 or +918330069872333333

.. code-block:: bash

    received_field = {
        'id':1,
        'name':"testuser",
        'email':'testmail@gmail.com',
        'mobile':'+918330',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> mobile is not a valid phone number
 
 
**Usecase 8** :- Check string field(str)

Rule : 'password' field only allow string

Scenario : Pass 'password' field with integer value

.. code-block:: bash

    received_field = {
        'id':1,
        'name':"testuser",
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':123
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','str']
    ]
   
    validation_result = validate_field(received_field, required_field)
    print(validation_result)
    
    Result
    ====================
    >> password is not a string value
  

If you are does not specify the field type, then the field type will be consider as **string**(str)
 
Scenario : Specify 'password' field type as " "

 .. code-block:: bash

    received_field = {
        'id':1,
        'name':"testuser",
        'email':'testmail@gmail.com',
        'mobile':'+918330069872',
        'password':"testpass@122#"
    }
    required_field = [
        ['id','int'],
        ['name','alpha'],
        ['email','email'],
        ['mobile','phone'],
        ['password','']
    ]
 
 
Here password consider as string value.
