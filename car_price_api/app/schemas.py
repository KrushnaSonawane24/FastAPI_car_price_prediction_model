from pydantic import (BaseModel, Field, AnyUrl,StrictFloat,EmailStr,
field_validator,# ye sirf ek hi field pe kaaam karta hai 
model_validator ,computed_field) #if you want to give multiple field so use model_validator
from typing import Optional, List
from enum import Enum
from typing_extensions import Literal,Annotated

from datetime import datetime

class FuleType(str,Enum):
    petrol="Petrol"
    diesel = "Diesel"
    cng="CNG"


class  SellerType(str,Enum):
    dealer="Dealer"
    individual="Individual"


class TransmissionType(str,Enum):
    automatic="Automatic"
    manual="Manual"


class CarFeatures(BaseModel):
    Car_Name: str = Field(..., example="ciaz")

    Year: int = Field(..., example=2017)

    Selling_Price: StrictFloat = Field(...,example=4.56)

    Present_Price: StrictFloat = Field(...,example=5.34)

    Kms_Driven: int = Field(...,example=270000)

    Fuel_Type: FuleType

    Seller_Type:SellerType

    Transmission: TransmissionType = Field(default="Manual",description="Manual and Automatic")

    Owner: int = Field(...,ge=0,le=3,example=0,description="Number of Previous owners")

class predictionResponse(BaseModel):
    prediction_price:StrictFloat