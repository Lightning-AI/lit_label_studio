r"""To test a lightning component:

1. Init the component.
2. call .run()
"""
from lit_label_studio.component import LitLabelStudio


def test_placeholder_component():
    app = LitLabelStudio()
    app.run()
