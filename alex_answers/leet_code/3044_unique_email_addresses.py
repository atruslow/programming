from typing import List


def num_unique_emails(emails: List[str]) -> int:

    return len(set(map(_parse_email, emails)))


def _parse_email(email):

    local_name, domain = email.split("@")

    local_name = local_name.replace(".", "").split("+")[0]

    return f"{local_name}@{domain}"


def test_example_one():
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    assert num_unique_emails(emails) == 2


def test_example_two():
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]

    assert num_unique_emails(emails) == 3