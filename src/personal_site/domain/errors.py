"""Errors raised by the domain rules.

@file
@brief Domain errors.
"""


class InvalidSkillError(ValueError):
    """A skill breaks a domain rule.

    @brief Raised when a skill has an empty name or a rating out of range.
    """
