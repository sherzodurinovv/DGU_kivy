
def resid_burgers ( nu, n, x, y, z, t ):
  import numpy as np
  from scipy.special import erf

  u =   2.0 * x
  ux =  2.0 * np.ones ( n )
  uxx = np.zeros ( n )
  uy =  np.zeros ( n )
  uyy = np.zeros ( n )
  uz =  np.zeros ( n )
  uzz = np.zeros ( n )
  ut =  np.zeros ( n )

  v =   - 2.0 * y
  vx =  np.zeros ( n )
  vxx = np.zeros ( n )
  vy =  - 2.0 * np.ones ( n )
  vyy = np.zeros ( n )
  vz =  np.zeros ( n )
  vzz = np.zeros ( n )
  vt =  np.zeros ( n )

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = erf ( y[i] / np.sqrt ( nu ) )
  wx =  np.zeros ( n )
  wxx = np.zeros ( n )
  wy =    2.0 * np.sqrt ( 1.0 / nu / np.pi )     * np.exp ( - y ** 2 / nu )
  wyy = - 4.0 * np.sqrt ( 1.0 / nu / np.pi ) * y * np.exp ( - y ** 2 / nu ) / nu
  wz =  np.zeros ( n )
  wzz = np.zeros ( n )
  wt =  np.zeros ( n )

  p = - 2.0 * ( x ** 2 + y ** 2 )
  px = - 4.0 * x
  py = - 4.0 * y
  pz = np.zeros ( n )

  ur = ut + u * ux + v * uy + w * uz + px - nu * ( uxx + uyy + uzz )
  vr = vt + u * vx + v * vy + w * vz + py - nu * ( vxx + vyy + vzz )
  wr = wt + u * wx + v * wy + w * wz + pz - nu * ( wxx + wyy + wzz )
  pr = ux + vy + wz

  return ur, vr, wr, pr

def resid_burgers_test ( ):


  import numpy as np
  import platform

  nu = 0.25

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  y = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  z = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  t = np.zeros ( n )

  ur, vr, wr, pr = resid_burgers ( nu, n, x, y, z, t )


  return f"resid_burgers_test\n Python version: %s' %{ ( platform.python_version ( ) )}\n'  resid_burgers evaluates the Burgers residual.'\n'  Sample at the initial time T = 0, using a region that is'\n'  the cube centered at (0,0,0) with radius 1.0,'\n '  Viscosity NU = %g' % {( nu )}\n'  Minimum    Maximum'\n '  Ur:  %14.6g  %14.6g' % {( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) )}\n'  Vr:  %14.6g  %14.6g' % {( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) }\n'  Wr:  %14.6g  %14.6g' % {( np.min ( np.abs ( wr ) ), np.max ( np.abs ( wr ) ) )}\n ' Pr:  %14.6g  %14.6g' % {( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )}\n'resid_burgers_test:'\n 'Normal end of execution.' "

def uvwp_burgers ( nu, n, x, y, z, t ):

  import numpy as np
  from scipy.special import erf

  u =   2.0 * x
  v =   - 2.0 * y
  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = erf ( y[i] / np.sqrt ( nu ) )
  p = - 2.0 * ( x ** 2 + y ** 2 )

  return u, v, w, p

def uvwp_burgers_test ( ):

#dastur qismi

  import numpy as np
  import platform

  nu = 0.25

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  y = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  z = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  t = np.zeros ( n )

  u, v, w, p = uvwp_burgers ( nu, n, x, y, z, t )

  return  f"'uvwp_burgers_test'\n '  Python version: %s' % {( platform.python_version ( ) )}\n '  UVWP samples the Burgers solution.'\n '  Estimate the range of velocity and pressure'\n '  at the initial time T = 0, using a region that is'\n'  the cube centered at (0,0,0) with radius 1.0,'\n '  Viscosity NU = %g' % {( nu )}\n '  U:  %14.6g  %14.6g' % {( np.min ( u ), np.max ( u ) )} '           Minimum       Maximum'\n'  V:  %14.6g  %14.6g' % {( np.min ( v ), np.max ( v ) )}\n'  W:  %14.6g  %14.6g' % {( np.min ( w ), np.max ( w ) )}\n'  P:  %14.6g  %14.6g' % {( np.min ( p ), np.max ( p ) ) }\n 'uvwp_burgers_test:'\n'  Normal end of execution.'"

