from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_requirements(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leadership_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        has_leadership = any(
            member.rank in leadership_ranks for member in self.crew
        )
        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                member.years_experience >= 5 for member in self.crew
            )
            if experienced_count / len(self.crew) < 0.5:
                error_message = (
                    "Long missions require at least 50% experienced crew "
                    "(5+ years)"
                )
                raise ValueError(error_message)

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-05-01T08:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=41,
                specialization="Mission Command",
                years_experience=16,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=34,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=5,
            ),
        ],
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
        )

    print("\n", "=" * 41)
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2026_LUNA",
            mission_name="Lunar Supply Relay",
            destination="Moon",
            launch_date="2026-06-10T10:30:00",
            duration_days=120,
            budget_millions=300.0,
            crew=[
                CrewMember(
                    member_id="C101",
                    name="Emma Reed",
                    rank=Rank.LIEUTENANT,
                    age=32,
                    specialization="Navigation",
                    years_experience=7,
                ),
                CrewMember(
                    member_id="C102",
                    name="Noah Blake",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Engineering",
                    years_experience=4,
                ),
            ],
        )
    except ValidationError as error:
        first_error = error.errors()[0]
        clean_message = str(
            first_error.get("ctx", {}).get("error", first_error["msg"])
        )
        print(clean_message)


if __name__ == "__main__":
    main()
