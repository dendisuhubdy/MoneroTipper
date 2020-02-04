import unittest

import helper
from helper import get_xmr_val
from tipbot.tip import parse_tip_amount

class mainTestCase(unittest.TestCase):

    helper.botname = "MoneroTip"

    def test_parse_tip_amount(self):
        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} 1.0 xmr", helper.botname) == "1.0")
        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} 1xmr", helper.botname) == "1")
        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} 5 xmr", helper.botname) == "5")
        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} tip 1 xmr", helper.botname) == "1")
        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} tip 1xmr", helper.botname) == "1")

        self.assertTrue(
            parse_tip_amount(f"/u/{helper.botname} 1 mxmr", helper.botname) == "0.001")
        self.assertTrue(
            parse_tip_amount(f"/u/{helper.botname} 1mxmr", helper.botname) == "0.001")
        self.assertTrue(
            parse_tip_amount(f"/u/{helper.botname} tip 1 mxmr", helper.botname) == "0.001")
        self.assertTrue(
            parse_tip_amount(f"/u/{helper.botname} tip 1mxmr", helper.botname) == "0.001")

        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} 1.0$", helper.botname) == str(
            get_xmr_val(1)))
        self.assertTrue(parse_tip_amount(f"/u/{helper.botname} $1", helper.botname) == str(
            get_xmr_val(1)))

        self.assertTrue(parse_tip_amount(f"Here's some stuff to throw the bot off:\n If you want to peer to peer trade Monero instead of using an exchange, check out LocalMonero: http://localmonero.co/\n/u/{helper.botname} 0.001 XMR", helper.botname) == "0.001")