def resid_ethier ( a, d, n, x, y, z, t ):

  import numpy as np
#
#  Make some temporaries.
#
  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2x = np.exp ( 2.0 * a * x )
  e2y = np.exp ( 2.0 * a * y )
  e2z = np.exp ( 2.0 * a * z )

  e2t = np.exp  ( -       d * d * t )
  e4t = np.exp  ( - 2.0 * d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )

  u =   -         a * (           ex * syz +         ez * cxy ) * e2t
  ux =  -         a * (       a * ex * syz -     a * ez * sxy ) * e2t
  uxx = -         a * (   a * a * ex * syz - a * a * ez * cxy ) * e2t
  uy =  -         a * (       a * ex * cyz -     d * ez * sxy ) * e2t
  uyy = -         a * ( - a * a * ex * syz - d * d * ez * cxy ) * e2t
  uz =  -         a * (       d * ex * cyz +     a * ez * cxy ) * e2t
  uzz =  -        a * ( - d * d * ex * syz + a * a * ez * cxy ) * e2t
  ut =  + d * d * a * (           ex * syz +         ez * cxy ) * e2t

  v =   -         a * (           ey * szx +         ex * cyz ) * e2t
  vx =  -         a * (       d * ey * czx +     a * ex * cyz ) * e2t
  vxx = -         a * ( - d * d * ey * szx + a * a * ex * cyz ) * e2t
  vy =  -         a * (       a * ey * szx -     a * ex * syz ) * e2t
  vyy = -         a * (   a * a * ey * szx - a * a * ex * cyz ) * e2t
  vz =  -         a * (       a * ey * czx -     d * ex * syz ) * e2t
  vzz =  -        a * ( - a * a * ey * szx - d * d * ex * cyz ) * e2t
  vt =  + d * d * a * (           ey * szx +         ex * cyz ) * e2t

  w =   -         a * (           ez * sxy +         ey * czx ) * e2t
  wx =  -         a * (       a * ez * cxy -     d * ey * szx ) * e2t
  wxx = -         a * ( - a * a * ez * sxy - d * d * ey * czx ) * e2t
  wy =  -         a * (       d * ez * cxy +     a * ey * czx ) * e2t
  wyy = -         a * ( - d * d * ez * sxy + a * a * ey * czx ) * e2t
  wz =  -         a * (       a * ez * sxy -     a * ey * szx ) * e2t
  wzz = -         a * (   a * a * ez * sxy - a * a * ey * czx ) * e2t
  wt =  + d * d * a * (           ez * sxy +         ey * czx ) * e2t

  p = - 0.5 * a * a * e4t * ( \
    + e2x + 2.0 * sxy * czx * eyz \
    + e2y + 2.0 * syz * cxy * ezx \
    + e2z + 2.0 * szx * cyz * exy )

  px = - 0.5 * a * a * e4t * ( \
    + 2.0 * a * e2x + 2.0 * a * cxy * czx * eyz - 2.0 * d * sxy * szx * eyz \
                    - 2.0 * a * syz * sxy * ezx + 2.0 * a * syz * cxy * ezx \
                    + 2.0 * d * czx * cyz * exy + 2.0 * a * szx * cyz * exy )

  py = - 0.5 * a * a * e4t * ( \
                    + 2.0 * d * cxy * czx * eyz + 2.0 * a * sxy * czx * eyz \
    + 2.0 * a * e2y + 2.0 * a * cyz * cxy * ezx - 2.0 * d * syz * sxy * ezx \
                    - 2.0 * a * szx * syz * exy + 2.0 * a * szx * cyz * exy )

  pz = - 0.5 * a * a * e4t * ( \
                    - 2.0 * a * sxy * szx * eyz + 2.0 * a * sxy * czx * eyz \
                    + 2.0 * d * cyz * cxy * ezx + 2.0 * a * syz * cxy * ezx \
    + 2.0 * a * e2z + 2.0 * a * czx * cyz * exy - 2.0 * d * szx * syz * exy )
