from designer.designer import DESIGNER
from painter.painter import PAINTER

# Comment out respective above and below to disable an app.

apps = [
    PAINTER,
    DESIGNER,
]

# Random test
[print(app.name) for app in apps]
