from datetime import datetime

from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import mapped_column

from bossbot.domain.base import Base


class CommuteClock(Base):
    __tablename__ = "commute_time"

    id = mapped_column(Integer, primary_key=True)
    member = mapped_column(ForeignKey("member.id"), nullable=False)
    start_time = mapped_column(DateTime)
    end_time = mapped_column(DateTime)

    def get_formatted_datetime(self) -> str:
        delta = self.end_time - self.start_time
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds // 60) % 60
        seconds = delta.seconds % 60

        time_format = []
        if days > 0:
            time_format.append(f"{days}일")
        if hours > 0:
            time_format.append(f"{hours}시간")
        if minutes > 0:
            time_format.append(f"{minutes}분")
        if seconds > 0:
            time_format.append(f"{seconds}초")

        return " ".join(time_format)

    def clock_on(self) -> None:
        self.start_time = self._get_current_datetime()

    def clock_off(self) -> None:
        self.end_time = self._get_current_datetime()

    @staticmethod
    def _get_current_datetime() -> datetime:
        return datetime.now()

    def __str__(self) -> str:
        return f"CommuteTime: {self.member}, {self.start_time}, {self.end_time}"
