using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;

namespace PureCode.CtpCSharp
{
    interface DllLoadUtils
    {
        IntPtr LoadLibrary(string fileName);
        void FreeLibrary(IntPtr handle);
        IntPtr GetProcAddress(IntPtr dllHandle, string name);
    }
    public class DllLoadUtilsWindows : DllLoadUtils
    {
        void DllLoadUtils.FreeLibrary(IntPtr handle)
        {
            FreeLibrary(handle);
        }

        IntPtr DllLoadUtils.GetProcAddress(IntPtr dllHandle, string name)
        {
            return GetProcAddress(dllHandle, name);
        }

        IntPtr DllLoadUtils.LoadLibrary(string fileName)
        {
            return LoadLibrary(fileName);
        }

        [DllImport("kernel32")]
        private static extern IntPtr LoadLibrary(string fileName);

        [DllImport("kernel32.dll")]
        private static extern int FreeLibrary(IntPtr handle);

        [DllImport("kernel32.dll")]
        private static extern IntPtr GetProcAddress(IntPtr handle, string procedureName);
    }

    internal class DllLoadUtilsLinux : DllLoadUtils
    {
        public IntPtr LoadLibrary(string fileName)
        {
            return dlopen(fileName, RTLD_NOW);
        }

        public void FreeLibrary(IntPtr handle)
        {
            dlclose(handle);
        }

        public IntPtr GetProcAddress(IntPtr dllHandle, string name)
        {
            // clear previous errors if any
            dlerror();
            var res = dlsym(dllHandle, name);
            var errPtr = dlerror();
            if (errPtr != IntPtr.Zero)
            {
                throw new Exception("dlsym: " + Marshal.PtrToStringAnsi(errPtr));
            }
            return res;
        }

        const int RTLD_NOW = 2;

        [DllImport("libdl.so")]
        private static extern IntPtr dlopen(String fileName, int flags);

        [DllImport("libdl.so")]
        private static extern IntPtr dlsym(IntPtr handle, String symbol);

        [DllImport("libdl.so")]
        private static extern int dlclose(IntPtr handle);

        [DllImport("libdl.so")]
        private static extern IntPtr dlerror();
    }

    public class AssembyLoader
    {

        public static IntPtr LoadLibrary(string libName)
        {
            var loader = new AssembyLoader(libName);
            return loader.dllHandle;
        }

        public AssembyLoader(string libName)
        {
            init(libName);
        }

        private bool IsLinux()
        {
            var p = (int)Environment.OSVersion.Platform;
            return (p == 4) || (p == 6) || (p == 128);
        }

        private DllLoadUtils dllLoadUtils;

        private IntPtr dllHandle;

        private void init(string libName)
        {
            dllLoadUtils = IsLinux() ? (DllLoadUtils)new DllLoadUtilsLinux() : new DllLoadUtilsWindows();
            if (IsLinux())
            {
                libName = libName.Replace(".dll", ".so");
            }

            if (!File.Exists(libName))
            {
                if(File.Exists(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, libName)))
                {
                    libName = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, libName);
                }
                else if(File.Exists(Path.Combine(Environment.CurrentDirectory, libName)))
                {
                    libName = Path.Combine(Environment.CurrentDirectory, libName);
                }
                else
                {
                    throw new Exception("not find file:" + libName);
                }
            }

            dllHandle = dllLoadUtils.LoadLibrary(libName);
        }

        public IntPtr GetDllHandle()
        {
            return dllHandle;
        }

        public Delegate Invoke(string funcName, Type type)
        {            
            var functionHandle = dllLoadUtils.GetProcAddress(dllHandle, funcName);

            var method = Marshal.GetDelegateForFunctionPointer(functionHandle, type);
            return method;
        }

        public Delegate Invoke(IntPtr pHModule, string lpProcName, Type t)
        {            
            // 若函数库模块的句柄为空，则抛出异常
			if (pHModule == IntPtr.Zero)
			{
				throw (new Exception(" 函数库模块的句柄为空 , 请确保已进行 LoadDll 操作 !"));
			}
			// 取得函数指针
			IntPtr farProc = dllLoadUtils.GetProcAddress(pHModule, lpProcName);
			// 若函数指针，则抛出异常
			if (farProc == IntPtr.Zero)
			{
				throw (new Exception(" 没有找到 :" + lpProcName + " 这个函数的入口点 "));
			}
            
			return Marshal.GetDelegateForFunctionPointer(farProc, t);
        }
    }

    public static class StringExtend
    {
        public static unsafe string GetString(byte[] array)
        {
            if (array == null || array.Length == 0)
                return string.Empty;

            int len = 0;
            for (var i = 0; i < array.Length; i++)
            {
                if (array[i] == 0)
                {
                    len = i;
                    break;
                }
            }

            fixed (byte* p = array)
            {
                var s = encoding.GetString(p, len);
                return s;
            }
        }

        /// <summary>
        /// 这个不是一个单纯转码函数，因为返回去的数组必须定长
        /// </summary>
        /// <param name="str"></param>
        /// <param name="length"></param>
        /// <returns></returns>
        public static byte[] GetBytes(string str, int length)
        {
            byte[] bytes = new byte[length];

            if (string.IsNullOrEmpty(str))
            {
                return bytes;
            }

            byte[] strBytes = encoding.GetBytes(str);
            if(strBytes.Length == length)
            {
                return strBytes;
            }

            Array.Copy(strBytes, bytes, Math.Min(length, strBytes.Length));

            return bytes;
        }

        static Encoding encoding = CodePagesEncodingProvider.Instance.GetEncoding("GB2312");
    }

}
