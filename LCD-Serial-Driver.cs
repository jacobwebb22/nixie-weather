using System.Threading;

public static class lcdDriver
{
    public static void WriteLine(string line)
    {
        //System.Text.UTF8Encoding encoder = new System.Text.UTF8Encoding();
        // byte[] bytesToSend = encoder.GetBytes(line);
        // lcd.Write(encoder.GetBytes(line), 0, encoder.GetBytes(line).Length);
            
        byte[] bytesToSend = System.Text.Encoding.UTF8.GetBytes(line);
        Print.LCD.Write(bytesToSend, 0, bytesToSend.Length);
        Thread.Sleep(5);
    }

    public static void WriteLines(string line1, string line2)
    {
        ClearScreen();
        SelectLineOne();

        // System.Text.UTF8Encoding encoder = new System.Text.UTF8Encoding();
        // byte[] bytesToSend = encoder.GetBytes(line);
        // lcd.Write(encoder.GetBytes(line), 0, encoder.GetBytes(line).Length);

        byte[] bytesToSend = System.Text.Encoding.UTF8.GetBytes(line1);
        Print.LCD.Write(bytesToSend, 0, bytesToSend.Length);

        Thread.Sleep(5);

        SelectLineTwo();
        bytesToSend = System.Text.Encoding.UTF8.GetBytes(line2);
        Print.LCD.Write(bytesToSend, 0, bytesToSend.Length);

        Thread.Sleep(5);
    }

    public static void SelectLineOne()
    {
        byte[] one = new byte[1];

        one[0] = 254;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        one[0] = 128;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);
    }

    public static void SelectLineTwo()
    {
        byte[] one = new byte[1];

        one[0] = 254;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        one[0] = 192;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);
    }

    public static void ClearScreen() 
    {
        byte[] one = new byte[1];
            
        one[0] = 254;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        one[0] = 1;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);
    }

    public static void SetScreenType() 
    {
        byte[] one = new byte[1];

        one[0] = 124;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        one[0] = 4;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        one[0] = 124;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        one[0] = 6;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);
    }

    public static void SetScreenBacklight(int brightness) // From 1 to 30
    {
        byte[] one = new byte[1];

        one[0] = 124;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);

        int output = 127 + brightness;
        one[0] = (byte)output;
        Print.LCD.Write(one, 0, 1);

        Thread.Sleep(5);
    }
}