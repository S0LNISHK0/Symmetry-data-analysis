using System;
using System.Collections.Generic;
using System.Text;
using System.IO;


namespace Turb
{
    using Turb.edu.jhu.pha.turbulence;
    class Program
    {
        static void Main(string[] args)
        {
//            Microsoft.Office.Interop.Excel.Application ApEx = new Microsoft.Office.Interop.Excel.Application();
            int Lgth = 24;
            Random random = new Random();
            TurbulenceService service = new TurbulenceService();
            Point3[] points = new Point3[Lgth];
            Vector3[] Veloc = new Vector3[Lgth];
            VelocityGradient[] VelGr = new VelocityGradient[Lgth];
//            service.GetBoxFilterAsync(
            for (int i = 0; i < Lgth; i++)
            {
                points[i] = new Point3();
//                points[i].x = 1;
//                points[i].y = 1;
//                points[i].z = 1;
                points[i].x = (float)(random.NextDouble() * 2.0 * 3.14);
                points[i].y = (float)(random.NextDouble() * 2.0 * 3.14);
                points[i].z = (float)(random.NextDouble() * 2.0 * 3.14);
            }
            string authToken = @"jhu.edu.pha.turbulence.testing-200711";
            string dataSet = @"isotropic1024fine";
            float time = 0.0024f;
            SpatialInterpolation SpatInt_V = Turb.edu.jhu.pha.turbulence.SpatialInterpolation.Lag4;
            SpatialInterpolation SpatInt_G = Turb.edu.jhu.pha.turbulence.SpatialInterpolation.M2Q14;
            TemporalInterpolation TempInt = Turb.edu.jhu.pha.turbulence.TemporalInterpolation.None;
            Veloc = service.GetVelocity(authToken, dataSet, time, SpatInt_V, TempInt, points);
            VelGr = service.GetVelocityGradient(authToken, dataSet, time, SpatInt_G, TempInt, points);
            float DUDx;
            float DVDx;
            float DWDx;
            float DUDy;
            float DVDy;
            float DWDy;
            float DUDz;
            float DVDz;
            float DWDz;
            float S11;
            float S12;
            float S13;
            float S21;
            float S22;
            float S23;
            float S31;
            float S32;
            float S33;
            float Tr;
            double sgm;
            double qi;
            double ri;
            double p1;
            double q1;
            double r1;
            double Qdis;
            double q2;
            double r2;
            for (int r = 0; r < Lgth; r++)
            {
                Console.WriteLine("X={0} Y={1} Z={2}", Veloc[r].x, Veloc[r].y, Veloc[r].z);
            }
            string path = @"c:\temp\TurbTest.txt";
            if (!File.Exists(path))
            {
                // Create a file to write to.
                using (StreamWriter sw = File.CreateText(path))
                {
//                    for (int r = 0; r < Lgth; r++)
//                    {
//                        sw.WriteLine("X={0} Y={1} Z={2}", Veloc[r].x, Veloc[r].y, Veloc[r].z);
//                    }
                    for (int r = 0; r < Lgth; r++)
                    {
                        DUDx = VelGr[r].duxdx;
                        DVDx = VelGr[r].duydx;
                        DWDx = VelGr[r].duzdx;
                        DUDy = VelGr[r].duxdy;
                        DVDy = VelGr[r].duydy;
                        DWDy = VelGr[r].duzdy;
                        DUDz = VelGr[r].duxdz;
                        DVDz = VelGr[r].duydz;
                        DWDz = VelGr[r].duzdz;
                        S11 = DUDx;
                        S12 = (DUDy + DVDx) / 2;
                        S13 = (DUDz + DWDx) / 2;
                        S21 = (DVDx + DUDy) / 2;
                        S22 = DVDy;
                        S23 = (DVDz + DWDy) / 2;
                        S31 = (DWDx + DUDz) / 2;
                        S32 = (DWDy + DVDz) / 2;
                        S33 = DWDz;
                        Tr = DUDx + DVDy + DWDz;
                        qi = -Math.Pow(S11, 2) - Math.Pow(S12, 2) - Math.Pow(S13, 2) - S11 * S22 - Math.Pow(S22, 2) - Math.Pow(S23, 2);
                        ri = -S11 * Math.Pow(S12, 2) + Math.Pow(S11, 2) * S22 - Math.Pow(S12, 2) * S22 + Math.Pow(S13, 2) * S22 + S11 * Math.Pow(S22, 2) - 2 * S12 * S13 * S23 + S11 * Math.Pow(S23, 2);
                        p1 = -Tr;
                        q1 = -Math.Pow(S12, 2) - Math.Pow(S13, 2) - Math.Pow(S23, 2) + S11 * S22 + S11 * S33 + S22 * S33;
                        r1 = Math.Pow(S23, 2) * S11 + Math.Pow(S13, 2) * S22 + Math.Pow(S12, 2) * S33 - 2 * S12 * S13 * S23 - S11 * S22 * S33;
                        q2 = (3 * q1 - Math.Pow(p1, 2)) / 3;
                        r2 = (2 * Math.Pow(p1, 3) - 9 * p1 * q1 + 27 * r1) / 27;
                        sgm = Tr/Math.Sqrt(Math.Pow(DUDx, 2) + Math.Pow(DVDy, 2) + Math.Pow(DWDz, 2));
                        Qdis = Math.Pow(q1 / 3, 3) + Math.Pow(r1 / 2, 2);

//                        sw.WriteLine("X1={0} Y1={1} Z1={2}", DUDx, DVDx, DWDx);
                        sw.WriteLine("S11={0} S12={1} S13={2}", S11, S12, S13);
                        sw.WriteLine("S21={0} S22={1} S23={2}", S21, S22, S23);
                        sw.WriteLine("S31={0} S32={1} S33={2}", S31, S32, S33);
                        sw.WriteLine("Характеристическое уравнение (с учетом несжимаемости): l^3+({0})l+({1})=0", qi, ri);
                        sw.WriteLine("Характеристическое уравнение (без учета несжимаемости): l^3+({0})l^2+({1})l+({2})=0", p1, q1, r1);
                        sw.WriteLine("Характеристическое уравнение (без учета несжимаемости): (l+({2}))^3+({0})(l+{2})+({1})=0", q2, r2, p1/3);
                        sw.WriteLine("sgm={0} Tr={1} X={2} Y={3} Z={4} Qdis={5}", sgm, Tr, points[r].x, points[r].y, points[r].z, Qdis);
                        sw.WriteLine(" ");
                    }
            //        sw.WriteLine("DUDx={0} DVDx={1} DWDx={2} DUDy={3} DVDy={4} DWDy={5} DUDz={6} DVDz={7} DWDz={8} Tr={9} X={10} Y={11} Z={12}", DUDx, DVDx, DWDx, DUDy, DVDy, DWDz, DUDz, DVDz, DWDz, Tr, points[r].x, points[r].y, points[r].z);
                }
            }
        }
    }
}
