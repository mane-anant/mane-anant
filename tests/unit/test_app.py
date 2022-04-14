
from users import app


def test_app():
    """Just checking the app was fully created."""
    # import pdb; pdb.set_trace()
    assert app.app
