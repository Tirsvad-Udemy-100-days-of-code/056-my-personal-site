"""Use case: get the profile for the CV site.

@file
@brief The GetProfile use case.
"""

from personal_site.application.ports import ProfileRepository
from personal_site.domain.profile import Profile


class GetProfile:
    """Return the profile of the site owner.

    @brief Use case called by the presentation layer.
    """

    def __init__(self, repository: ProfileRepository) -> None:
        """Create the use case.

        @param repository The source of the profile.
        """
        self._repository = repository

    def execute(self) -> Profile:
        """Run the use case.

        @return The profile to show.
        """
        return self._repository.get()
