def count_tickets(tickets):
    """
    Count total tickets: pairs count as 2, remaining single ticket counts as 1
    """
    T = 0
    
    # Count pairs of tickets
    pairs = tickets // 2
    T = T + (pairs * 2)
    
    # Check if 1 ticket remains
    if tickets % 2 == 1:
        T = T + 1
    
    return T

# Test the function
print("Testing ticket counting algorithm:")
print(f"5 tickets: {count_tickets(5)}")  # Should be 5 (2 pairs + 1 remaining)
print(f"6 tickets: {count_tickets(6)}")  # Should be 6 (3 pairs + 0 remaining)
print(f"1 ticket: {count_tickets(1)}")   # Should be 1 (0 pairs + 1 remaining)
print(f"0 tickets: {count_tickets(0)}")  # Should be 0 (0 pairs + 0 remaining)