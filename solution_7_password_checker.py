# 8. Password Strength Checker

# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


password = "12gdagsjxxzz"

password_len = len(password)

if password_len < 6:
    strenth = "week"
    
elif password_len <= 10:
    strenth = "Medium"

else:
    strenth = "strong"
    
print(strenth)
