from sqlalchemy import Text, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase):
	created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
	updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

class IdUser(Base):
	__tablename__ = 'id'

	id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	iduser: Mapped[str] = mapped_column(Text)
	