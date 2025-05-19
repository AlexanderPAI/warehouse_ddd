from fastapi import APIRouter

router = APIRouter(
    prefix="/customer",
    tags=["Customer"],
)


@router.post(path="/", summary="Create customer")
async def create_customer():
    """Create customer"""
    pass


@router.get(path="/", summary="Get customer by id or name")
async def get_customer():
    """Get customer by id or name"""
    pass
