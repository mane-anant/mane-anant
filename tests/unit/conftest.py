import pytest
from users import app


@pytest.fixture
def fixture_client():
    """Create an api test client fixture."""
    # import pdb; pdb.set_trace()
    return app.app.test_client()
