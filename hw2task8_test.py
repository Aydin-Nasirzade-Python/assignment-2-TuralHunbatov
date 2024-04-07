import Task_8
from random import choice, randint
import unittest
from unittest.mock import patch
from io import StringIO

class TestMainFunction(unittest.TestCase):

  def test_input(self):
        input_value = [(-4.4057254536046075, 3.521382459550379, False), (-0.5188984078845564, 22.17673033620724, False), (-0.8954359440924726, 0.8352790409735661, False), (-3.352353702591394, 13.309747180573952, False), (-0.002785803185985536, 22.617266697574525, False), (-3.5888003094584016, 21.17273113191961, False), (-1.5540181774281097, 5.230071139987616, False), (-0.8321934641142974, 6.941648232264496, False), (-1.2207686459877731, 6.022967541906529, False), (-3.1769523274123412, 5.899640472261599, True), (-0.6917631355170144, 11.719803644239866, False), (-4.895086953260519, 12.508356048169711, True), (-4.7956081825803185, 7.3105187954098065, True), (-3.528483715755299, 8.186718866535605, True), (-3.4202279297764844, 0.46466290223321494, False), (-0.3895277269320232, 6.922346230787535, False), (-0.05512442221976688, 3.310424954169555, False), (-4.287624850402395, 23.22967124486319, False), (-4.9253106638886965, 18.57830091885543, True), (-1.2033354249591524, 0.7366307172879755, False), (-3.1239415513879876, 3.8509054542133465, False), (-2.2617039464304236, 4.483799491712914, True), (-0.7025837774897177, 8.575034867195807, False), (-1.1986356282039612, 10.010491574114349, False), (-0.7798962194277639, 1.5680489456127378, False), (0.3743555757099939, 0.028907062541600692, True), (-1.7324782361781905, 3.6970991198313916, False), (-0.44695148933857065, 5.566560934643291, False), (-0.7622870898441119, 4.972356218767171, False), (-0.4832882628587032, 4.895746840940549, False), (-0.14829528257338764, 3.8800831403313025, False), (-1.5486483023186388, 4.969655288973656, False), (-1.1786426290774863, 1.6966238548815418, False), (-1.1481505766369875, 3.9575441004332577, False), (-0.5862290369319443, 5.549418915321471, False), (-0.6875335589101206, 0.01577512936128911, False), (-0.6126701701641211, 2.0547286126873856, False), (-1.703854404989671, 2.0831432361936457, False), (-1.6774748470808822, 4.468363544771025, False), (-1.2474578461880317, 5.903611611264205, False), (-1.4312038995993346, 1.4504039479891224, False), (-1.2126221255530947, 0.880742658611622, False), (-0.4392588965346591, 5.421390219891745, False), (-1.166733134157046, 1.0861634460373468, False), (-0.9727556585066013, 4.83864600130343, False), (-0.24783081260599893, 5.932280809200647, False), (-0.5438700501188976, 2.8408690726877057, False), (-0.25711138980085146, 0.778136968566894, False), (-1.7103755306106252, 1.3209291081276733, False), (-0.6133976986080727, 1.8470783158342954, False), (0.6403142830095438, 1.0064348106404948, False), (0.2391628052556004, -0.7652228301318331, False), (0.564140729927072, -1.5333779765351931, False), (0.9091064310564276, -2.5334595032850666, False), (0.2502550104003358, -0.19031652696836687, False), (0.4651260599702036, -0.851173798184953, False), (0.42969630313125695, -0.46656457665914175, False), (0.3697282583765472, -2.1395979378693184, False), (0.7052380504928529, -1.0546817524772583, False), (0.40699827234070596, -2.0546457476446056, False), (0.8028732659824398, -1.5453097628775014, False), (0.8578687936075029, -1.6592739773101877, False), (0.31794203166327406, -1.1233632057271743, False), (0.9469273980159315, -1.8806951368643614, False), (0.813217602584455, -0.6902103927069758, False), (0.8153618921253785, -0.37827037873860014, False), (0.13398239667357192, -0.7615088015087088, False), (0.5506165001793834, -0.6615879451855422, False), (0.7950268161339741, -0.1936699005422846, False), (0.4551933140858383, -0.3779077290427031, False), (0.23788161607701064, -0.8130226471557949, False), (0.047974817325248886, -2.045156012197782, False), (0.4218687838465639, -0.7840734486787833, False), (0.26959789056959227, -2.344006613832153, False), (0.5926548219644565, -2.2634865771537047, False), (1.4118886369104555, 0.42240557672057494, True), (0.41597707936173034, 0.5858613161477173, False), (1.9375574774510698, 0.503199272846271, False), (0.16298815700783775, 1.394837473448191, False), (1.5302332790669846, 0.8637689393172059, False), (1.6618338982485221, 0.27636072576289655, True), (1.8138524386532349, 0.4480662422134758, False), (1.9234020043323805, 0.6377939860296717, False), (0.3336199970081084, 1.409321322044387, False), (1.4630544766700557, 0.27534695290288486, True), (0.01295797987867453, 0.7262221346571216, False), (0.5920596812911443, 0.13684747243944656, True), (0.34179045405166875, 0.9338713461944566, False), (0.7680761416994617, 0.19401590932381946, True), (0.4881070861702388, 0.5949766908191598, False), (0.32179723554394957, 1.2756042722853314, False), (1.3943974379120518, 0.9795348991527437, False), (1.4449354940397732, 0.05139049088000175, True), (0.07820558615650319, 0.7196265580380796, False), (1.6678321239389196, 0.7330853176118243, False), (0.6225644768699459, 0.19917863947626874, True), (1.7785937876890083, 1.4703615357975486, False), (1.342813274025097, 1.1235211848705924, False), (1.3559361257496312, 0.20565672226999215, True), (1.9824266351247473, 1.0461161524487999, False)]
        expected_output = ("The point is not in the shaded area", "The point is in the shaded area")
        
        for _ in range(randint(10,30)):
            test = choice(input_value)
            with patch('builtins.input', side_effect=test[:2]), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_8.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output[test[2]])

if __name__ == '__main__':
    unittest.main()