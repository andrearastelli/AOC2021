import java.util.Arrays;

int[] random_numbers;
ArrayList<Table> tables = new ArrayList<Table>();
int idx_random_number = 0;
int max_random_number = 0;
int first_table_completed = -1;
int last_table_completed = -1;

void settings()
{
  final int size = 100*10 + 10*10 + 5; 
  size(size, size);
}

void setup()
{
  String[] input_data = loadStrings("C:\\scripts\\AOC2021\\src\\AOC2021\\day_04\\p1_input");
  
  String[] random_numbers_strings = input_data[0].split(",");
  
  random_numbers = randomNumberSequence(random_numbers_strings);  
  max_random_number = random_numbers.length;
  last_table_completed = max_random_number;

  tables = extractTables(subset(input_data, 0));
  
  frameRate(5);
}

void draw()
{
  if (idx_random_number == max_random_number - 1)
  {
    noLoop();
  }
  
  // Cleanup the canvas
  background(0);
  
  // Draw the random number
  int random_number = random_numbers[idx_random_number];
  print(random_number, " ");
  
  // Draw the tables
  for(int table_idx=0; table_idx<tables.size(); ++table_idx)
  {
    int x = (table_idx % 10) * 100 + (table_idx % 10) * 10 + 5;
    int y = (table_idx / 10) * 100 + (table_idx / 10) * 10 + 5;
    
    Table table = tables.get(table_idx);
    
    if (!table.hasWon())
      table.checkNumber(random_number);
      
    table.draw(x, y);    
  }

  idx_random_number++;
}

void mousePressed()
{
  noLoop();
}

void mouseReleased()
{
  loop();
}
