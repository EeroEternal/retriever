from fastapi import APIRouter, Depends

from retriever.config.tools import AVAILABLE_TOOLS
from retriever.models import get_session
from retriever.schemas.tool import ManagedTool
from retriever.services.request_validators import validate_user_header

router = APIRouter(
    prefix="/tools", dependencies=[Depends(get_session), Depends(validate_user_header)]
)


@router.get("/", response_model=list[ManagedTool])
def list_tools() -> list[ManagedTool]:
    """
    List all available tools.

    Returns:
        list[Tool]: List of available tools.
    """
    return AVAILABLE_TOOLS.values()
