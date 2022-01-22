Validate Filed
===============

> This is a project that is used to validate fields, which is empty or it contain accurate values. Before touching the database we can check and raise appropriate error if any mistmatch on it.

Installing
============

.. code-block:: bash

pip install validate_email

Usage
=====

.. code-block:: bash

    >>> from src.validate_field import filed_exists
    >>> received_filed = {"email":"email", "phone_number":"+918330063408"}
    >>> required_filed = [['phone_number','phone'],['email','email']]
   
    >>> validate_field.filed_exists(received_filed, required_filed)
