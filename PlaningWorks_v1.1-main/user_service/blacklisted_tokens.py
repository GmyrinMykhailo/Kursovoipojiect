from typing import Set

blacklisted_tokens: Set[str] = set()


def blacklist_token(token: str):
    blacklisted_tokens.add(token)


def is_token_blacklisted(token: str) -> bool:
    return token in blacklisted_tokens