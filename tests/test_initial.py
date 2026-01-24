# --- 1️⃣ Test top-level import ---
def test_top_level_import():
    import pyuikit


# --- 2️⃣ Test components import ---
def test_components_importable():
    from pyuikit import Body, Div
    from pyuikit.components import Text, Button, Input

    # Simple assertions to make sure they exist
    assert Body is not None
    assert Div is not None
    assert Text is not None
    assert Button is not None
    assert Input is not None