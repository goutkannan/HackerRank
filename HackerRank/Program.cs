using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication3
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] tokens_x1 = Console.ReadLine().Split(' ');
            int x1 = Convert.ToInt32(tokens_x1[0]);
            int v1 = Convert.ToInt32(tokens_x1[1]);
            int x2 = Convert.ToInt32(tokens_x1[2]);
            int v2 = Convert.ToInt32(tokens_x1[3]);
            if((x2>x1) && (v2 >= v1))
            {
                Console.Write("No");
            }
            else if(v1>v2)
            {
                int diff = x2 - x1;
                int factor = diff - (v1 - v2);
                while(factor>0)
                {
                    factor = factor - (v1 - v2); 

                }
                if(factor==0)
                    Console.Write("Yes");
                else
                    Console.Write("No");
            }

            
        }
    }
}
