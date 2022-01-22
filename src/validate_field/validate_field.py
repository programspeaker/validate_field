import phonenumbers
from django.core.validators import validate_email


def filed_exists(received_filed, required_filed):
    message = ''
    for i in required_filed:
        if i[0] not in received_filed or (i[0] in received_filed and received_filed[i[0]]==''):
            missing_value = i[0] + ' is not found'
            message = missing_value
            break
        
        if i[1] == 0:
            field_type = 'str'
        else:
            field_type = i[1]

        if (field_type == 'str'):
            field_name = i[0]
            field_value = received_filed[i[0]]
            mistmatch_type_value = is_string(field_name, field_value)
            message = mistmatch_type_value
            if message is not True:
                break

        elif field_type == 'int':
            field_name = i[0]
            field_value = received_filed[i[0]]
            mistmatch_type_value = is_integer(field_name, field_value)
            message = mistmatch_type_value
            if message is not True:
                break
        
        elif (field_type == 'alpha'):
            field_name = i[0]
            field_value = received_filed[i[0]]

            mistmatch_type_value = is_alpha(field_name, field_value)
            message = mistmatch_type_value
            if message is not True:
                break
        
        elif (field_type == 'phone'):
            field_name = i[0]
            field_value = received_filed[i[0]]

            mistmatch_type_value = is_phonenumber(field_name, field_value)
            message = mistmatch_type_value
            if message is not True:
                break
        
        elif (field_type == 'email'):
            field_name = i[0]
            field_value = received_filed[i[0]]

            mistmatch_type_value = is_email(field_name, field_value)
            message = mistmatch_type_value
            if message is not True:
                break

    return message


def is_integer(field_name, field_value):
    if not isinstance(field_value, int):
        mistmatch_type = field_name + ' is not an integer value'
        message = mistmatch_type
        return message
    else:
        return True


def is_string(field_name, field_value):
    if not isinstance(field_value, str):
        mistmatch_type = field_name + ' is not an string value'
        message = mistmatch_type
        return message
    else:
        return True


def is_alpha(field_name, field_value):
    field_value = field_value.isalpha()
    if field_value is False:
        mistmatch_type = field_name + ' is only allow alphabets'
        message = mistmatch_type
        return message
    else:
        return True


def is_phonenumber(field_name, field_value):
    my_number = phonenumbers.parse(field_value)
    if phonenumbers.is_valid_number(my_number) is False:
        mistmatch_type = field_name + 'is not a valid number'
        message = mistmatch_type
        return message
    else:
        return True


def is_email(field_name, field_value):
    if validate_email(field_value) is False:
        mistmatch_type = field_name + 'is not a valid email'
        message = mistmatch_type
        return message
    else:
        return True