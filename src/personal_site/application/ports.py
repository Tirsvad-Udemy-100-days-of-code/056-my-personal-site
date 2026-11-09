"""Ports: what the use cases need from the outside world.

@file
@brief Interfaces implemented by the infrastructure layer.
"""

from typing import Protocol

from personal_site.domain.profile import Profile


class ProfileRepository(Protocol):
    """Source of the profile.

    @brief Port that returns the profile shown on the CV site.
    """

    def get(self) -> Profile:
        """Return the profile.

        @return The profile of the site owner.
        """
        ...
