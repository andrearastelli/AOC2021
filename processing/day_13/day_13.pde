import java.awt.Point;

String input_file_path = "C:\\scripts\\AOC2021\\src\\AOC2021\\day_13\\p1_input";

int max_x = -1;
int max_y = -1;

ArrayList<Point> points = new ArrayList<Point>();
ArrayList<Point> lines = new ArrayList<Point>();

void settings()
{
  size(1320, 900);
}

void setup()
{
  String[] file_content = loadStrings(input_file_path);
  
  for (String line : file_content)
  {
    if (line.trim().equalsIgnoreCase(""))
    {
      break;
    }
    String[] s_coordinates = line.trim().split(",");
    int x = int(s_coordinates[0]);
    int y = int(s_coordinates[1]);
    
    max_x = max(max_x, x);
    max_y = max(max_y, y);
    
    points.add(new Point(x, y));
  }
  
  boolean ignore_line = true;
  for (String line : file_content)
  {    
    if (line.trim().equalsIgnoreCase(""))
    {
      ignore_line = false;
      continue;
    }
    
    if (ignore_line == true) continue;
    
    String[] chunks = line.trim().split(" ");
    String[] coords = chunks[2].split("=");
    char direction = coords[0].charAt(0);
    int value = int(coords[1]);
    
    Point p;
    if (direction == 'x') p = new Point(value, 0);
    else p = new Point(0, value);
    
    lines.add(p);
  }
  
  boolean[][] matrix = new boolean[1000][1000];
  println(max_x, max_y);
  
  printArray(lines);
}

void draw()
{
  background(0);
  
  shapeMode(CENTER);
  fill(255);
  noStroke();
  for (Point p : points)
  {
    circle(p.x, p.y, 5);
  }
  
  Point line0 = lines.get(0);
  println(line0);
  fill(0, 255, 0);
  for (Point p : points)
  {  
    if (p.x > line0.x)
    {
      circle(p.x - 2 * (p.x - line0.x), p.y, 5);
    }
  }
  
  stroke(255, 0, 0);
  for(Point p : lines)
  {
    if (p.y == 0)
      line(p.x, 0, p.x, height);
    else
      line(0, p.y, width, p.y);
      
    //break;
  }
}
