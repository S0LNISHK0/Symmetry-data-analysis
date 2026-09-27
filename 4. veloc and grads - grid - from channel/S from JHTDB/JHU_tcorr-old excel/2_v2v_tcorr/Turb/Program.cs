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
            //            Microsoft.Office.Interop.Excel.Application ApEx = new Microsoft.Office.Interop.Excel.Application();
            int Nmb_of_pts_1cycle = 3;//1000;//1500;//2000-optimal
            int Nmb_of_Cycles = 3;//100;//100//800
            int Nmb_of_Widths = 3;//15
            int Nmb_of_TimeSteps = 6;
            float Width = 0.1f;//\eta=0.0028, L=1.364, \lambda=0.113, x\in(0,2\pi), 1024^3
            float Width2 = 0.4f;
            float time_0 = 0.2f;//t\in(0; 10.056), \delta t=0.002, 5028 snapshots
            float time_step = 0.03f;//t_\eta=0.0424, t_L=1.99
            float[] time = new float[3 * Nmb_of_TimeSteps + 1];//3
            float[] delta_t = new float[3 * Nmb_of_TimeSteps + 1];//3
            int Nmb_of_pts = new int();
            Random random = new Random();
            TurbulenceService service = new TurbulenceService();
            Point3[] points = new Point3[Nmb_of_pts_1cycle];
            Point3[,] points2 = new Point3[Nmb_of_pts_1cycle, Nmb_of_Widths + 1];
            Point3[,] points21 = new Point3[Nmb_of_pts_1cycle, Nmb_of_Widths + 1];
            Point3[] points3 = new Point3[Nmb_of_pts_1cycle];
            Point3[] points31 = new Point3[Nmb_of_pts_1cycle];
            Vector3[] Veloc = new Vector3[Nmb_of_pts_1cycle];
            Vector3[,,] Veloc2 = new Vector3[Nmb_of_pts_1cycle, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];//3
            Vector3[,,] Veloc21 = new Vector3[Nmb_of_pts_1cycle, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];//3
            VelocityGradient[,,] VelGr2 = new VelocityGradient[Nmb_of_pts_1cycle, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];
            VelocityGradient[,,] VelGr21 = new VelocityGradient[Nmb_of_pts_1cycle, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];
            Vector3[] Veloc3 = new Vector3[Nmb_of_pts_1cycle];
            Vector3[] Veloc31 = new Vector3[Nmb_of_pts_1cycle];
            VelocityGradient[] VelGr3 = new VelocityGradient[Nmb_of_pts_1cycle];
            VelocityGradient[] VelGr31 = new VelocityGradient[Nmb_of_pts_1cycle];
            float[] Phi = new float[Nmb_of_pts_1cycle];
            float[] Theta = new float[Nmb_of_pts_1cycle];
            double[,,] s = new double[4, 4, Nmb_of_pts_1cycle];
            double[,,] v = new double[4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];//3
            double[,,,] A = new double[4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];//3
            double[,,,] Cvv = new double[4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];
            double[,,,,,] Cvvv = new double[4, 4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1, 3 * Nmb_of_TimeSteps + 1];//3
            double[,,,,,,] CvvA = new double[4, 4, 4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1, 3 * Nmb_of_TimeSteps + 1];//3
            double[,,] v1 = new double[4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];//3
            double[,,,] A1 = new double[4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];//3
            double[,,,] Cvv1 = new double[4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1];
            double[,,,,,] Cvvv1 = new double[4, 4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1, 3 * Nmb_of_TimeSteps + 1] ;//3
            double[,,,,,,] CvvA1 = new double[4, 4, 4, 4, Nmb_of_Widths + 1, 3 * Nmb_of_TimeSteps + 1, 3 * Nmb_of_TimeSteps + 1];//3
            for (int I_T = 0; I_T <= 3 * Nmb_of_TimeSteps; I_T++)//3
            {
                if (I_T <= Nmb_of_TimeSteps)
                {
                    time[I_T] = time_0 + I_T * time_step;
                }
                if (I_T > Nmb_of_TimeSteps && I_T <= 2 * Nmb_of_TimeSteps)
                {
                    time[I_T] = time_0 + (Nmb_of_TimeSteps + 1) * (I_T - Nmb_of_TimeSteps) * time_step;//10_1//10_0
                }
                if (I_T > 2 * Nmb_of_TimeSteps)
                {
                    time[I_T] = time_0 + (Nmb_of_TimeSteps + 1) * (Nmb_of_TimeSteps + 1) * (I_T - 2 * Nmb_of_TimeSteps) * time_step;// 200/3 //50
                }
                delta_t[I_T] = time[I_T] - time_0;
                for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                {
                    for (int i = 1; i <= 3; i++)
                    {
                        for (int j = 1; j <= 3; j++)
                        {
                            Cvv[i, j, I_W, I_T] = 0;
                            Cvv1[i, j, I_W, I_T] = 0;
                            for (int I_T1 = 0; I_T1 <= 3 * Nmb_of_TimeSteps; I_T1++)//3
                            {
                                for (int k = 1; k <= 3; k++)
                                {
                                    Cvvv[i, j, k, I_W, I_T, I_T1] = 0;
                                    Cvvv1[i, j, k, I_W, I_T, I_T1] = 0;
                                    for (int l = 1; l <= 3; l++)
                                    {
                                        CvvA[i, j, k, l, I_W, I_T, I_T1] = 0;
                                        CvvA1[i, j, k, l, I_W, I_T, I_T1] = 0;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            string path = @"c:\temp\T_corr1.txt";
            if (!File.Exists(path))
            {
                // Create a file to write to.
                using (StreamWriter sw = File.CreateText(path))
                {
                    for (int J = 0; J < Nmb_of_Cycles; J++)
                    {
                        for (int I = 0; I < Nmb_of_pts_1cycle; I++)
                        {
                            points[I] = new Point3();
                            points[I].x = (float)(random.NextDouble() * 2.0 * 3.14);
                            points[I].y = (float)(random.NextDouble() * 2.0 * 3.14);
                            points[I].z = (float)(random.NextDouble() * 2.0 * 3.14);
                            Theta[I] = (float)(random.NextDouble() * Math.PI);
                            Phi[I] = (float)(random.NextDouble() * 2 * Math.PI);
                            s[1, 1, I] = Math.Sin(Theta[I]) * Math.Cos(Phi[I]);
                            s[1, 2, I] = Math.Sin(Theta[I]) * Math.Sin(Phi[I]);
                            s[1, 3, I] = Math.Cos(Theta[I]);
                            s[2, 1, I] = Math.Cos(Theta[I]) * Math.Cos(Phi[I]);
                            s[2, 2, I] = Math.Cos(Theta[I]) * Math.Sin(Phi[I]);
                            s[2, 3, I] = -Math.Sin(Theta[I]);
                            s[3, 1, I] = -Math.Sin(Phi[I]);
                            s[3, 2, I] = Math.Cos(Phi[I]);
                            s[3, 3, I] = 0;
                            for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                            {
                                points2[I, I_W] = new Point3();
                                points2[I, I_W].x = points[I].x + (I_W) * Width * (float)(s[1, 1, I]);
                                points2[I, I_W].y = points[I].y + (I_W) * Width * (float)(s[1, 2, I]);
                                points2[I, I_W].z = points[I].z + I_W * Width * (float)(s[1, 3, I]);
                                points21[I, I_W] = new Point3();
                                points21[I, I_W].x = points[I].x + ((I_W + 1) * Width2) * (float)(s[1, 1, I]);
                                points21[I, I_W].y = points[I].y + ((I_W + 1) * Width2) * (float)(s[1, 2, I]);
                                points21[I, I_W].z = points[I].z + ((I_W + 1) * Width2) * (float)(s[1, 3, I]);
                            }
                        }
                        string authToken = @"jhu.edu.pha.turbulence.testing-201311";
                        string dataSet = @"isotropic1024";
                        SpatialInterpolation SpatInt_V = Turb.edu.jhu.pha.turbulence.SpatialInterpolation.M2Q14;
                        TemporalInterpolation TempInt = Turb.edu.jhu.pha.turbulence.TemporalInterpolation.None;
                        for (int I_T = 0; I_T <= 3 * Nmb_of_TimeSteps; I_T++)//3
                        {
                            for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                            {
                                for (int I = 0; I < Nmb_of_pts_1cycle; I++)
                                {
                                    points3[I] = new Point3();
                                    points3[I].x = points2[I, I_W].x;
                                    points3[I].y = points2[I, I_W].y;
                                    points3[I].z = points2[I, I_W].z;
                                    points31[I] = new Point3();
                                    points31[I].x = points21[I, I_W].x;
                                    points31[I].y = points21[I, I_W].y;
                                    points31[I].z = points21[I, I_W].z;
                                }
                                Veloc3 = service.GetVelocity(authToken, dataSet, time[I_T], SpatInt_V, TempInt, points3);
                                VelGr3 = service.GetVelocityGradient(authToken, dataSet, time[I_T], SpatInt_V, TempInt, points3);
                                Veloc31 = service.GetVelocity(authToken, dataSet, time[I_T], SpatInt_V, TempInt, points31);
                                VelGr31 = service.GetVelocityGradient(authToken, dataSet, time[I_T], SpatInt_V, TempInt, points31);
                                for (int I = 0; I < Nmb_of_pts_1cycle; I++)
                                {
                                    Veloc2[I, I_W, I_T] = Veloc3[I];
                                    Veloc21[I, I_W, I_T] = Veloc31[I];
                                    VelGr2[I, I_W, I_T] = VelGr3[I];
                                    VelGr21[I, I_W, I_T] = VelGr31[I];
                                }
                                Console.WriteLine("J={0}, I_T={1}, I_W={2}", J, I_T, I_W);
                            }
                        }
                        for (int I = 0; I < Nmb_of_pts_1cycle; I++)
                        {
                            for (int I_T = 0; I_T <= 3 * Nmb_of_TimeSteps; I_T++)//3
                            {
                                for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                                {
                                    for (int i = 1; i <= 3; i++)
                                    {
                                        v[i, I_W, I_T] = Veloc2[I, I_W, I_T].x * s[i, 1, I] + Veloc2[I, I_W, I_T].y * s[i, 2, I] + Veloc2[I, I_W, I_T].z * s[i, 3, I];
                                        v1[i, I_W, I_T] = Veloc21[I, I_W, I_T].x * s[i, 1, I] + Veloc21[I, I_W, I_T].y * s[i, 2, I] + Veloc21[I, I_W, I_T].z * s[i, 3, I];
                                        for (int j = 1; j <= 3; j++)
                                        {
                                            A[i, j, I_W, I_T] = VelGr2[I, I_W, I_T].duxdx * s[i, 1, I] * s[j, 1, I] + VelGr2[I, I_W, I_T].duydx * s[i, 2, I] * s[j, 1, I] + VelGr2[I, I_W, I_T].duzdx * s[i, 3, I] * s[j, 1, I] + VelGr2[I, I_W, I_T].duxdy * s[i, 1, I] * s[j, 2, I] + VelGr2[I, I_W, I_T].duydy * s[i, 2, I] * s[j, 2, I] + VelGr2[I, I_W, I_T].duzdy * s[i, 3, I] * s[j, 2, I] + VelGr2[I, I_W, I_T].duxdz * s[i, 1, I] * s[j, 3, I] + VelGr2[I, I_W, I_T].duydz * s[i, 2, I] * s[j, 3, I] + VelGr2[I, I_W, I_T].duzdz * s[i, 3, I] * s[j, 3, I];
                                            A1[i, j, I_W, I_T] = VelGr21[I, I_W, I_T].duxdx * s[i, 1, I] * s[j, 1, I] + VelGr21[I, I_W, I_T].duydx * s[i, 2, I] * s[j, 1, I] + VelGr21[I, I_W, I_T].duzdx * s[i, 3, I] * s[j, 1, I] + VelGr21[I, I_W, I_T].duxdy * s[i, 1, I] * s[j, 2, I] + VelGr21[I, I_W, I_T].duydy * s[i, 2, I] * s[j, 2, I] + VelGr21[I, I_W, I_T].duzdy * s[i, 3, I] * s[j, 2, I] + VelGr21[I, I_W, I_T].duxdz * s[i, 1, I] * s[j, 3, I] + VelGr21[I, I_W, I_T].duydz * s[i, 2, I] * s[j, 3, I] + VelGr21[I, I_W, I_T].duzdz * s[i, 3, I] * s[j, 3, I];
                                        }
                                    }
                                }
                            }
                            for (int I_T = 0; I_T <= 3 * Nmb_of_TimeSteps; I_T++)//3
                            {
                                for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                                {
                                    for (int i = 1; i <= 3; i++)
                                    {
                                        for (int j = 1; j <= 3; j++)
                                        {
                                            Cvv[i, j, I_W, I_T] += (v[i, I_W, 0] - v[i, 0, 0]) * (v[j, I_W, I_T] - v[j, 0, I_T]);
                                            Cvv1[i, j, I_W, I_T] += (v1[i, I_W, 0] - v[i, 0, 0]) * (v1[j, I_W, I_T] - v[j, 0, I_T]);
                                            for (int I_T1 = 0; I_T1 <= 3 * Nmb_of_TimeSteps; I_T1++)//3
                                            {
                                                for (int k = 1; k <= 3; k++)
                                                {
                                                    Cvvv[i, j, k, I_W, I_T, I_T1] += (v[i, I_W, 0] - v[i, 0, 0]) * (v[j, I_W, I_T] - v[j, 0, I_T]) * (v[k, I_W, I_T1] - v[k, 0, I_T1]);
                                                    Cvvv1[i, j, k, I_W, I_T, I_T1] += (v1[i, I_W, 0] - v[i, 0, 0]) * (v1[j, I_W, I_T] - v[j, 0, I_T]) * (v1[k, I_W, I_T1] - v[k, 0, I_T1]);
                                                    for (int l = 1; k <= 3; k++)
                                                    {
                                                        CvvA[i, j, k, l, I_W, I_T, I_T1] += (v[i, I_W, 0] - v[i, 0, 0]) * (v[j, I_W, I_T] - v[j, 0, I_T]) * (A[k, l, I_W, I_T1] + A[k, l, 0, I_T1]);
                                                        CvvA1[i, j, k, l, I_W, I_T, I_T1] += (v1[i, I_W, 0] - v[i, 0, 0]) * (v1[j, I_W, I_T] - v[j, 0, I_T]) * (A1[k, l, I_W, I_T1] + A[k, l, 0, I_T1]);
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                            Nmb_of_pts++;
                        }
                    }
                    sw.WriteLine("Nmb_of_pts={0}, time_0={1}", Nmb_of_pts, time_0);
                    sw.WriteLine(" ");
                    for (int I_T = 0; I_T <= 3 * Nmb_of_TimeSteps; I_T++)//3
                    {
                        for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                        {
                            for (int i = 1; i <= 3; i++)
                            {
                                for (int j = 1; j <= 3; j++)
                                {
                                    Cvv[i, j, I_W, I_T] = Cvv[i, j, I_W, I_T] / Nmb_of_pts;
                                    Cvv1[i, j, I_W, I_T] = Cvv1[i, j, I_W, I_T] / Nmb_of_pts;
                                    for (int I_T1 = 0; I_T1 <= 3 * Nmb_of_TimeSteps; I_T1++)//3
                                    {
                                        for (int k = 1; k <= 3; k++)
                                        {
                                            Cvvv[i, j, k, I_W, I_T, I_T1] = Cvvv[i, j, k, I_W, I_T, I_T1] / Nmb_of_pts;
                                            Cvvv1[i, j, k, I_W, I_T, I_T1] = Cvvv1[i, j, k, I_W, I_T, I_T1] / Nmb_of_pts;
                                            for (int l = 1; k <= 3; k++)
                                            {
                                                CvvA[i, j, k, l, I_W, I_T, I_T1] = CvvA[i, j, k, l, I_W, I_T, I_T1] / Nmb_of_pts;
                                                CvvA1[i, j, k, l, I_W, I_T, I_T1] = CvvA1[i, j, k, l, I_W, I_T, I_T1] / Nmb_of_pts;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    sw.WriteLine(" ");
                    for (int I_W = 0; I_W <= Nmb_of_Widths; I_W++)
                    {
                        sw.WriteLine("r={0}; ", I_W * Width);
                        sw.WriteLine(" ");
                        sw.WriteLine(" ");
                        sw.WriteLine("tau; ");//delta-t
                        for (int I_T = 0; I_T <= 3 * Nmb_of_TimeSteps; I_T++)
                        {
                            sw.WriteLine("{0}; ", delta_t[I_T]);
                        }
                    }
                }
            }
        }
    }
}
