from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()


# Pydantic models for request/response validation
class Property(BaseModel):
    id: int
    address: str
    city: str
    state: str
    zip_code: str
    price: float
    bedrooms: int
    bathrooms: float
    square_feet: int
    property_type: str
    year_built: int


# Sample data
SAMPLE_PROPERTIES = [
    {
        "id": 1,
        "address": "123 Main Street",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94102",
        "price": 850000.00,
        "bedrooms": 3,
        "bathrooms": 2.0,
        "square_feet": 1800,
        "property_type": "Single Family",
        "year_built": 1950
    },
    {
        "id": 2,
        "address": "456 Oak Avenue",
        "city": "Austin",
        "state": "TX",
        "zip_code": "78701",
        "price": 425000.00,
        "bedrooms": 2,
        "bathrooms": 1.5,
        "square_feet": 1200,
        "property_type": "Condo",
        "year_built": 2010
    },
    {
        "id": 3,
        "address": "789 Pine Road",
        "city": "Denver",
        "state": "CO",
        "zip_code": "80202",
        "price": 625000.00,
        "bedrooms": 4,
        "bathrooms": 3.0,
        "square_feet": 2400,
        "property_type": "Townhouse",
        "year_built": 2005
    }
]


@router.get("/properties", response_model=List[Property])
def get_properties():
    """
    Get a list of all properties.
    Returns sample property data for demonstration.
    """
    return SAMPLE_PROPERTIES


@router.get("/properties/{property_id}", response_model=Property)
def get_property(property_id: int):
    """
    Get a single property by ID.
    """
    property = next((p for p in SAMPLE_PROPERTIES if p["id"] == property_id), None)
    if not property:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Property not found")
    return property

