#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
import hashlib

def strength_check(password):
    issues = []
    
    if len(password) < 8:
        issues.append("Password too short (min 8 characters)")
    if not re.search(r"[A-Z]", password):
        issues.append("Missing upperacse letter")
    if not re.search(r"[a-z]", password):
        issues.append("Missing lowercase letter")
    if not re.search(r"[0-9]", password):
        issues.append("Missing number")
    if not re.search(r"[!@#$%^&*]", password):
        issues.append("Missing special characters")
        
    return issues

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = input("Enter a password to review: ")
issues = strength_check(password)

if issues:
    print("\n Weak Password: ")
    for issue in issues:
        print(f"- {issue}")
else:
    print("\n Strong Password")
    
hashed = hash_password(password)
print("\n SHA256 Hash:")
print(hashed)


# In[ ]:




