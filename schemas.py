from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
    """Inbound lead from the website's contact form.
    Collection name inferred as "inquiry".
    """
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    service: str = Field(..., description="Requested service type")
    message: Optional[str] = Field(None, max_length=4000)

# You can keep or extend more schemas as needed for future features
