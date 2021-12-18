class DumboOctopus
{
  private int energy = 0;
  private boolean trigger_flash = false;
  
  public DumboOctopus(int starting_energy)
  {
    energy = starting_energy;
  }
  
  public void increase_energy_level()
  {
    this.energy ++;
    
    if (this.energy > 9)
    {
      this.trigger_flash = true;
      this.energy = 0;
    }
  }
  
  public boolean is_flash_triggered()
  {
    return this.trigger_flash;
  }
  
  public void release_flash()
  {
    this.trigger_flash = false;
  }
}
