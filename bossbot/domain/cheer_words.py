from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import mapped_column

from bossbot.domain.base import Base


class CheerWords(Base):
    __tablename__ = "cheer_words"

    id = mapped_column(Integer, primary_key=True)
    author_id = mapped_column(Integer, ForeignKey("member.id"))
    word = mapped_column(String(250), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)
    updated_at = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self) -> str:
        return f"CheerWords: {self.word}"
