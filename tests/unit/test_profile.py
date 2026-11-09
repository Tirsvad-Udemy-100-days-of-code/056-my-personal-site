"""Unit tests for the profile entities."""

import dataclasses

import pytest

from personal_site.constants import MAX_STARS, MIN_STARS
from personal_site.domain.errors import InvalidSkillError
from personal_site.domain.profile import Skill


def test_skill_accepts_the_lowest_and_highest_rating() -> None:
    assert Skill("Python", MIN_STARS).stars == MIN_STARS
    assert Skill("Python", MAX_STARS).stars == MAX_STARS


@pytest.mark.parametrize("stars", [MIN_STARS - 1, MAX_STARS + 1])
def test_skill_rejects_a_rating_out_of_range(stars: int) -> None:
    with pytest.raises(InvalidSkillError):
        Skill("Python", stars)


def test_skill_rejects_a_blank_name() -> None:
    with pytest.raises(InvalidSkillError):
        Skill("   ", 3)


def test_skill_is_immutable() -> None:
    skill = Skill("Python", 3)
    with pytest.raises(dataclasses.FrozenInstanceError):
        skill.stars = 5  # type: ignore[misc]
