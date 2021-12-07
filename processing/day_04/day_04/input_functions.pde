int[] randomNumberSequence(String[] list_random_numbers)
{
  int[] random_numbers = new int[list_random_numbers.length];
  
  for (int i=0; i<list_random_numbers.length; ++i)
  {
    random_numbers[i] = int(list_random_numbers[i].trim());
  }
  
  return random_numbers;
} // end randomNumberSequence

void printTable(int[][] table)
{
  for (int x=0; x<table.length; ++x)
  {
    for (int y=0; y<table[x].length; ++y)
    {
      print(table[x][y], " ");
    }
    print("\n");
  }
} // end printTable

String[] cleanupStringArray(String[] string_array)
{
  StringList output = new StringList();
  for (int i=0; i<string_array.length; ++i)
  {
    if (string_array[i].equals(""))
      continue;
    output.append(string_array[i]);
  }
  
  return output.array();
} // end cleanupStringArray

ArrayList<Table> extractTables(String[] input_data)
{
  ArrayList<Table> output = new ArrayList<Table>();
  
  int[][] table = new int[5][5];
  int idx_row = 0;
  int idx_col = 0;
  for (int idx=2; idx<input_data.length; ++idx)
  {    
    input_data[idx] = input_data[idx].trim();
    String[] number_strings = input_data[idx].split(" ");
    number_strings = cleanupStringArray(number_strings);
    
    if (number_strings.length < 5)
    {
      printTable(table); 
      output.add(new Table(table));
      
      // Reset variables
      table = new int[5][5];
      idx_row = 0;
      idx_col = 0;
      
      // Jump to next iteration directly
      continue;
    }
    
    int[] numbers = new int[number_strings.length];
    for (int idx_number=0; idx_number<5; ++idx_number)
    {
      numbers[idx_number] = int(number_strings[idx_number].trim());
    }
    
    //printArray(numbers);
    for(idx_col=0; idx_col<5; ++idx_col)
    {
      table[idx_row][idx_col] = numbers[idx_col];
    }
    
    ++idx_row;
  }
  
  return output;
} // end extractTables
