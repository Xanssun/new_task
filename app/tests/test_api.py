import httpx
import pytest
from schemas.app_schemas import ApplicationCreate


@pytest.mark.parametrize(
    "application_data, expected_status",
    [
        (
            ApplicationCreate(
                user_name = "one_test_user",
                description = "some description"
            ),
            201
        ),
        (
            ApplicationCreate(
                user_name = "two_test_user",
                description = "some description"
            ),
            201
        ),
        (
            ApplicationCreate(
                user_name = "thee_test_user",
                description = "some description"
            ),
            201
        )
    ]
)
@pytest.mark.asyncio
async def test_create_applications(application_data, expected_status):
    
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.post("/api/v1/applications", json=application_data.model_dump())
    
    assert response.status_code == expected_status


@pytest.mark.asyncio
async def test_get_applications():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.get("/api/v1/applications")
    
    assert response.status_code == 200
    assert len(response.json()["applications"]) > 0
