from sqlalchemy import Integer, String
from sqlalchemy import mapped_column

from bossbot.domain.base import Base


class Member(Base):
    __tablename__ = "member"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(255), nullable=False)

    def __str__(self) -> str:
        return f"User: {self.username}"
