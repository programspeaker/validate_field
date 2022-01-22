Validate Filed
=======================

This is a project that is used to validate fields, which is empty or it contain accurate values. Before touching the database we can check and raise appropriate error if any mistmatch on it.

Installing
=======================

.. code-block:: bash
    
    pip install validate_email

Usage
=======================
Enter received_filed(field values that comes from the customer side) and required_filed(list of values need to be check)

.. code-block:: bash

    >>> from src.validate_field import validate_field
    >>> received_filed = {"email":"dummy@xyz.com", "phone_number":"+919988776655"}
    >>> required_filed = [['phone_number','phone'],['email','email']]
   
    >>> validate_field.validate_field(received_filed, required_filed)
