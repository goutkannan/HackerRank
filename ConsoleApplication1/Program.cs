using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(String[] args)
        {
            string[] tokens_n = Console.ReadLine().Split(' ');
            int n = Convert.ToInt32(tokens_n[0]);
            int k = Convert.ToInt32(tokens_n[1]);
            string[] a_temp = Console.ReadLine().Split(' ');
            int[] a = Array.ConvertAll(a_temp, Int32.Parse);
            int j = 0;
            int count=0;
            for (int i = 0; i < n - 1; i++)
            {
                for (j = i + 1; j <= n -1; j++)
                {
                    if ((a[i] + a[j]) % k == 0)
                        count++; 
                }
            }
            Console.WriteLine(count);
        }
    }
}
