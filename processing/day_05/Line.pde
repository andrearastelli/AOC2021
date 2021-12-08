public class Line
{
  public int x1, x2;
  public int y1, y2;
  
  public Line(int x1, int y1, int x2, int y2)
  {
    // Keep X1 to always be the lowest coordinate
    if (x1 > x2)
    {
      this.x1 = x2;
      this.x2 = x1;
    }
    else
    {
      this.x1 = x1;
      this.x2 = x2;
    }
    
    // Keep Y1 to always be the lowest coordinate
    if (y1 > y2)
    {
      this.y1 = y2;
      this.y2 = y1;
    }
    else
    {
      this.y1 = y1;
      this.y2 = y2;
    }
  } // end Line
  
  public void draw()
  {
    noStroke();
    fill(255);
    ellipseMode(RADIUS);
    for (int x=this.x1; x<this.x2; ++x)
    {
      for (int y=this.y1; y<this.y2; ++y)
      {
        println(x, y);
        ellipse(x, y, 2, 2);
      }
    }
  } // end draw
  
  public String toString()
  {
    return "[" + this.x1 + "," + this.y1 + "] / "
          +"[" + this.x2 + "," + this.y2 + "]";
  } // end toString()
}
