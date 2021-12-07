import java.util.Collections;
import java.util.Arrays;

public class Line
{
  public int x1, x2;
  public int y1, y2;
  
  public Line(int x1, int y1, int x2, int y2)
  {
    this.x1 = x1;
    this.y1 = y1;
    this.x2 = x2;    
    this.y2 = y2;
  }
  
  public String toString()
  {
    return "[" + x1 + "," + y1 + "] / "
          +"[" + x2 + "," + y2 + "]";
  }
}

ArrayList<Line> lines;
int max_x = 0, max_y = 0;
int[][] grid_weights;
int max_weight = 0;

void setup()
{
  String[] input_lines = loadStrings("C:\\scripts\\AOC2021\\src\\AOC2021\\day_05\\p1_input");  
  
  lines = new ArrayList<Line>();  
  
  for(int idx=0; idx<input_lines.length; ++idx)
  {
    String[] coordinates = input_lines[idx].split("->");
    
    String[] x1y1 = coordinates[0].split(",");
    String[] x2y2 = coordinates[1].split(",");
    
    int x1 = int(x1y1[0].trim());
    int y1 = int(x1y1[1].trim());
    int x2 = int(x2y2[0].trim());
    int y2 = int(x2y2[1].trim());
    
    if (x1==x2 || y1 == y2)
    {
      max_x = max(max_x, x1, x2);
      max_y = max(max_y, y1, y2);
  
      lines.add(new Line(x1, y1, x2, y2));
    }
  }
  
  lines.removeAll(Collections.singleton(null));
  
  println(max_y);
  println(max_x);
  
  grid_weights = new int[max_y][max_x+1];

  for (Line line : lines)
  {    
    if (line.x1 == line.x2)
    {
      for(int y=line.y1; y<line.y2; ++y)
      {
        grid_weights[y][line.x1]++;
      }
    }
    else if (line.y1 == line.y2)
    {
      for (int x=line.x1; x<line.x2; ++x)
      {
        grid_weights[line.y1][x]++;
      }
    }
  }
  
  max_weight += 0; //<>//
  max_weight += 1; //<>//
  max_weight -= 1; //<>//
  
  for(int y=0; y<grid_weights.length; ++y)
  {
    for(int x=0; x<grid_weights[y].length; ++x)
    {
      max_weight = max(max_weight, grid_weights[y][x]);
    }
  }
  
  println(max_x);
  println(max_y);
  
  print(max_weight);

  size(1000, 1000);
  background(0);
  
  background(0);
  
  // Draw grid
  strokeWeight(0.25);
  stroke(255);
  for (int y=0; y<max_y; ++y)
  {
    line(0, y, max_x, y);
  }
  for (int x=0; x<max_x; ++x)
  {
    line(x, 0, x, max_y);
  }
  
  //noStroke();
  //fill(255, 128);
  //for(int y=0; y<grid_weights.length; ++y)
  //{
  //  for (int x=0; x<grid_weights[y].length; ++x)
  //  {
  //    int weight = grid_weights[y][x];
  //    float w = map(weight, 0, max_weight, 0, 50);  
  //    circle(x, y, w);
  //  }
  //}
  
  int num_zero = 0;
  for(int y=0; y<grid_weights.length; ++y)
  {
    for (int x=0; x<grid_weights[y].length; ++x)
    {
      if (grid_weights[y][x] <= 1)
        num_zero += 1;
    }
  }
  
  println(num_zero);
}
