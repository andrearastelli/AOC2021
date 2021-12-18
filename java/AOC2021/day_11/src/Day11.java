import processing.core.PApplet;
import processing.data.StringList;

public class Day11 extends PApplet
{
    private Tangle tangle;

    @Override
    public void settings()
    {
        this.smooth();
        this.size(600, 600);
    }

    @Override
    public void setup()
    {
        StringList lines = new StringList();
        lines.append(
            loadStrings(
                    "C:\\scripts\\AOC2021\\src\\AOC2021\\day_11\\p1_input"
            )
        );

        // Convert to int[][]
//        int[][] input_matrix = new int[10][10];
//        int row = 0;
//        for (String line : lines)
//        {
//            for (int col=0; col<line.length(); ++col)
//            {
//                int value = Integer.parseInt(str(line.charAt(col)));
//                input_matrix[row][col] = value;
//            }
//            row++;
//        }

        int[][] input_matrix = {
            {1, 1, 1, 1, 1},
            {1, 9, 9, 9, 1},
            {1, 9, 1, 9, 1},
            {1, 9, 9, 9, 1},
            {1, 1, 1, 1, 1}
        };

        tangle = new Tangle(input_matrix, this);
    }

    @Override
    public void draw()
    {
        background(0);

        tangle.cycle();

        tangle.draw();

        this.noLoop();
    }

    @Override
    public void mousePressed()
    {
        this.loop();
    }

    @Override
    public void mouseReleased()
    {
        this.noLoop();
    }

    public static void main(String[] args)
    {
        PApplet.main("Day11");
    }
}
