ArrayList<Line> lines;
int max_x = 0;
int max_y = 0;
int[][] grid_weights;
int max_weight = 0;

void settings()
{
  size(1000, 1000);
}

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
    
    //if (x1 == x2 || y1 == y2)
    {
      max_x = max(max_x, x1, x2);
      max_y = max(max_y, y1, y2);
  
      lines.add(new Line(x1, y1, x2, y2));
    }
  }
  
  println(lines.size());
  println("Setup mode ended");
  
  // Investigate the points with more than 2 lines overlapping
  println("Start investigating overlapping points for lines");
  int total_overlapping = 0;
  for (int x=0; x<max_x; ++x)
  {
    for (int y=0; y<max_y; ++y)
    {
      int count_overlaps = 0;
      for (Line line : lines)
      {
        count_overlaps += int(line.overlaps(x, y));
      }
      
      if (count_overlaps >= 2)
      {
        ++total_overlapping;
      }
    }
  }
  println("Total overlapping: ", total_overlapping);
  println("End investigation.");
}

void draw()
{
  background(0);
  
  stroke(255, 30);
  for (Line line : lines)
  {
    line.draw();
  }
  
  noLoop();
}
