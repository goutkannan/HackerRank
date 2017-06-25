using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chaos
{
    class Program
    {
        static void Main(string[] args)
        {
            int T = Convert.ToInt32(Console.ReadLine());
            for (int a0 = 0; a0 < T; a0++)
            {
                int n = Convert.ToInt32(Console.ReadLine());
                string[] q_temp = Console.ReadLine().Split(' ');
                int[] q = Array.ConvertAll(q_temp, Int32.Parse);
                int len = q.Length;
                int dif = 0;
                for (int i = len-1; i >=0; i--)
                {
                    if (q[i]- (i+1) > 2)
                    {
                        //Console.WriteLine(Math.Abs(i - q[i-1]));
                        Console.WriteLine("Too chaotic");
                        break;
                    }
                    for(int j = Math.Max(0,q[i]-2);j < i;j++)
                    {
                        if (q[j] > q[i]) dif++;
                    }

                }
                Console.WriteLine(dif);
            }
        }

    }
}
