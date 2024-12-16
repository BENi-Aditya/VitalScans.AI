import numpy as np
from scipy import stats
import json
import random

def generate_pattern(pattern_type):
    if pattern_type == 'spiral':
        t = np.linspace(0, 10, 100)
        x = t * np.cos(t)
        y = t * np.sin(t)
    elif pattern_type == 'wave':
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
    else:  # circle
        t = np.linspace(0, 2*np.pi, 100)
        x = np.cos(t)
        y = np.sin(t)
    
    # Normalize to 0-1 range
    x = (x - np.min(x)) / (np.max(x) - np.min(x))
    y = (y - np.min(y)) / (np.max(y) - np.min(y))
    
    return list(zip(x.tolist(), y.tolist()))

def analyze_tracing(user_path, original_path):
    # Convert paths to numpy arrays
    user_path = np.array(user_path)
    original_path = np.array(original_path)
    
    # Interpolate user_path to match the length of original_path
    t_user = np.linspace(0, 1, len(user_path))
    t_original = np.linspace(0, 1, len(original_path))
    user_path_interp = np.array([np.interp(t_original, t_user, user_path[:, i]) for i in range(2)]).T
    
    # Compute various metrics
    deviation = np.mean(np.sqrt(np.sum((user_path_interp - original_path)**2, axis=1)))
    smoothness = compute_smoothness(user_path)
    speed_consistency = compute_speed_consistency(user_path)
    
    # Adjust metrics for mouse/trackpad use
    deviation *= 0.5  # Reduce the impact of deviation
    smoothness = (smoothness + 1) / 2  # Increase overall smoothness
    speed_consistency = (speed_consistency + 1) / 2  # Increase overall speed consistency
    
    # Simple scoring system (lower is better)
    score = deviation * 40 + (1 - smoothness) * 30 + (1 - speed_consistency) * 30
    
    # Classify risk (adjusted thresholds)
    if score < 30:
        risk = "Low"
    elif score < 50:
        risk = "Medium"
    else:
        risk = "High"
    
    return {
        "deviation": float(deviation),
        "smoothness": float(smoothness),
        "speed_consistency": float(speed_consistency),
        "score": float(score),
        "risk": risk
    }

def compute_smoothness(path):
    # Compute the second derivative (acceleration) of the path
    acceleration = np.diff(path, n=2, axis=0)
    jerk = np.sum(np.sqrt(np.sum(acceleration**2, axis=1)))
    return 1 / (1 + jerk * 0.1)  # Reduced impact of jerk

def compute_speed_consistency(path):
    # Compute speeds between consecutive points
    speeds = np.sqrt(np.sum(np.diff(path, axis=0)**2, axis=1))
    # Use coefficient of variation as a measure of consistency
    return 1 - (np.std(speeds) / (np.mean(speeds) + 1e-6))  # Added small constant to avoid division by zero

def get_random_pattern():
    pattern_types = ['spiral', 'wave', 'circle']
    return generate_pattern(random.choice(pattern_types))

# Example usage
if __name__ == "__main__":
    original_path = generate_pattern('spiral')
    user_path = [(x + random.uniform(-0.05, 0.05), y + random.uniform(-0.05, 0.05)) for x, y in original_path]
    
    result = analyze_tracing(user_path, original_path)
    print(json.dumps(result, indent=2))