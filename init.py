from db2lin import db2lin

class Init:

  l = 400
  x_b = 2600
  y_b = 2600
  z_b = 30

  # The vehicles are in the range of a(meters) to b(meters) The distance of the two vehicles is set to be max. delta(meters)
  a = -500
  b = 500
  delta = 100

  p_s = .5 / ((3.9 * 10) ** (-14))
  p_r = .5 / ((3.9 * 10) ** (-14))
  p_v1 = .1 / ((3.9 * 10) ** (-14))
  p_v2 = .1 / ((3.9 * 10) ** (-14))

  f = 2e9
  c = 3e8

  # the variables needed for calculating the v2v pathloss Dual-slope Path Loss Model in Urban Scenarios
  PL_0 = 63.9   # reference path loss at the reference distance
  d_b = 161     # the breakpoint distance
  n1 = 1.81     # path loss exponents
  n2 = 2.85     # path loss exponents
  d_0 = 10      # reference distance

  # environment constants for the A2G channel model
  alpha_suburban = 5.0188
  beta_suburban = 0.3511
  eta_los_suburban = 0.1
  eta_nlos_suburban = 21

  alpha_urban = 9.6101
  beta_urban = 0.1592
  eta_los_urban = 1
  eta_nlos_urban = 20

  alpha_dense_urban = 11.9480
  beta_dense_urban = 0.1359
  eta_los_dense_urban = 1.6
  eta_nlos_dense_urban = 23

  alpha_high_urban = 27.1562
  beta_high_urban = 0.1225
  eta_los_high_urban = 2.3
  eta_nlos_high_urban = 34

  alpha = alpha_suburban #The environment constants for the probability of line of sight
  beta = beta_suburban # The environment constants for the probability of line of sight
  eta_los = db2lin(eta_los_suburban) # Additinal pathloss to free space for LOS
  eta_nlos = db2lin(eta_nlos_suburban)