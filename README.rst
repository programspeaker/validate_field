Validate Filed
===============

This is a project that is used to validate fields, which is empty or it contain accurate values. Before touching the database we can check and raise appropriate error if any mistmatch on it.

Installing
============

.. code-block:: bash
    
    pip install validate-field

Usage
=====
Enter received_filed(field values that comes from the front-end side) and required_filed(list of values that need to be check in th back-end)

.. code-block:: bash

    from validate_field.validation import validate_field
    
    received_filed = {
        'id':1,
        'name':"sarath",
        'email':'test@gmail.com',
        'mobile':'+918330069872',
        'password':"abc@122#"
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
