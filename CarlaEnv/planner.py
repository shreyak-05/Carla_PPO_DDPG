import numpy as np

# ==============================================================================
# -- import route planning (copied and modified from CARLA 0.9.4's PythonAPI) --
# ==============================================================================
import carla
from agents.navigation.local_planner import RoadOption
from agents.navigation.global_route_planner import GlobalRoutePlanner
from agents.navigation.global_route_planner_dao import GlobalRoutePlannerDAO
from agents.tools.misc import vector
 

def compute_route_waypoints(map, start_waypoint, end_waypoint, resolution=5.0, plan=None, max_steps=2000):
    current_waypoint = start_waypoint
    route = []
    steps = 0

    if plan is None:
        plan = [RoadOption.LANEFOLLOW]
        # raise ValueError("A maneuver plan must be provided. Example: [RoadOption.STRAIGHT]*3 + [RoadOption.RIGHT]")

    for maneuver in plan:
        next_wps = current_waypoint.next(resolution)
        if not next_wps:
            break
        current_waypoint = next_wps[0]
        route.append((current_waypoint, maneuver))
        steps += 1
        if steps >= max_steps:
            print("Max steps reached during route planning")
            break

    return route
