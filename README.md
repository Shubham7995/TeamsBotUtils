# Teams Bot Utilities

A package containing utility functions and classes for Teams bot implementations.

## Features

- **Telemetry**: Integration with Mixpanel for tracking bot usage and performance
- **Image Processing**: Utilities for handling and processing images in Teams messages
- **Activity Extensions**: Helper methods for Bot Framework Activity objects
- **HTTP Utilities**: Reusable HTTP client functions

## Installation

```bash
pip install teams_bot_utils
```

Or add it to your project's requirements.txt:

```
teams_bot_utils>=0.1.0
```

## Usage

### Telemetry

```python
from teams_bot_utils.telemetry import BotTelemetry

# Initialize with your Mixpanel token
telemetry = BotTelemetry("your-mixpanel-token")

# Track bot installation
telemetry.track_bot_installed(team_id="team123", user_id="user456")

# Track message received
telemetry.track_message_received(
    user_id="user456",
    session_id="session789",
    has_text=True
)
```

### Image Processing

```python
from teams_bot_utils.image import extract_image_from_activity

# Extract and process image from Teams activity
image_base64 = await extract_image_from_activity(context.activity.attachments)
```

### Activity Extensions

```python
from teams_bot_utils.activity import extend_activity_class

# Extend the Activity class with helper methods
extend_activity_class()

# Now you can use the helper methods directly on Activity objects
has_text, file_count, image_count, extensions = activity.check_message_contents()
```

## Contributing

1. Clone the repository
2. Create a new feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License