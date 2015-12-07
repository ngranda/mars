import atmosphere_splitter
def print_file():
   print "TITLE"
   print ""
   print "* Set the defaults for precision simulations"
   print "DEFAULTS                                                              PRECISIO"
   print "* Define the beam characteristics"
   print "BEAM            -1.0                                                  PROTON"
   print "* Define the beam position"
   print "SOURCE           0.0       0.0       0.0     2.0E6     2.0E6     9.9E8GCR"
   print "SOURCE      3.3895E8                                                   &"
   print "*"
   print "GEOBEGIN                                                              COMBNAME"
   print "    0    0"
   print "* Mars Radius"
   atmosphere_splitter.atmosphere_radius()
   print "SPH MARS       0.0 0.0 -3.4895E8 3.48950E+08"
   print "SPH TOPATMOS   0.0 0.0 -3.4895E8 3.68950E+08"
   print "RPP REGION     -1E6 1E6 -1E6 1E6 -1E6 1E6"
   print "XYP AT_CUT     -1E6"
   print "XYP SURFACE    0.0" + "\n" + "SPH UNIVERSE   0.0 0.0 -3.3895E8 1E9"
   print "ELL CRTR1      0.0 0.0 4.714E5 0.0 0.0 -4.714E5 1E6"
   print "END"
   print "* Black hole"
   print "MARS         5 +MARS -REGION" +"\n" +"UNIVERSE     5 -UNIVERSE"
   print "DEEPSPAC     5 -TOPATMOS +UNIVERSE"+"\n"+"GROUND       5 +REGION +MARS"
   print "AVEATMOS     5 +TOPATMOS -MARS +AT_CUT"
   atmosphere_splitter.region()
   print "END" + "\n" + "GEOEND"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   print "MATERIAL          1.        1.       1.6       26.                    REGOLITH"
   print "MATERIAL         25. 54.938044       7.9       27.                    MANGANES"
   print "LOW-MAT     MANGANES       25.       55.       87.                    MANGANES"
   print "MATERIAL         16.     32.06       2.8       28.                    SULFUR"
   print "LOW-MAT       SULFUR       16.       -2.       87.                    SULFUR"
   print "MATERIAL         19.   39.0983       3.0       29.                    POTASSIU"
   print "LOW-MAT     POTASSIU       19.       -2.       87.                    POTASSIU"
   print "MATERIAL         15.  30.97376       3.0       30.                    PHOSPHO"
   print "MATERIAL         17.     35.45       3.0       31.                    CHLORINE"
   print "LOW-MAT     CHLORINE       17.       -2.       87.                    CHLORINE"
   print "MATERIAL         24.   51.9961       2.0       32.                    CHROMIUM"
   print "LOW-MAT     CHROMIUM       24.       -2.       87.                    CHROMIUM"
   print "MATERIAL         30.    65.382       3.0       33.                    ZINC"
   print "LOW-MAT         ZINC       30.       -2.       87.                    ZINC"
   print "MATERIAL         35.    79.904       2.0       34.                    BROMINE"
   print "LOW-MAT      BROMINE       35.       -2.       87.                    BROMINE"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   print "COMPOUND      -.3621    OXYGEN   -.03259    SODIUM     -.082  MAGNESIUREGOLITH"
   print "COMPOUND      -.1085  ALUMINUM   -.04107   SILICON  -.006391   PHOSPHOREGOLITH"
   print "COMPOUND     -.04189    SULFUR   -.01046  CHLORINE  -.008684  POTASSIUREGOLITH"
   print "COMPOUND      -.1047   CALCIUM   -.02508  TITANIUM   -.02576  CHROMIUMREGOLITH"
   print "COMPOUND     -.00324  MANGANES   -.03252      IRON   -.06276    NICKELREGOLITH"
   print "COMPOUND     -.04812      ZINC  -.004184   BROMINE                    REGOLITH"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   print "MATERIAL          1.        1.        1.       35.                    ATMOSPHE"
   print "MATERIAL          1.  1.007825       1.0       36.                    HYDROG-1"
   print "LOW-MAT     HYDROG-1        1.        1.       87.                    HYDROG-1"
   print "MATERIAL          1.2.01410178       1.0       37.                    DEUTERIU"
   print "LOW-MAT     DEUTERIU        1.        2.       87.                    DEUTERIU"
   print "MATERIAL         10.   20.1797       1.0       38.                    NEON"
   print "LOW-MAT         NEON       35.       -2.       87.                    BROMINE"
   print "MATERIAL         36.   83.7982       1.0       39.                    KRYPTON"
   print "LOW-MAT      KRYPTON       36.       -2.      120.                    KRYPTON"
   print "MATERIAL         54.   131.293       1.0       40.                    XENON"
   print "LOW-MAT        XENON       54.       -2.       87.                    XENON"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   print "COMPOUND     -.01017  HYDROGEN  -.004817  HYDROG-1  -.009626  DEUTERIUATMOSPHE"
   print "COMPOUND     -.06379    CARBON    -.1333      NEON    -.4146    OXYGENATMOSPHE"
   print "COMPOUND     -.09091      NEON   -.09091     ARGON   -.09091   KRYPTONATMOSPHE"
   print "COMPOUND     -.09091     XENON                                        ATMOSPHE"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   atmosphere_splitter.density_input()
   print "* densit less than 1e-9 g/cc breaks things"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   print "ASSIGNMA    REGOLITH      MARS" + "\n" + "ASSIGNMA    BLCKHOLE  UNIVERSE"
   print "ASSIGNMA    REGOLITH    GROUND"
   print "ASSIGNMA      VACUUM  DEEPSPAC"
   print "ASSIGNMA      ATMOS8  AVEATMOS"
   atmosphere_splitter.assign_density()
   print "EMF"
   print "LOW-NEUT        260.                           0.0                -11."
   atmosphere_splitter.proton_usrbdx()
   atmosphere_splitter.neutron_usrbdx()
   atmosphere_splitter.electron_usrbdx()
   atmosphere_splitter.muons_usrbdx()
   atmosphere_splitter.photon_usrbdx()
   atmosphere_splitter.helium3_usrbdx()
   atmosphere_splitter.helium4_usrbdx()
   atmosphere_splitter.triton_usrbdx()
   atmosphere_splitter.deuteron_usrbdx()
   atmosphere_splitter.heavyion_usrbdx()
   print "USRTRACK         -1.    PROTON      -24.    GROUND        1.     1000.pro"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.   NEUTRON      -24.    GROUND        1.     1000.neu"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.  ELECTRON      -24.    GROUND        1.     1000.ele"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.     MUONS      -24.    GROUND        1.     1000.mu"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.    PHOTON      -24.    GROUND        1.     1000.pho"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.  3-HELIUM      -24.    GROUND        1.     1000.he3"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.  4-HELIUM      -24.    GROUND        1.     1000.he4"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.    TRITON      -24.    GROUND        1.     1000.tri"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.  DEUTERON      -24.    GROUND        1.     1000.deu"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.  HEAVYION      -24.    GROUND        1.     1000.h"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRTRACK         -1.   DOSE-EQ      -24.    GROUND        1.     1000.dose-eq"
   print "USRTRACK          1.      1E-6                                         &"
   print "USRBIN           10.   DOSE-EQ      -38.     5.1E5     5.1E5   5.002E5TOP"
   print "USRBIN           0.0       0.0     5.0E5     2550.     2550.        1. &"
   print "USRBIN           10.   DOSE-EQ      -39.     5.1E5     5.1E5   2.502E5HALFWAY"
   print "USRBIN           0.0       0.0     2.5E5     2550.     2550.        1. &"
   print "USRBIN           10.   DOSE-EQ      -40.     5.1E5     5.1E5      100.GROUND"
   print "USRBIN           0.0       0.0     -100.     2550.     2550.        1. &"
   print "USRBIN           10.   DOSE-EQ      -41.      100.     5.1E5     5.1E5Half-side"
   print "USRBIN         -100.       0.0       0.0        1.     2550.     2550. &"
   print "USRBIN           10.   DOSE-EQ      -42.    10000.       1E6     1.5E7Side_dose"
   print "USRBIN           0.0      -1E6       0.0        1.      200.     1500. &"
   print "USRBIN           10.  BEAMPART      -43.    10000.       1E6     1.5E7Side_beamp"
   print "USRBIN           0.0      -1E6       0.0        1.      200.     1500. &"
   print "USRBIN           10.   NEUTRON      -44.    10000.       1E6     1.5E7Side_neu"
   print "USRBIN           0.0      -1E6       0.0        1.      200.     1500. &"
   print "* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7.."
   print "* Set the random number seed"
   print "RANDOMIZ         1.0"
   print "* Set the number of primary histories to be simulated in the run"
   print "START          1.0E6                            1."
   print "STOP"

# generate the file for input into flair
print_file()


