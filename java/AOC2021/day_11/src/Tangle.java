import processing.core.PApplet;

import java.util.HashMap;
import java.awt.Point;
import java.util.Map;

public class Tangle
{
    private HashMap<Point, DumboOctopus> octopi = null;
    private PApplet applet;


    /**
     * Creates a new Tangle with a PApplet as a parent.
     *
     * @param applet The parent PApplet instance.
     */
    public Tangle(PApplet applet)
    {
        this.octopi = new HashMap<Point, DumboOctopus>(100);
        this.applet = applet;
    }

    /**
     * Creates a new Tangle from an input matrix identifying octopi energy levels.
     * @param input_matrix The octopi energy level matrix.
     * @param applet The parent PApplet instance.
     */
    public Tangle(int[][] input_matrix, PApplet applet)
    {
        // This is done assuming the matrix is square
        int initial_capacity = input_matrix.length * input_matrix[0].length;
        this.octopi = new HashMap<Point, DumboOctopus>(initial_capacity);

        for (int y=0; y<input_matrix.length; ++y)
        {
            for (int x=0; x<input_matrix[y].length; ++x)
            {
                this.add_octopus(input_matrix[y][x], x, y);
            }
        }

        this.applet = applet;
    }


    /**
     * Adds a new octopus into the tangle with the given energy level and at the given coordinates.
     *
     * @param energy_level The octopus energy level.
     * @param x The X position of the octopus.
     * @param y The Y position of the octopus.
     */
    public void add_octopus(int energy_level, int x, int y)
    {
        this.add_octopus(energy_level, new Point(x, y));
    }

    /**
     * Adds a new octopus into the tangle with the given energy lavel and at the given point.
     *
     * @param energy_level The octopus energy level.
     * @param p The Point position of the octopus.
     */
    public void add_octopus(int energy_level, Point p)
    {
        this.octopi.put(p, new DumboOctopus(energy_level));
    }


    /**
     * Update the neighborood octopi from the given octopus coordinates.
     *
     * @param x The X position of the octopus.
     * @param y The Y position of the octopus.
     */
    public void update_neighborood(Point position)
    {
        DumboOctopus current_octopus = this.octopi.get(position);
        for (int ty=-1; ty<=1; ++ty)
        {
            for (int tx=-1; tx<=1; ++tx)
            {
                // Skip the increment for the current coordinate
                if (tx == 0 && ty == 0) continue;

                int px = position.x + tx;
                int py = position.y + ty;
                Point p = new Point(px, py);

                if (this.octopi.containsKey(p))
                {
                    DumboOctopus octopus = this.octopi.get(p);
                    if (octopus.energy_level() > 9)
                    {
                        current_octopus.increase_energy_level();
                    }
                }
            }
        }

        this.octopi.put(position, current_octopus);
    }


    /**
     *
     */
    public void cycle()
    {
        // Increase the energy level of every octopus
        this.octopi.forEach(
            (point, dumboOctopus) -> dumboOctopus.increase_energy_level()
        );

        // Update octopus neighborood when it's energy level reaches values above 9
        for (Map.Entry<Point, DumboOctopus> entry : this.octopi.entrySet()) {
            Point point = entry.getKey();
            DumboOctopus dumboOctopus = entry.getValue();
            if (dumboOctopus.energy_level() <= 9)
            {
                update_neighborood(point);
            };
        }

        // Set all octopi that have flashed back to a rechargeable status.
        this.octopi.forEach((point, dumboOctopus) -> dumboOctopus.release_flash());
    }


    /**
     *
     */
    public void draw()
    {
        applet.fill(255);
        applet.noStroke();
        int text_size = 25;
        applet.textSize(text_size);

        for (Map.Entry<Point, DumboOctopus> entry : this.octopi.entrySet()) {
            Point point = entry.getKey();
            DumboOctopus dumboOctopus = entry.getValue();
            if (dumboOctopus.energy_level() == 9)
            {
                applet.fill(255, 0, 0);
            }
            else
            {
                int ramped_color = (int)PApplet.map(
                    dumboOctopus.energy_level(),
                    0, 9,
                    50, 255
                );
                applet.fill(ramped_color);
            }
            applet.text(
                dumboOctopus.energy_level(),
                point.x * text_size,
                point.y * text_size + text_size
            );
        }
    }
}
