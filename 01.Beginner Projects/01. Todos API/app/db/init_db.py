from app.db.database import Base, engine
from app.models import todo  # noqa: F401 - Import all models so Base knows them

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
