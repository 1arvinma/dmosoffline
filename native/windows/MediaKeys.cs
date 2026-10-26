using System;using System.Runtime.InteropServices;
class MediaKeys {
 [DllImport("user32.dll")]static extern void keybd_event(byte key,byte scan,uint flags,UIntPtr extra);
 static int Main(string[] args){if(args.Length!=1)return 2;byte k;switch(args[0]){case "previous":k=0xB1;break;case "next":k=0xB0;break;case "play-pause":k=0xB3;break;case "stop":k=0xB2;break;case "volume-up":k=0xAF;break;case "volume-down":k=0xAE;break;default:return 2;}keybd_event(k,0,0,UIntPtr.Zero);keybd_event(k,0,2,UIntPtr.Zero);return 0;}
}
