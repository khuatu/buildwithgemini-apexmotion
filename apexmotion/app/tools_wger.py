"""Tool for fetching public exercise data from the open-source wger database."""

import os
import re
from typing import Any, Dict, List, Optional
import requests

WGER_BASE_URL = "https://wger.de/api/v2"

CATEGORY_MAP = {
    "abs": 10,
    "core": 10,
    "arms": 8,
    "biceps": 8,
    "triceps": 8,
    "back": 12,
    "lats": 12,
    "pull": 12,
    "calves": 14,
    "cardio": 15,
    "chest": 11,
    "push": 11,
    "legs": 9,
    "quads": 9,
    "hamstrings": 9,
    "shoulders": 13,
    "delts": 13,
}


def search_public_exercises(
    category: Optional[str] = None,
    limit: int = 5,
) -> Dict[str, Any]:
    """Queries the free public wger Exercise Database (from the GitHub public-apis directory).

    Fetches real-world exercise variations, anatomical target muscles, and movement descriptions.

    Args:
        category: Optional category filter. One of: 'abs', 'arms', 'back', 'calves', 'cardio', 'chest', 'legs', 'shoulders'.
        limit: Maximum number of exercises to retrieve (default: 5).

    Returns:
        A dictionary with the list of matching public exercises and their details.
    """
    api_key = os.environ.get("WGER_API_KEY")
    headers = {"Accept": "application/json"}
    if api_key:
        headers["Authorization"] = f"Token {api_key}"

    params = {"limit": min(limit, 20)}
    if category and category.lower() in CATEGORY_MAP:
        params["category"] = CATEGORY_MAP[category.lower()]

    try:
        response = requests.get(
            f"{WGER_BASE_URL}/exerciseinfo/",
            params=params,
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        clean_results: List[Dict[str, Any]] = []
        for item in data.get("results", []):
            # Extract English translation if available, or first translation
            trans_list = item.get("translations", [])
            selected_trans = next((t for t in trans_list if t.get("language") == 2), None)
            if not selected_trans and trans_list:
                selected_trans = trans_list[0]

            name = selected_trans.get("name", "Unknown Exercise") if selected_trans else "Unknown Exercise"
            raw_desc = selected_trans.get("description", "") if selected_trans else ""
            clean_desc = re.sub(r"<[^<]+?>", "", raw_desc).strip()

            muscles = [
                m.get("name_en") or m.get("name")
                for m in item.get("muscles", [])
                if m.get("name_en") or m.get("name")
            ]
            secondary_muscles = [
                m.get("name_en") or m.get("name")
                for m in item.get("muscles_secondary", [])
                if m.get("name_en") or m.get("name")
            ]
            cat_name = item.get("category", {}).get("name", "General")

            clean_results.append({
                "id": item.get("id"),
                "name": name,
                "category": cat_name,
                "target_muscles": muscles,
                "secondary_muscles": secondary_muscles,
                "description": clean_desc[:250] + ("..." if len(clean_desc) > 250 else ""),
            })

        return {
            "status": "success",
            "source": "wger Public Exercise API",
            "count": len(clean_results),
            "exercises": clean_results,
        }
    except Exception as e:
        return {
            "status": "error",
            "source": "wger Public Exercise API",
            "error": str(e),
        }
