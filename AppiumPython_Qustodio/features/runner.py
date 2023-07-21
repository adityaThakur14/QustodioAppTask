import argparse
import subprocess as subp
if __name__ == '__main__':
   p = argparse.ArgumentParser()
  #--testdir command line argument added
   p.add_argument('--testdir', required=False, help="File path")
   a = p.parse_args()
   testdir = a.testdir
   testdir = "features"
   #complete command
   c= f'behave --no-capture {testdir}'
   s = subp.run(c, shell=True, check=True)


