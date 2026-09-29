"""Google Maps Platform tools for Geocoding and Places API (New)."""

import os
from typing import Any, Dict, List, Optional
import requests
from dotenv import load_dotenv

# Load variables from .env if present
load_dotenv()


def _get_api_key() -> str:
    key = os.environ.get("GOOGLE_MAPS_API_KEY", "").strip()
    if not key or key == "PASTE_KEY_HERE":
        raise ValueError(
            "GOOGLE_MAPS_API_KEY is not set or contains placeholder. Please set a valid key in your .env file."
        )
    return key


def geocode_address(address: str) -> Dict[str, Any]:
    """Converts a street address, city, or location description into geographic latitude and longitude coordinates.

    Uses the Google Maps Geocoding REST API directly.

    Args:
        address: The address or place to geocode (e.g. '1600 Amphitheatre Pkwy, Mountain View, CA' or 'Berlin Alexanderplatz').

    Returns:
        A dictionary with formatted address, latitude, longitude, and place_id.
    """
    try:
        api_key = _get_api_key()
    except ValueError as e:
        return {"status": "error", "error": str(e)}

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        status = data.get("status")
        if status != "OK":
            return {
                "status": "error",
                "api_status": status,
                "error": data.get("error_message", f"Geocoding failed with status: {status}"),
            }

        first_result = data["results"][0]
        location = first_result.get("geometry", {}).get("location", {})

        return {
            "status": "success",
            "name": first_result.get("formatted_address"),
            "formatted_address": first_result.get("formatted_address"),
            "location": {
                "latitude": location.get("lat"),
                "longitude": location.get("lng"),
            },
            "place_id": first_result.get("place_id"),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def search_nearby_places(
    latitude: float,
    longitude: float,
    place_type: str = "gym",
    radius_meters: float = 1500.0,
    max_results: int = 5,
) -> Dict[str, Any]:
    """Finds nearby places of a specific type (e.g. 'gym', 'fitness_center', 'park', 'athletic_field') using the Places API (New).

    Uses the HTTP POST endpoint https://places.googleapis.com/v1/places:searchNearby with X-Goog-FieldMask.

    Args:
        latitude: Latitude of the center point.
        longitude: Longitude of the center point.
        place_type: Place type to search for (e.g., 'gym', 'fitness_center', 'park', 'sports_complex').
        radius_meters: Search radius in meters (max 50000.0, default 1500.0).
        max_results: Max items to return (1-20, default 5).

    Returns:
        A dictionary with matching places containing name, address, and coordinates.
    """
    try:
        api_key = _get_api_key()
    except ValueError as e:
        return {"status": "error", "error": str(e)}

    url = "https://places.googleapis.com/v1/places:searchNearby"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location,places.types,places.id",
    }
    payload = {
        "includedTypes": [place_type],
        "maxResultCount": min(max(max_results, 1), 20),
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": float(latitude),
                    "longitude": float(longitude),
                },
                "radius": float(radius_meters),
            }
        },
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        places_data: List[Dict[str, Any]] = []
        for p in data.get("places", []):
            display_name = p.get("displayName", {}).get("text", "Unknown Place")
            formatted_address = p.get("formattedAddress", "")
            loc = p.get("location", {})
            places_data.append({
                "name": display_name,
                "address": formatted_address,
                "location": {
                    "latitude": loc.get("latitude"),
                    "longitude": loc.get("longitude"),
                },
                "place_id": p.get("id"),
                "types": p.get("types", []),
            })

        return {
            "status": "success",
            "count": len(places_data),
            "places": places_data,
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
