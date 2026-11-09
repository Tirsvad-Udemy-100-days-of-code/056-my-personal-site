"""Profile data of the site owner, kept in code.

@file
@brief Adapter that implements ProfileRepository with fixed data.
"""

from personal_site.domain.profile import Education, Profile, Project, Skill


class InCodeProfileRepository:
    """Holds the profile as Python data.

    @brief Implements the ProfileRepository port without a database.
    """

    def get(self) -> Profile:
        """Return the profile of Jens Tirsvad Nielsen.

        @return The profile.
        """
        return Profile(
            name="Jens Tirsvad Nielsen",
            headline="Datamatiker student at UCL, Odense · Linux fan",
            about=(
                "I am a Datamatiker student (AP Graduate in Computer Science) "
                "at UCL in Odense, Denmark.",
                "I am a Linux fan, and I care about how software is structured, "
                "tested and reviewed.",
                "I am learning to build web applications with Python and Flask "
                "in the 100 Days of Code bootcamp, and I use AI as a tool in "
                "software development.",
            ),
            skills=(
                Skill("Software architecture", 5),
                Skill("Software SQA and QC", 5),
                Skill("AI for software development", 4),
            ),
            education=(
                Education(
                    programme="Datamatiker (AP Graduate in Computer Science)",
                    school="UCL Erhvervsakademi og Professionshøjskole, Odense",
                    focus="Software development, databases, system design and "
                    "web development",
                ),
            ),
            interests=(
                "Linux and open source",
                "Software architecture",
                "Quality assurance: SQA and QC",
                "AI-assisted software development",
            ),
            projects=(
                Project(
                    "100 Days of Code",
                    "The Udemy Python bootcamp. This site is the Day 56 project.",
                ),
                Project(
                    "SQA and QC framework",
                    "Documents are reviewed before code is written; this "
                    "repository follows it.",
                ),
            ),
        )
