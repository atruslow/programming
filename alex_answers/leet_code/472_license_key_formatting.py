from typing import List


def license_key_formatting(s: str, k: int) -> str:

    sections = []
    s = s.replace("-", "").upper()
    overflow = len(s) % k or k

    first_section, rest = s[:overflow], s[overflow:]
    sections.append(first_section)

    while rest:

        section, rest = rest[:k], rest[k:]

        sections.append(section)

    return "-".join(sections)


def test_example_one():

    assert license_key_formatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"


def test_example_two():

    assert license_key_formatting("2-5g-3-J", 2) == "2-5G-3J"
