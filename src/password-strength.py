import re

def is_strong_password(password):

   # Check for minimum length
   if len(password) < 8:
    return False

   # Check for uppercase letter
   if not re.search(r"[A-Z]", password):
    return False

   # Check for number
   if not re.search(r"[0-9]", password):
    return False

   return True

