"""Unit tests for the GetProfile use case, with a fake repository."""

from personal_site.application.get_profile import GetProfile
from personal_site.domain.profile import Profile, Skill
from personal_site.infrastructure.in_code_profile_repository import (
    InCodeProfileRepository,
)


class FakeProfileRepository:
    def __init__(self, profile: Profile) -> None:
        self._profile = profile

    def get(self) -> Profile:
        return self._profile


def make_profile(name: str) -> Profile:
    return Profile(
        name=name,
        headline="Headline",
        about=("About",),
        skills=(Skill("Python", 3),),
        education=(),
        interests=(),
        projects=(),
    )


def test_execute_returns_the_profile_of_the_repository() -> None:
    profile = make_profile("Test Person")
    assert GetProfile(FakeProfileRepository(profile)).execute() is profile


def test_in_code_profile_has_the_requested_skills() -> None:
    profile = GetProfile(InCodeProfileRepository()).execute()
    skills = {skill.name: skill.stars for skill in profile.skills}
    assert profile.name == "Jens Tirsvad Nielsen"
    assert skills == {
        "Software architecture": 5,
        "Software SQA and QC": 5,
        "AI for software development": 4,
    }


def test_in_code_profile_mentions_linux_and_ucl_odense() -> None:
    profile = InCodeProfileRepository().get()
    text = " ".join((profile.headline, *profile.about, *profile.interests))
    assert "Linux" in text
    assert "UCL" in text
    assert "Odense" in text
