import java.util.Arrays;
import java.util.stream.*;

void settings()
{
  size(600, 600);
}

//int[][] matrix = new int[10][10];
int[][] matrix = {
  {1, 1, 1, 1, 1},
  {1, 9, 9, 9, 1},
  {1, 9, 1, 9, 1},
  {1, 9, 9, 9, 1},
  {1, 1, 1, 1, 1},
};

final int max_iterations = 100;
int iterations = 0;

void setup()
{
  //String[] lines = loadStrings("C:\\scripts\\AOC2021\\src\\AOC2021\\day_11\\p1_input");
  //for (int j=0; j<lines.length; ++j)
  //{
  //  for (int i=0; i<lines[j].length(); ++i)
  //  {
  //    matrix[j][i] = int(str(lines[j].charAt(i)));  
  //  }
  //}
  
  frameRate(1); //<>//
}

void draw()
{
  background(0);
  
  draw_matrix(matrix);
  
  // Update the matrix
  // increment all the values for the octopi
  matrix = increment_energy_level(matrix);
  
  draw_matrix_with_offset(matrix, 250, 0, 50);
  
  // Check around each 9 to increment
  int idx = 0;
  while( matrix_has_9s(matrix) )
  {
    matrix = flash_update(matrix);
    
    draw_matrix_with_offset(matrix, idx*125, 250, 25);
    
    idx++;
  }
  
  iterations ++;
  
  //if (iterations >= 2)
  noLoop();
}

void mousePressed()
{
  noLoop();
}

void mouseReleased()
{
  loop();
}
