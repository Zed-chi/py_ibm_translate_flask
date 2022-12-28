""" translator module """

import translators.server as tss


def english_to_french(english_text: str) -> str:
    """translator module"""
    cleaned = english_text.strip()
    return tss.bing(cleaned, "en", "fr")


def french_to_english(french_text: str) -> str:
    """translator module"""
    cleaned = french_text.strip()
    return tss.bing(cleaned, "fr", "en")
