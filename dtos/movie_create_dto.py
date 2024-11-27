from pydantic import BaseModel, Field

class MovieCreateDto(BaseModel):
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1,le=10)
    category: str = Field(min_length=3, max_length=10)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2021,
                "rating": 9.8,
                "category": "Acción",
            }
            
        }
    }
    