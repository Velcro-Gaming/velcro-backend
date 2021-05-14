import os
import re
import csv
import json
import base64
import random
import string
import phonenumbers
from PIL import Image
from io import BytesIO

from django.core.files.base import ContentFile
from django.conf import settings
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_int_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_referral_code_generator(instance):
    Klass = instance.__class__
    new_referral_code = random_int_generator(size=8)
    while Klass.objects.filter(referral_code=new_referral_code).exists():
        new_referral_code = random_string_generator(size=8)
    return new_referral_code


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    slug = slugify(instance.name)
    new_slug = slug
    Klass = instance.__class__
    numb = 1
    while Klass.objects.filter(slug=new_slug).exists():
        new_slug = "{slug}-{num}".format(
            slug=slug,
            num=numb
        )
        numb += 1
    return new_slug


def parse_full_name(full_name):
    try:
        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[1]
    except:
        first_name = full_name.split(' ')[0]
        last_name = ""
    return first_name, last_name
    
    
def process_email_address(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    match = re.match(pattern, email)
    if match:
        return True, email  # Valid, Email
    return False, None


def process_mobile_number(number):
    print(phonenumbers.parse(number))
    try:
        mobile = phonenumbers.parse(number)
        if phonenumbers.is_possible_number(mobile) and phonenumbers.is_valid_number(mobile):
            formatted_mobile = phonenumbers.format_number(mobile, phonenumbers.PhoneNumberFormat.E164)
            return True, formatted_mobile
    except:
        return False, None


def process_local_mobile_number(mobile):
    pattern = r"^(0|234|\+234)+[01789]........."
    match = re.match(pattern, mobile)
    if match:
        if mobile[0] == '0' and len(mobile) == 11:
            mobile_num = '234' + mobile[1:]
        elif len(mobile) == 10:
            mobile_num = '234' + mobile
        elif mobile[0:4] == '+234' and len(mobile) == 14:
            mobile_num = mobile[1:]

        elif mobile[0:3] == '234' and len(mobile) == 13:
            mobile_num = mobile
        else:
            return False, None  # Valid, Number
        return True, mobile_num  # Valid, Number
    return False, None  # Valid, Number


def unique_mobile_number_generator(Klass):
    mobile = "23400" + random_int_generator(size=8)
    while Klass.objects.filter(mobile=mobile).exists():
        mobile = "23400" + random_int_generator(size=8)
    return mobile


def base64_to_file(image_ext, image_b64):
    img_data = base64.b64decode(image_b64)
    buffer = BytesIO(img_data)
    image = Image.open(buffer)
    image.save(buffer, image_ext)
    image_content = ContentFile(buffer.getvalue())
    return image_content
