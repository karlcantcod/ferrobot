






# This module initializes the Leopard speech-to-text engine.
# It wraps the creation of a Leopard instance using the provided access key,
# allowing for voice-to-text conversion in the virtual assistant application.



# leopard.py
from pvleopard import create
from config import PV_ACCESS_KEY

def init_leopard():
    """
    Initializes and returns a Leopard instance.
    """
    leopard_instance = create(
        access_key=PV_ACCESS_KEY,
        enable_automatic_punctuation=True,
    )
    return leopard_instance
