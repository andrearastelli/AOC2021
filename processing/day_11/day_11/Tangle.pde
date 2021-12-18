import java.awt.Point;

/**
 Apparently a group of octopus can be called a "Tangle":
 https://oceansyrup.com/octopi-octopodes-octopuses/
 */
class Tangle
{
  // We know that the input file contains a 10x10 matrix
  // with octopi energy levels, so we can directly reserve
  // the 100 slots necessary to allocate the octopi
  // from the file
  private HashMap<Point, DumboOctopus> octopi = null;
  
  
  public Tangle()
  {
    this.octopi = new HashMap<Point, DumboOctopus>(100);
  }
  
  public Tangle(int[][] input_matrix)
  {
    this.octopi = new HashMap<Point, DumboOctopus>(
      input_matrix.length * input_matrix[0].length
    );
    
    for (int y=0; y<input_matrix.length; ++y)
    {
      for (int x=0; x<input_matrix[y].length; ++x)
      {
        this.add_octopus(input_matrix[y][x], x, y);
      }
    }
  }
  
  
  public void add_octopus(int energy_level, int x, int y)
  {
    this.add_octopus(energy_level, new Point(x, y));
  }
  
  public void add_octopus(int energy_level, Point p)
  {
    this.octopi.put(p, new DumboOctopus(energy_level));
  }
  
  
  public void update_neighborood(int x, int y)
  {
    
  }
}
