from app.core.database import Base
import os
print(os.getenv("DATABASE_URL"))

print("📌 ตารางทั้งหมดใน Base.metadata:")
print(Base.metadata.tables.keys())
