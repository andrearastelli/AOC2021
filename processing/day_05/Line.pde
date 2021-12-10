public class Line
{
  public int x1, x2;
  public int y1, y2;
  
  public Line(int x1, int y1, int x2, int y2)
  {
    this.x1 = x1;
    this.x2 = x2;
    this.y1 = y1;
    this.y2 = y2;
  } // end Line
  
  public boolean overlaps(int x, int y)
  {
    boolean overlaps = false;
    
    if (this.y1 == this.y2 && y == this.y1)
    {
      if (x >= this.x1 && x <= this.x2)
      {
        overlaps = true;
      }
    }
    else if (this.x1 == this.x2 && x == this.x1)
    {
      if (y >= this.y1 && y <= this.y2)
      {
        overlaps = true;
      }
    }
    else
    {
      //int line_length = (int)dist(this.x1, this.y1, this.x2, this.y2);
      //for (int i=0; i<line_length; ++i)
      //{
      //  int lx = (int)lerp(this.x1, this.x2, map(i, 0, line_length, 0, 1));
      //  int ly = (int)lerp(this.y1, this.y2, map(i, 0, line_length, 0, 1));
      //  if (x == lx && y == ly)
      //  {
      //    overlaps = true;
      //  }
      //}
    }
    
    return overlaps;
  } // end overlaps
  
  public void draw()
  {
    noStroke();
    fill(255, 30);
    ellipseMode(RADIUS);
    
    int ellipse_radius = 1;
    
    // Draw the dots vertically when x1 == x2
    if (this.x1 == this.x2)
    {
      int x = this.x1;
      for (int y=this.y1; y<this.y2; ++y)
      {
        ellipse(x, y, ellipse_radius, ellipse_radius);
      }
    }
    
    // Draw the dots horizontally when y1 == y2
    else if (this.y1 == this.y2)
    {
      int y = this.y1;
      for (int x=this.x1; x<this.x2; ++x)
      {
        ellipse(x, y, ellipse_radius, ellipse_radius);
      }
    }
    
    // Draw the dots diagonally when x1 != x2 and y1 != y2
    else
    {      
      int line_length = abs(this.x2 - this.x1);
      
      for (int x=0; x<line_length; ++x)
      {
        int cx = (int)lerp(this.x1, this.x2, map(x, 0, line_length-1, 0, 1));
        int cy = (int)lerp(this.y1, this.y2, map(x, 0, line_length-1, 0, 1));
        
        ellipse(cx, cy, ellipse_radius, ellipse_radius);
      }      
    }
  } // end draw
  
  public String toString()
  {
    return "[" + this.x1 + "," + this.y1 + "] / "
          +"[" + this.x2 + "," + this.y2 + "]";
  } // end toString()
}
