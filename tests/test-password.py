from src.password import is_strong_password

def test_strong_password():
   assert is_strong_password("Secure123")

def test_short_password():
   assert not is_strong_password("abc")

def test_no_number():
   assert not is_strong_password("Password")

def test_no_uppercase():
   assert not is_strong_password("password123")