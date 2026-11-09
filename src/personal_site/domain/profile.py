"""Entities of the personal CV: the profile and its parts.

@file
@brief Frozen dataclasses that describe a person on the CV site.
"""

from dataclasses import dataclass

from personal_site.constants import MAX_STARS, MIN_STARS
from personal_site.domain.errors import InvalidSkillError


@dataclass(frozen=True)
class Skill:
    """A skill with a star rating.

    @brief One row of the skills table.
    """

    name: str
    stars: int

    def __post_init__(self) -> None:
        """Check the rules of a skill.

        @brief Reject an empty name and a rating outside MIN_STARS..MAX_STARS.
        @throws InvalidSkillError when a rule is broken.
        """
        if not self.name.strip():
            raise InvalidSkillError("A skill needs a name.")
        if not MIN_STARS <= self.stars <= MAX_STARS:
            raise InvalidSkillError(
                f"Stars must be between {MIN_STARS} and {MAX_STARS}, "
                f"got {self.stars}."
            )


@dataclass(frozen=True)
class Education:
    """A programme of study.

    @brief One row of the education section.
    """

    programme: str
    school: str
    focus: str


@dataclass(frozen=True)
class Project:
    """A project the person works on.

    @brief One row of the projects section.
    """

    name: str
    description: str


@dataclass(frozen=True)
class Profile:
    """Everything the CV site shows about a person.

    @brief The aggregate rendered by the home page.
    """

    name: str
    headline: str
    about: tuple[str, ...]
    skills: tuple[Skill, ...]
    education: tuple[Education, ...]
    interests: tuple[str, ...]
    projects: tuple[Project, ...]