#
#  Evaluate the residuals.
#
  ur = ut + u * ux + v * uy + w * uz + px - ( uxx + uyy + uzz )
  vr = vt + u * vx + v * vy + w * vz + py - ( vxx + vyy + vzz )
  wr = wt + u * wx + v * wy + w * wz + pz - ( wxx + wyy + wzz )
  pr = ux + vy + wz;

  return ur, vr, wr, pr

def resid_ethier_test( ):


#dastur qismi
  import numpy as np
  import platform

  a = np.pi / 4.0
  d = np.pi / 2.0

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  y = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  z = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  t = np.zeros ( n )

  ur, vr, wr, pr = resid_ethier ( a, d, n, x, y, z, t )

  return f"'resid_ethier_test'\n'  Python version: %s' % {( platform.python_version ( ) )}\n '  resid_ethier evaluates the Ethier residual.'\n'  Sample the residuals'\n'  at the initial time T = 0, using a region that is'\n'  the cube centered at (0,0,0) with radius 1.0,'\n'  Parameter A = %g' % ( a )\n'  Parameter D = %g' % ( d )\n'           Minimum       Maximum'\n'  Ur:  %14.6g  %14.6g' % ({ np.min ( np.abs ( ur ) )}, np.max {( np.abs ( ur ) ) })\n '  Vr:  %14.6g  %14.6g' % ( np.min {( np.abs ( vr ) )}, np.max {( np.abs ( vr ) ) })\n'  Wr:  %14.6g  %14.6g' % ( np.min {( np.abs ( wr ) )}, np.max {( np.abs ( wr ) ) }\n'  Pr:  %14.6g  %14.6g' % {( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )}\n'resid_ethier_test:'\n'  Normal end of execution.'"

def uvwp_ethier ( a, d, n, x, y, z, t ):

  import numpy as np

  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2t = np.exp  ( - d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )

  u = - a * ( ex * syz + ez * cxy ) * e2t
  v = - a * ( ey * szx + ex * cyz ) * e2t
  w = - a * ( ez * sxy + ey * czx ) * e2t
  p = 0.5 * a * a * e2t * e2t * ( \
    + ex * ex + 2.0 * sxy * czx * eyz \
    + ey * ey + 2.0 * syz * cxy * ezx \
    + ez * ez + 2.0 * szx * cyz * exy )

  return u, v, w, p

def uvwp_ethier_test ( ):

#*****************************************************************************80


  import numpy as np
  import platform

  a = np.pi / 4.0
  d = np.pi / 2.0

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  y = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  z = x_lo + ( x_hi - x_lo ) * np.random.rand ( n )
  t = np.zeros ( n )

  u, v, w, p = uvwp_ethier ( a, d, n, x, y, z, t )

#  Terminate.
#
  print ( '' )
  print ( )
  print ( )
  return  f" 'uvwp_ethier_test'\n'  Python version: %s' % {( platform.python_version ( ) )}\n'  uvwp_ethier evaluates the Ethier solution.'\n'  Estimate the range of velocity and pressure'\n'  at the initial time T = 0, using a region that is'\n'  the cube centered at (0,0,0) with radius 1.0,'\n '  Parameter A = %g' % ( a )\n'  Parameter D = %g' % ( d ) \n '           Minimum       Maximum'\n '  U:  %14.6g  %14.6g' % ( {np.min ( u ), np.max ( u ) })\n'  V:  %14.6g  %14.6g' % ( {np.min ( v ), np.max ( v ) })\n '  W:  %14.6g  %14.6g' % ( {np.min ( w ), np.max ( w ) })\n'  P:  %14.6g  %14.6g' % ( {np.min ( p ), np.max ( p )} )\n 'uvwp_ethier_test:'\n '  Normal end of execution.'"

def navier_stokes_3d_exact_test ( ):

  import platform

  print ( '' )
  print ( 'navier_stokes_3d_exact_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test navier_stokes_3d_exact()' )

  uvwp_burgers_test ( )
  resid_burgers_test ( )

  uvwp_ethier_test ( )
  resid_ethier_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'navier_stokes_3d_exact_test():' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def timestamp ( ):


  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  navier_stokes_3d_exact_test ( )
  timestamp ( )
