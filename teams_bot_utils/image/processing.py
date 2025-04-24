"""
Image processing utilities for Teams bots
"""

from botbuilder.schema import Attachment
import httpx
import base64
import logging
from typing import List, Optional

from ..utils.connection_pool import get_http_client


async def download_and_encode_image(url: str) -> str:
    """
    Download an image from a URL and encode it as base64

    Args:
        url (str): The URL of the image

    Returns:
        str: Base64 encoded image data or empty string on failure
    """
    try:
        # Get client from shared pool instead of creating a new one each time
        client = await get_http_client(timeout=30.0, client_id="image_processing")

        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()

        image_data = base64.b64encode(response.content).decode("utf-8")
        logging.info(
            f"Successfully downloaded and encoded image ({len(image_data)} bytes)"
        )

        return image_data

    except httpx.HTTPError as e:
        logging.error(f"HTTP error downloading image: {str(e)}")
    except Exception as e:
        logging.error(f"Error downloading image: {str(e)}")

    return ""


async def process_image_attachment(attachment: Attachment) -> str:
    """
    Process an image attachment from Teams and prepare it for the API

    Args:
        attachment (Attachment): The Teams attachment

    Returns:
        str: Base64 encoded image data or empty string on failure
    """
    logging.info(
        f"Processing image attachment: {attachment.content_type}, {attachment.name}"
    )

    image_url = None

    # Handle Teams file download info
    if attachment.content_type == "application/vnd.microsoft.teams.file.download.info":
        if isinstance(attachment.content, dict) and "downloadUrl" in attachment.content:
            image_url = attachment.content["downloadUrl"]
    # Handle direct image content types
    elif attachment.content_type in [
        "image/png",
        "image/jpeg",
        "image/gif",
        "image/webp",
    ]:
        if attachment.content_url:
            image_url = attachment.content_url

    if not image_url:
        logging.warning(f"No valid image URL found in attachment")
        return ""

    # Download and encode the image
    logging.info(f"Downloading image from URL")
    return await download_and_encode_image(image_url)


async def extract_image_from_activity(attachments: List[Attachment]) -> Optional[str]:
    """
    Extract the first image from activity attachments

    Args:
        attachments: List of attachments from the activity

    Returns:
        str: Base64 encoded image data or None if no image found
    """
    if not attachments:
        return None

    for attachment in attachments:
        if hasattr(attachment, "content_type") and (
            attachment.content_type.startswith("image/")
            or attachment.content_type
            == "application/vnd.microsoft.teams.file.download.info"
        ):
            base64_data = await process_image_attachment(attachment)
            if base64_data:
                return base64_data

    return None
