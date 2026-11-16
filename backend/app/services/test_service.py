from app.api.schemas.test_schemas import TestCreate, TestReturn
from app.utils.unitofwork import IUnitOfWork, UnitOfWork

class TestService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def create_test(self, test_data: TestCreate) -> dict:
        async with self.uow:
            new_test = await self.uow.tests.add_one({"text": test_data.text})
            test_id = new_test.id 
            await self.uow.commit()
            
            return {"message": "Test успешно создан", "id": test_id}

    async def get_all_tests(self) -> list[TestReturn]:
        async with self.uow:
            tests = await self.uow.tests.find_all()
            return [TestReturn.model_validate(t) for t in tests]