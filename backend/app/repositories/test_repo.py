from app.db.models.test import Test
from app.repositories.basic_repo import Repository

class TestRepository(Repository):
    model = Test
