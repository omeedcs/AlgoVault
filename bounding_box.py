import math

class BoundingBox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def center(self):
        return (self.x + self.width / 2, self.y + self.height / 2)

    @property
    def corners(self):
        return [
            (self.x, self.y),                           # Top-left
            (self.x + self.width, self.y),              # Top-right
            (self.x + self.width, self.y + self.height),# Bottom-right
            (self.x, self.y + self.height)              # Bottom-left
        ]

    def contains_point(self, point):
        px, py = point
        return (self.x <= px <= self.x + self.width and
                self.y <= py <= self.y + self.height)

    def __str__(self):
        return f"BoundingBox(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

def get_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_bounding_box_distance(box1, box2):
    """Calculate the distance between the centers of two bounding boxes."""
    return get_distance(box1.center, box2.center)

def calculate_iou(box1, box2):
    """Calculate the Intersection over Union (IoU) of two bounding boxes."""
    x_left = max(box1.x, box2.x)
    y_top = max(box1.y, box2.y)
    x_right = min(box1.x + box1.width, box2.x + box2.width)
    y_bottom = min(box1.y + box1.height, box2.y + box2.height)

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    union_area = box1.area + box2.area - intersection_area

    return intersection_area / union_area

def scale_bounding_box(box, scale_factor):
    """Scale a bounding box by a given factor."""
    new_width = box.width * scale_factor
    new_height = box.height * scale_factor
    new_x = box.x + (box.width - new_width) / 2
    new_y = box.y + (box.height - new_height) / 2
    return BoundingBox(new_x, new_y, new_width, new_height)

def rotate_point(point, angle, center):
    """Rotate a point around a center by a given angle (in radians)."""
    ox, oy = center
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (qx, qy)

def rotate_bounding_box(box, angle):
    """Rotate a bounding box by a given angle (in degrees)."""
    angle_rad = math.radians(angle)
    rotated_corners = [rotate_point(corner, angle_rad, box.center) for corner in box.corners]
    
    x_coords, y_coords = zip(*rotated_corners)
    new_x = min(x_coords)
    new_y = min(y_coords)
    new_width = max(x_coords) - new_x
    new_height = max(y_coords) - new_y
    
    return BoundingBox(new_x, new_y, new_width, new_height)

def merge_bounding_boxes(boxes):
    """Merge multiple bounding boxes into a single bounding box that contains all of them."""
    if not boxes:
        return None
    
    x_min = min(box.x for box in boxes)
    y_min = min(box.y for box in boxes)
    x_max = max(box.x + box.width for box in boxes)
    y_max = max(box.y + box.height for box in boxes)
    
    return BoundingBox(x_min, y_min, x_max - x_min, y_max - y_min)

# Example usage
if __name__ == "__main__":
    box1 = BoundingBox(10, 10, 50, 50)
    box2 = BoundingBox(30, 30, 60, 60)

    print(f"Box 1: {box1}")
    print(f"Box 2: {box2}")
    print(f"Distance between boxes: {calculate_bounding_box_distance(box1, box2):.2f}")
    print(f"IoU: {calculate_iou(box1, box2):.2f}")

    scaled_box = scale_bounding_box(box1, 1.5)
    print(f"Scaled Box 1: {scaled_box}")

    rotated_box = rotate_bounding_box(box1, 45)
    print(f"Rotated Box 1: {rotated_box}")

    merged_box = merge_bounding_boxes([box1, box2])
    print(f"Merged Box: {merged_box}")

    test_point = (40, 40)
    print(f"Point {test_point} is inside Box 1: {box1.contains_point(test_point)}")
    print(f"Point {test_point} is inside Box 2: {box2.contains_point(test_point)}")