import re
def vunerable_redirect(user_url):

    # CRITICAL FLAW: The pattern lacks anchors (^ and $).
    # It only checks if "mycompany.com" exists ANYWHERE in the string.
    unsafe_pattern=r"mycompany\.com"
    if re.match(unsafe_pattern,user_url):
        return f"redirecting to {user_url}"
    return "Access denied"
# ==========================================
# 2. THE SECURE CODE (How you remediate it)
# ==========================================

def secure_redirect(user_url):
    # REMEDIATION: Strict allow-listing using anchors and explicit boundaries.
    # Enforces that the URL MUST start with https:// and end with ://mycompany.com
    secure_pattern=r"https://mycompany\.com(/[a-zA-Z0-9_-]*)*$"

    if re.match(secure_pattern,user_url):
        return f"Redirecting saftely to{user_url}"
    return " access denied: untrusted url dtected"

#demonstration payload
attack_url="https://evil-attacker.com"
print("vulnerable sys output")
print(vunerable_redirect(attack_url))

print("\n safe output")
print(secure_redirect(attack_url))