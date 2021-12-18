void draw_matrix_with_offset(int[][] matrix, int x_offset, int y_offset, int text_size)
{
  // Show the matrix
  textSize(text_size);
  
  for(int y=0; y<matrix.length; ++y)
  {
    for(int x=0; x<matrix[y].length; ++x)
    {
      int tx = x * (text_size) + int(text_size * 0.5) + x_offset;
      int ty = y * (text_size) + int(text_size * 0.9) + y_offset;
      
      int matrix_value = matrix[y][x];
      if (matrix_value >= 9)
        fill(255, 0, 0);
      else
        fill(map(matrix_value, 0, 9, 25, 255));
        
      text(""+matrix_value, tx, ty);
    }
  }
}


void draw_matrix(int[][] matrix)
{
  draw_matrix_with_offset(matrix, 0, 0, 50);
}


int[][] increment_energy_level(int[][] matrix)
{
  for(int y=0; y<matrix.length; ++y)
  {
    for(int x=0; x<matrix[y].length; ++x)
    {
      matrix[y][x] += 1;
    }
  }
  
  return matrix;
}


boolean matrix_has_9s(int[][] matrix)
{
  boolean contains_9 = false;
  for (int i=0; i < matrix.length; ++i)
  {
    for (int j=0; j < matrix[i].length; ++j)
    {
      contains_9 = contains_9 || (matrix[i][j] > 9);
    }
  }
  
  return contains_9;
}


int[][] flash_octopi(int[][] matrix, int x, int y)
{
  for (int iy=-1; iy<=1; ++iy)
  {
    for (int ix=-1; ix<=1; ++ix)
    {
      if (ix == 0 && iy == 0) continue;
      
      if (y+iy < 0 || y+iy >= matrix.length) continue;
      
      if (x+ix < 0 || x+ix >= matrix[y].length) continue;
      
      matrix[y+iy][x+ix] += 1;
    }
  }
  
  return matrix;
}


int[][] flash_update(int[][] matrix)
{
  ArrayList<int[]> reset_coordinates = new ArrayList<int[]>();
  
  int draw_idx = 0;
  for (int y=0; y<matrix.length; ++y)
  {
    for (int x=0; x<matrix[y].length; ++x)
    {
      int value = matrix[y][x];
      
      if (value > 9)
      {
        matrix = flash_octopi(matrix, x, y);
        draw_matrix_with_offset(matrix, (draw_idx%8)*70, 400+int(draw_idx/8)*70, 13);
        draw_idx ++;
      }
    }
  }
  
  for (int y=0; y<matrix.length; ++y)
  {
    for (int x=0; x<matrix[y].length; ++x)
    {
      if (matrix[y][x] >= 9)
      {
        int[] position = {x, y};
        reset_coordinates.add(position);
      }
    }
  }
  
  for (int[] position : reset_coordinates)
  {
    int x = position[0];
    int y = position[1];
    matrix[y][x] = 0;
    
    print("["+x+", "+y+"] ");
  }
  println("");
  
  return matrix;
}
