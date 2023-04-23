from typing import Tuple, Dict


def validate_email_addr(email_addr: str) -> bool:
    """
    Returns True if the email_addr is valid per specification. Otherwise, return False.
    """
    # Total length of email too long.
    if len(email_addr.strip()) > 254:
        return False
    
    # No domain!
    if email_addr.count('@') != 1:
        return False
    
    # Total length of email before @ too long.
    if len(email_addr.strip().split('@')[0]) > 64:
        return False
    
    # Total length of email after @ too long.
    if len(email_addr.strip().split('@')[1]) > 251:
        return False


    for c in email_addr:
        if not c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.-':
            return False
    
    first_part = email_addr.strip().split('@')[0]
    second_part = email_addr.strip().split('@')[1]
    
    if '-' in [first_part[0], first_part[-1]]:
        return False
    
    if '.' in [first_part[0], first_part[-1]]:
        return False
    
    if second_part not in ['com', 'net', 'org']:
        return False

    return True


def validate_email_payload(sender_name: str, sender_addr: str, receiver_name: str, receiver_addr: str, html: str,
                           replacements: Dict) -> bool:
    """
    Returns True if the payload is validated and is safe to send out. Otherwise, return False.
    """
    if (len(sender_name.strip()) < 5) or (len(sender_name.strip()) > 30):
        raise ValueError

    if (len(receiver_name.strip()) < 5) or (len(receiver_name.strip()) > 60):
        raise ValueError

    if (not validate_email_addr(sender_addr)):
        raise ValueError

    if (not validate_email_addr(receiver_addr)):
        raise ValueError
    
    for key in replacements:
        if ('{' + f'{key}' + '}') not in html:
            raise ValueError

    return True
