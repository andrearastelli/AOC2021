/**
 Table object that contains functions to help with
 - checking if an extracted number is in the table
 - check if the table has won
 - draw the table
 */
public class Table
{
  private int[][][] table = new int[5][5][2]; 
  private boolean bingo = false;
  private int last_extracted_number;
  
  /**
   Construct the Table object by copying the content of the array
   into the internal data structure
   */
  public Table(int[][] input_table)
  {
    this.updateTable(input_table);
  }
  
  /**
   Updates the table content with the new input table.
   There is no need to zero-out the internal object that checks
   if a number has already been extracted because by definition
   a new int array gets initializated to have all 0 values.
   */
  public void updateTable(int[][] input_table)
  {
    this.table = new int[5][5][2];
    this.bingo = false;
    
    for (int x=0; x<5; ++x)
    {
      for (int y=0; y<5; ++y)
      {
        this.table[x][y][0] = input_table[x][y];
      }
    }
  } // end updateTable
  
  /**
   Checks if an extracted number as input is contained in the internal
   table, and if so it sets the corresponding flag to 1.
   */
  public void checkNumber(int extracted_number)
  {
    for (int x=0; x<5; ++x)
    {
      for (int y=0; y<5; ++y)
      {
        if (this.table[x][y][0] == extracted_number)
        {
          this.table[x][y][1] = 1;
        }
      }
    }
    
    this.last_extracted_number = extracted_number;
    
    this.checkVictory();
  } // end checkNumber
  
  /**
   Checks if the current table has won or not and saves the status.
   */
  public void checkVictory()
  {
    if (this.bingo == false)
    {
      for (int tx = 0; tx<5; ++tx)
      {
        int row_sum = 0;
        for(int ty = 0; ty<5; ++ty)
        {
          row_sum += this.table[tx][ty][1];
        }
        
        if (row_sum == 5)
        {
          this.bingo = true;
          break;
        }
      }
    }
    
    if (this.bingo == false) 
    {
      for(int ty = 0; ty<5; ++ty)
      {
        int col_sum = 0;
        for (int tx = 0; tx<5; ++tx)
        {
          col_sum += this.table[tx][ty][1];
        }
        
        if (col_sum == 5)
        {
          this.bingo = true;
          break;
        }
      }
    }
  } // end checkVictory
  
  /**
   Returns the saved vistory status.
   */
  public boolean hasWon()
  {
    return this.bingo;
  } // end hasWon
  
  /**
   Draws the current table at the given coordinates.
   
   The drawing is also responsible for highlighting the extracted numbers
   and changing the table background color based on the winning status.
   */
  public void draw(int x, int y)
  {
    textSize(10);
    if (!this.hasWon())
    {
      fill(255, 50);
      stroke(255);
    }
    else
    {
      fill(200, 255, 200, 50);
      stroke(50, 200, 50);
    }
      
    rectMode(CORNER);
    rect(x, y, 100, 100, 5);
    
    for (int ix=0; ix<5; ++ix)
    {
      for (int iy=0; iy<5; ++iy)
      {
        int textColor = 255;
        if (table[ix][iy][1] == 1)
        {
          shapeMode(CENTER);
          fill(200, 200, 255);
          stroke(255);
          circle(x+(ix*20)+11, y+(iy*20)+10, 20);
          textColor = 0;
        }
        fill(textColor);
        text(this.table[ix][iy][0], x+(ix*20)+5, y+(iy*20)+15);
      }
    }
    
    if (this.hasWon())
    {
      textSize(20);
      fill(255, 0, 0);
      text(this.score(), x, y + 50);
    }
  } // end draw
  
  public int score()
  {
    int result = 0;
    for (int x=0;x<5;++x)
    {
      for (int y=0;y<5;++y)
      {
        result += this.table[x][y][0] * this.table[x][y][1];
      }
    }
    
    return result * this.last_extracted_number;
  } // end score
}
