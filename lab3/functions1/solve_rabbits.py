def solve(num_heads, num_legs):
    """
    take rabbits as x.
    """
    if num_legs % 2 != 0 or num_legs < num_heads * 2:
      return "Invalid condition."  
      
    chickens = (4 * num_heads - num_legs) // 2
    rabbits  = num_heads - chickens    
    
    return chickens, rabbits