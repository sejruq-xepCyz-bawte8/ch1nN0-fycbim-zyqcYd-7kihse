import anvil.users
import anvil.secrets
import hmac
import hashlib
import base64

secret_key = anvil.secrets.get_secret("IDHMAC").encode('utf-8')


def generate_id(item_info):
    # Convert item information to bytes
    item_info_bytes = item_info.encode('utf-8')
    # Create HMAC using SHA-256
    hmac_gen = hmac.new(secret_key, item_info_bytes, hashlib.sha256)
    # Get the HMAC digest
    digest = hmac_gen.digest()
    # Encode the item info and HMAC for safe transmission
    encoded_id = base64.urlsafe_b64encode(item_info_bytes + digest).decode('utf-8')
    return encoded_id

def verify_id(encoded_id):
    # Decode the ID
    id_bytes = base64.urlsafe_b64decode(encoded_id)
    # Separate the original item info and the HMAC
    original_info = id_bytes[:-32]  # SHA-256 HMAC size is 32 bytes
    original_hmac = id_bytes[-32:]
    # Recompute the HMAC
    hmac_gen = hmac.new(secret_key, original_info, hashlib.sha256)
    recomputed_hmac = hmac_gen.digest()
    # Compare the HMACs to verify
    return hmac.compare_digest(original_hmac, recomputed_hmac)

