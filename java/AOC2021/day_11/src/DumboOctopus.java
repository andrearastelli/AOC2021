import java.beans.BeanProperty;

public class DumboOctopus
{
    private int energy = 0;
    private boolean trigger_flash = false;


    /**
     * Creates a new octopus with the given energy level.
     *
     * @param starting_energy the octopus energy level upon creation.
     */
    public DumboOctopus(int starting_energy)
    {
        this.energy = starting_energy;
    }


    /**
     * Increase the energy level of the current octopus.
     */
    public void increase_energy_level()
    {
        if (!this.is_flash_triggered())
        {
            this.energy ++;
        }

        if (this.energy > 9 && !this.is_flash_triggered())
        {
            this.trigger_flash = true;
            this.energy = 0;
        }
    }


    /**
     * Returns whether the flash has been triggered by the
     * previous increase of energy level.
     *
     * @return if the flash has been triggered for the current octopus or not.
     */
    public boolean is_flash_triggered()
    {
        return this.trigger_flash;
    }


    /**
     * Releases the flash after it has been triggered.
     */
    public void release_flash()
    {
        this.trigger_flash = false;
    }


    /**
     * Returns the current octopus energy level.
     *
     * @return the energy level.
     */
    public int energy_level()
    {
        return this.energy;
    }


    @Override
    public String toString()
    {
        return String.format("[ Energy: %d; Flash: %B ]", this.energy_level(), this.is_flash_triggered());
    }
}
