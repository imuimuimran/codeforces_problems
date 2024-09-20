def can_form_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x

def can_form_segment(x, y, z):
    return x + y == z or x + z == y or y + z == x

def main():
    a, b, c, d = map(int, input().split())
    
    # Check for triangle
    if (can_form_triangle(a, b, c) or
        can_form_triangle(a, b, d) or
        can_form_triangle(a, c, d) or
        can_form_triangle(b, c, d)):
        print("TRIANGLE")
    # Check for segment
    elif (can_form_segment(a, b, c) or
          can_form_segment(a, b, d) or
          can_form_segment(a, c, d) or
          can_form_segment(b, c, d)):
        print("SEGMENT")
    # Neither triangle nor segment
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
