using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Numerics;

namespace Turb
{
    using Turb.edu.jhu.pha.turbulence;
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            var service = new TurbulenceService();
            var points = new Point3[10];
            Vector3[] output;
            for (int i = 0; i < points.Length; i++)
            {
                points[i] = new Point3();
                points[i].x = (float)(random.NextDouble() * 2.0 * 3.14);
                points[i].y = (float)(random.NextDouble() * 2.0 * 3.14);
                points[i].z = (float)(random.NextDouble() * 2.0 * 3.14);
            }
            SpatialInterpolation SpatInt_V = Turb.edu.jhu.pha.turbulence.SpatialInterpolation.M2Q14;
            TemporalInterpolation TempInt = Turb.edu.jhu.pha.turbulence.TemporalInterpolation.None;
            output = service.GetVelocity("edu.jhu.pha.turbulence.testing-201311", "isotropic1024fine", 0.0024f, SpatInt_V, TempInt, points); // put null for the last parameter
            for (int r = 0; r < output.Length; r++)
            {
                Console.WriteLine("X={0} Y={1} Z={2}", output[r].x, output[r].y, output[r].z);
            }
        }
    }
}
