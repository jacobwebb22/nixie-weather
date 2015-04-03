using System;
using System.Threading;
using Microsoft.SPOT;
using Microsoft.SPOT.Hardware;
using SecretLabs.NETMF.Hardware;
using SecretLabs.NETMF.Hardware.NetduinoPlus;
using System.IO.Ports;

public static class Print
{
    public static System.IO.Ports.SerialPort LCD;
    static AnalogInput Pot1;
    static AnalogInput Pot2;
    public static int SetOld1 = 0;
    public static int SetOld2 = 0;

    public static void Setup() 
    {
        LCD = new System.IO.Ports.SerialPort(SerialPorts.COM1, 9600, Parity.None, 8, StopBits.One);
        LCD.Open();

        Pot1 = new AnalogInput(Pins.GPIO_PIN_A5);
        Pot2 = new AnalogInput(Pins.GPIO_PIN_A4);
    }
    
    
    public static void Updating()
    {

        lcdDriver.ClearScreen();
        lcdDriver.WriteLines("    UPDATING", "");

    }

    public static void UpdateFailed()
    {

        lcdDriver.ClearScreen();
        lcdDriver.SelectLineOne();
        lcdDriver.WriteLine("UPDATE FAILED");

    }

    public static void PrintToday()
    {
        lcdDriver.ClearScreen();
        lcdDriver.SelectLineOne();
        lcdDriver.WriteLines(States.Location.City + "    " + States.Currently.Day[0], States.Currently.TempNow + " " + States.Currently.CondNow);
    }

    public static void PrintBacklight()
    {
        int Set2 = Sector(2);

        if (Set2 != SetOld2 && Set2 != 0)
        {
            switch (Set2)
            {
                case 1:
                    lcdDriver.SetScreenBacklight(1);
                    break;
                case 2:
                    lcdDriver.SetScreenBacklight(5);
                    break;
                case 3:
                    lcdDriver.SetScreenBacklight(10);
                    break;
                case 4:
                    lcdDriver.SetScreenBacklight(20);
                    break;
                case 5:
                    lcdDriver.SetScreenBacklight(29);
                    break;
                default:
                    break;
            }
            SetOld2 = Set2;
        }
    }

    public static void PrintWeather()
    {
        int Set1 = Sector(1);

        if (Set1 != SetOld1 && Set1 != 0)
        {
            switch (Set1)
            {
                case 1:
                    lcdDriver.WriteLines(States.Location.City + "    " + States.Currently.Day[0], States.Currently.TempNow + " " + States.Currently.CondNow);
                    break;
                case 2:
                    lcdDriver.WriteLines("Today" + "      " + States.Currently.TempLow[0] + "-" + States.Currently.TempHigh[0], States.Currently.Cond[0]);
                    break;
                case 3:
                    lcdDriver.WriteLines(States.Currently.Day[1] + "        " + States.Currently.TempLow[1] + "-" + States.Currently.TempHigh[1], States.Currently.Cond[1]);
                    break;
                case 4:
                    lcdDriver.WriteLines(States.Currently.Day[2] + "        " + States.Currently.TempLow[2] + "-" + States.Currently.TempHigh[2], States.Currently.Cond[2]);
                    break;
                case 5:
                    lcdDriver.WriteLines(States.Currently.Day[3] + "        " + States.Currently.TempLow[3] + "-" + States.Currently.TempHigh[3], States.Currently.Cond[3]);
                    break;
                default:
                    break;
            }
            SetOld1 = Set1;
        }
    }

    public static int Sector(int PotNum)
    {
        int Reading1 = 0;

        if (PotNum == 1) { Reading1 = Pot1.Read(); }
        if (PotNum == 2) { Reading1 = Pot2.Read(); }

        if (Reading1 < 200) { return 1; }
        else if (Reading1 < (400) && Reading1 >= (200)) { return 2; }
        else if (Reading1 < (600) && Reading1 >= (400)) { return 3; }
        else if (Reading1 < (800) && Reading1 >= (600)) { return 4; }
        else if (Reading1 >= (800)) { return 5; }
        else { return 0; }
    }
}