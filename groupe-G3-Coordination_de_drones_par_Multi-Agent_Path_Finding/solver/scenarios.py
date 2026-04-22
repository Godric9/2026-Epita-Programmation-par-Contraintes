"""
Each scenario returns a dict with:
  grid_config: dict passed to Grid(**grid_config)
  drones: list of {id, start, goal}
  nofly: list of {min, max} bounding boxes (optional)
  buildings: list of {row, col, height} (optional, 3D only)
  description: str
"""
from typing import Dict, Any

SCENARIOS: Dict[str, Any] = {
    "small_2d": {
        "description": "8×8 grid, 5 drones — validation scenario",
        "grid_config": {"rows": 8, "cols": 8, "alts": 1},
        "drones": [
            {"id": 0, "start": [0, 0], "goal": [7, 7]},
            {"id": 1, "start": [7, 0], "goal": [0, 7]},
            {"id": 2, "start": [0, 7], "goal": [7, 0]},
            {"id": 3, "start": [3, 0], "goal": [3, 7]},
            {"id": 4, "start": [0, 3], "goal": [7, 3]},
        ],
        "nofly": [],
        "buildings": [],
    },
    "city_2d": {
        "description": "16×16 grid, 10 drones — main 2D demo",
        "grid_config": {"rows": 16, "cols": 16, "alts": 1},
        "drones": [
            {"id": 0,  "start": [0,  0],  "goal": [15, 15]},
            {"id": 1,  "start": [15, 0],  "goal": [0,  15]},
            {"id": 2,  "start": [0,  15], "goal": [15, 0]},
            {"id": 3,  "start": [15, 15], "goal": [0,  0]},
            {"id": 4,  "start": [0,  7],  "goal": [15, 8]},
            {"id": 5,  "start": [15, 8],  "goal": [0,  7]},
            {"id": 6,  "start": [7,  0],  "goal": [8,  15]},
            {"id": 7,  "start": [8,  15], "goal": [7,  0]},
            {"id": 8,  "start": [3,  3],  "goal": [12, 12]},
            {"id": 9,  "start": [12, 12], "goal": [3,  3]},
        ],
        "nofly": [],
        "buildings": [],
    },
    "city_3d": {
        "description": "16×16×5 city, 10 drones — main 3D demo",
        "grid_config": {"rows": 16, "cols": 16, "alts": 5},
        "drones": [
            {"id": 0,  "start": [0,  0,  0], "goal": [15, 15, 4]},
            {"id": 1,  "start": [15, 0,  0], "goal": [0,  15, 3]},
            {"id": 2,  "start": [0,  15, 1], "goal": [15, 0,  2]},
            {"id": 3,  "start": [15, 15, 2], "goal": [0,  0,  1]},
            {"id": 4,  "start": [0,  7,  0], "goal": [15, 8,  4]},
            {"id": 5,  "start": [15, 8,  0], "goal": [0,  7,  3]},
            {"id": 6,  "start": [7,  0,  0], "goal": [8,  15, 2]},
            {"id": 7,  "start": [8,  15, 0], "goal": [7,  0,  4]},
            {"id": 8,  "start": [3,  3,  0], "goal": [12, 12, 3]},
            {"id": 9,  "start": [12, 12, 0], "goal": [3,  3,  4]},
        ],
        "nofly": [],
        "buildings": [
            {"row": 2,  "col": 2,  "height": 3},
            {"row": 2,  "col": 3,  "height": 3},
            {"row": 5,  "col": 5,  "height": 4},
            {"row": 5,  "col": 6,  "height": 4},
            {"row": 9,  "col": 2,  "height": 2},
            {"row": 9,  "col": 9,  "height": 5},
            {"row": 9,  "col": 10, "height": 5},
            {"row": 12, "col": 12, "height": 3},
            {"row": 13, "col": 12, "height": 3},
            {"row": 3,  "col": 13, "height": 4},
        ],
    },
}


def get_scenario(name: str) -> Dict[str, Any]:
    if name not in SCENARIOS:
        raise KeyError(f"Unknown scenario '{name}'. Available: {list(SCENARIOS.keys())}")
    return SCENARIOS[name]


def list_scenarios():
    return [{"name": k, "description": v["description"]} for k, v in SCENARIOS.items()]
