from fastapi import APIRouter, Depends
from app.api.schemas.test_schemas import TestCreate, TestReturn
from app.services.test_service import TestService
from app.utils.unitofwork import UnitOfWork

router = APIRouter(prefix="/tests", tags=["Tests"])

def get_test_service() -> TestService:
    return TestService(UnitOfWork())

@router.post("/")
async def create_test(test: TestCreate, service: TestService = Depends(get_test_service)):
    return await service.create_test(test)

@router.get("/", response_model=list[TestReturn])
async def get_tests(service: TestService = Depends(get_test_service)):
    return await service.get_all_tests()